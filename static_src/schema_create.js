$(function ($){
    $('#schema_create').submit(function (e){
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            complete: function (response) {
            if (response) {

          }
            console.log(response, 'SUCcESS')
                added_row = '<tr>'
                    + '<th scope="col">' + response['responseJSON']['order'] +  '</th>'
                    + '<td>' + response['responseJSON']['file_name'] +  '</td>'
                    + '<td>' + 'Ready' +  '</td>'
                    + '<td>' + response['responseJSON']['link_start'] + response['responseJSON']['link_end'] + '</td>'
                    + '</tr>'
                $('#flex-table').append(added_row)
            },
            error: function (response) {
                console.log(response, 'SUCcESS');
            }
    })
})
})
