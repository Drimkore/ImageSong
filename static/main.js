$(document).ready(function(){

    $('#postAns').click(function(){
        $.ajax({
            url: '/answer',
            type: 'post',
            dataType: 'json',
            data: $('form').serialize(),
            beforeSend: function()
            {
                //$('samp[name="output_field"]').html('');
            },
            success: function(response){
                //$('img[name="check"]').attr( "src", `${response.result}`)
                alert(response.result)
                
            }
        })
     }) 

    $('#getGen').click(function(){
        $.ajax({
            url: '/generate',
            type: 'get',
            dataType: 'json',
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