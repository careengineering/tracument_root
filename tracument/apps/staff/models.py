from django.db import models

class Unit (models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Birim"
        verbose_name_plural = "Birimler"


class Title (models.Model):
    name = models.CharField(max_length=200, unique=True)
    short_name = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Unvan"
        verbose_name_plural = "Unvanlar"


class Duty (models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gorev"
        verbose_name_plural = "Gorevler"


class Payroll (models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kadro"
        verbose_name_plural = "Kadrolar"

class Staff(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    duty = models.ManyToManyField(Duty)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Personel"
        verbose_name_plural = "Personeller"


