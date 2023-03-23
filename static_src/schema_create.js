$(function ($){
    $('#schema_create').submit(function (e){
        e.preventDefault()
//        console.log(this, 'error')
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                console.log('ok - ', response)
            },
            error: function (response) {
                console.log('err - ', response)
            }
    })
})
})
