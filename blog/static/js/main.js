$("[href='#article']").click(function(){
    $.post('http://127.0.0.1:5000/api/page/get_page_list',
    {},
    function(ret){
        $("#article").text("");
        $.each(ret.data, function(k, v){
            $("#article").append("<div>" + v.id + ':' + v.title +"</div>")
        })
    })
    $("#article").text("test")
})
