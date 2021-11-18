let contrySelected = $('#id_default_country').val();
if(!contrySelected) {
    $('id_default_country').css('color', '#aab7c4');
};
$('id_default_country').change(function(){
    countrySelected = $(rhis).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    }else{
        $(this).css('color', '#aab7c4');
    }
});
