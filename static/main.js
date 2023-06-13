$(document).ready(function(){

    $('.btn').click(function(){
        $.ajax({
            url: '',
            type: 'post',
            dataType: 'json',
            data: $('form').serialize(),
            beforeSend: function()
            {
                $('samp[name="output_field"]').html('');
            },
            success: function(response){
                $('img[name="check"]').attr( "src", `${response.result}`)
                
            }
        })
    })
})

$(document).ajaxSend(function(event, request, settings) {
    $('#loading-indicator').show();
});

$(document).ajaxComplete(function(event, request, settings) {
    $('#loading-indicator').hide();
})