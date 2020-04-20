$(document).ready(function () {
  $('#select-qty').on('change', function () {
    $('#qtyForm').submit();
  });

  $('.quantity').each(function () {
    const spinner = $(this),
      input = spinner.find('input[type="number"]'),
      btnUp = spinner.find('.quantity-up'),
      btnDown = spinner.find('.quantity-down'),
      btnDelete = spinner.find('.quantity-none'),
      min = input.attr('min'),
      max = input.attr('max');

    btnUp.click(function () {
      var oldValue = parseFloat(input.val());
      if (oldValue >= max) {
        var newVal = oldValue;
      } else {
        var newVal = oldValue + 1;
      }
      spinner.find('input').val(newVal);
      spinner.find('input').trigger('change');
    });

    btnDown.click(function () {
      var oldValue = parseFloat(input.val());
      if (oldValue <= min) {
        var newVal = oldValue;
      } else {
        var newVal = oldValue - 1;
      }
      spinner.find('input').val(newVal);
      spinner.find('input').trigger('change');
    });

    btnDelete.click(function () {
      var oldValue = parseFloat(input.val());
      if (oldValue > min) {
        var newVal = oldValue - oldValue;
      }

      spinner.find('input').val(newVal);
      spinner.find('input').trigger('change');
    });
  });
});
