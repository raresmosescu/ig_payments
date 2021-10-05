
$('.custom-switch-option').click(function() {
    let value = $('#package-switch-output').val();
    console.log(value);
    if (value == 'growth') {
        $('#growth-package').show();
        $('#sales-package').hide();
        $('#custom-package').hide();
    } else if (value == 'sales') {
        $('#sales-package').show();
        $('#growth-package').hide();
        $('#custom-package').hide();
    } else if (value == 'custom') {
        $('#growth-package').hide();
        $('#sales-package').hide();
        $('#custom-package').show();
    }
});
