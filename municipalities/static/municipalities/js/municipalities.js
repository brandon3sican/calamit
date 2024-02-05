$(document).ready(function(){
    $('#store').on('click', function(){
        $municipality_name = $('#municipality_name').val();
        $description = $('#description').val();
        $contact_person = $('#contact_person').val();
        $contact_number = $('#contact_number').val();
        
        
        if($municipality_name == "" || $description == "" || $contact_person == "" || $contact_number == ""){
            alert("Please complete the required field");
        }else{
            $.ajax({
                url: 'store/',
                type: 'POST',
                data: $('#addMunicipalityForm').serialize(),
                dataType: 'json',
                /*{
                    municipality_name: $municipality_name,
                    description: $description,
                    contact_person: $contact_person,
                    contact_number: $contact_number,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },*/
                success: function(){
                    /*Read();
                    $('#municipality_name').val('');
                    $('#description').val('');
                    $('#contact_person').val('');
                    $('#contact_number').val('');
                    alert("New Member Successfully Added");*/
                }
            });
        }
    });
});

function Read(){
    $.ajax({
        url: '{% url "municipalities-read" %}',
        type: 'POST',
        async: false,
        data:{
            res: 1,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $('#result').html(response);
        }
    });
}