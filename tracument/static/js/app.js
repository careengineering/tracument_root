function confirmDelete(name, surname) {
  if (confirm(`'${name} ${surname}' adlı personeli silmek istediğinizden emin misiniz?`)) {
      return true;
  }
  return false;
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
  $('.filter-form select').select2();

  $('.filter-form select').on('change', function() {
      $(this).closest('form').submit();
  });
});
