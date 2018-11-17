$(document).ready(function(){
    $('.menu').click(function(){
        $('nav ul').toggleClass('active')
    })
})

$(document).ready(function(){
    $('.icon-bici').click(function(){
        $('#arri_cont').toggleClass('none')
    })
})

$(document).ready(function(){
    $('.btn_cancelar').click(function(){
        $('#arri_cont').removeClass('none')
    })
})