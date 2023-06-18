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
                if (response.result == true){
                    $('#score').text(`${response.score}`)
                    $('#getGen').click()
                }
                else {
                    console.log(response.lives)
                    $('#qwe').text(`${response.lives}`)
                    if (response.lives == 0){
                        location.reload()
                    }  
                }
            }
        })
     })
     
    let click = 0;  

     $('#getHelp').click(function(){
        $.ajax({
            url: '/help',
            type: 'get',
            dataType: 'text',
            beforeSend: function()
            {
                //$('samp[name="output_field"]').html('');
            },
            success: function(response){
                console.log(response)
                click +=1
                $('#help').append(document.createTextNode(`${response + ' '}`))
                if (click == 3){
                    $("#getHelp").attr("disabled", true);
                }
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

