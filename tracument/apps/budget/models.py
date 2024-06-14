from django.db import models
import datetime

class Currency (models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} ({self.short_name})"

    class Meta:
        verbose_name = "Para Birimi"
        verbose_name_plural = "Para Birimleri"
    

class AccountHolder (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Banka"
        verbose_name_plural = "Bankalar"

class TransactionPerson(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "İşlemi Yapan"
        verbose_name_plural = "İşlemi Yapanlar"

class BankAccount (models.Model):
    name = models.CharField(max_length=200)
    account_holder = models.ForeignKey(AccountHolder, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE)
    current_balance = models.DecimalField(decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.bank} ({self.currency})"

    class Meta:
        verbose_name = "Hesap"
        verbose_name_plural = "Hesaplar"


class CreditCard (models.Model):
    name = models.CharField(max_length=200)
    account_holder = models.ForeignKey(AccountHolder, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE)
    cutoff_day = models.IntegerField()
    pay_day = models.IntegerField()
    limit = models.DecimalField(decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.bank} ({self.currency})"

    class Meta:
        verbose_name = "Kredi Kartı"
        verbose_name_plural = "Kredi Kartları"

class BankTransaction (models.Model):
    DEPOSIT = 1
    WITHDRAWAL = 0
    TRANSFER = 2

    TRANSACTION_TYPE_CHOICES = [
        (DEPOSIT, 'Gelen'),
        (WITHDRAWAL, 'Giden'),
        (TRANSFER, 'Transfer'),
    ]

    source_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    destination_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='transfers', null=True, blank=True)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE_CHOICES)
    transaction_person = models.ForeignKey(TransactionPerson, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    date = models.DateField (default=datetime.date.today)
    amount = models.DecimalField(decimal_places=2)
    amount_after_transaction = models.DecimalField(decimal_places=2)

    def save(self, *args, **kwargs):
        if self.transaction_type == self.WITHDRAWAL:
            self.amount = -self.amount
            self.amount_after_transaction = self.source_account.current_balance + self.amount
            self.source_account.current_balance = self.amount_after_transaction
            self.source_account.save()
        
        elif self.transaction_type == self.DEPOSIT:
            self.amount_after_transaction = self.source_account.current_balance + self.amount
            self.source_account.current_balance = self.amount_after_transaction
            self.source_account.save()
        
        elif self.transaction_type == self.TRANSFER:
            if not self.destination_account:
                raise ValueError("Destination account must be set for transfer transactions.")
            if self.source_account.current_balance < self.amount:
                raise ValueError("Insufficient funds for transfer.")

            # Decrease balance from source account
            self.source_account.current_balance -= self.amount
            self.source_account.save()

            # Create a transaction record for the source account
            source_transaction = BankTransaction(
                source_account=self.source_account,
                transaction_type=self.WITHDRAWAL,
                transaction_person=self.transaction_person,
                description=f'Transfer to {self.destination_account.account_number}',
                date=self.date,
                amount=-self.amount,
                amount_after_transaction=self.source_account.current_balance
            )
            source_transaction.save()

            # Increase balance in destination account
            self.destination_account.current_balance += self.amount
            self.destination_account.save()

            # Create a transaction record for the destination account
            destination_transaction = BankTransaction(
                source_account=self.destination_account,
                transaction_type=self.DEPOSIT,
                transaction_person=self.transaction_person,
                description=f'Transfer from {self.source_account.account_number}',
                date=self.date,
                amount=self.amount,
                amount_after_transaction=self.destination_account.current_balance
            )
            destination_transaction.save()

            # Return as this instance is handled by the created transactions
            return
        
        super(BankTransaction, self).save(*args, **kwargs)