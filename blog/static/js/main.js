$("[href='#article']").click(function(){
    $.post('http://127.0.0.1:5000/api/page/get_page_list',
    {},
    function(ret){
        $("#article").text("");
        var insert = '<ul class="page">'
        $.each(ret.data, function(k, v){
            var date = new Date(v.date_create);
            date = date.getFullYear() + '-' +
                (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-' +
                date.getDate();
            date = "<span class='date'>" + date + '</span>'
            var page ="<a>" + v.title + "</a>"
            var li = '<li class="page" id="' + v.id + '">' + date + page + "</li>"
            insert = insert + li
        })
        insert = insert + "</ul>"

        $("#article").append(insert)
    })
    $("#article").text("test")
})
