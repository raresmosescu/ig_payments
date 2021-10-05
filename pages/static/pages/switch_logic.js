// Update would repeat output when option is clicked 
// YES/NO LOGIC BUTTONS

// custom switch style & logic 

function hover_style() {
    $('.custom-switch-option').each(function () {
        $(this).hover(function(){
            if (!$(this).hasClass('is-clicked')) { // if it DOESN'T have is-clicked class
                $(this).css("background-color", "green");
            }
        }, function(){
            if (!$(this).hasClass('is-clicked')) {
                $(this).css("background-color", "black");
            }
        });
    });
}

$('.custom-switch-option').click(function () {
    $('.custom-switch-option').css('background-color', '#000000').removeClass('is-clicked');
    $(this).css('background-color', '#48C774').addClass('is-clicked');
    let data = $(this).attr( "value" ) // the output will be based on the "value" attribute of the options
    $('.custom-switch-output').val(data);
    hover_style();
});

$(document).ready(function () {
    $('.custom-switch-option').css('background-color', '#000000').css('color', '#ffffff');
    hover_style();
});