function confirmDelete(name, surname) {
    return confirm(name + ' ' + surname + ' adlı personeli silmek istediğinizden emin misiniz?');
}




// form validation
(function() {
    'use strict';
    window.addEventListener('load', function() {
      var forms = document.getElementsByClassName('needs-validation');
      var validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
          }
          form.classList.add('was-validated');
        }, false);
      });
    }, false);
  })();
  

  // Select2
$(document).ready(function() {
  $('.select2').select2({
    theme: 'bootstrap4',
    width: '100%'
  });
});