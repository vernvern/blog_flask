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
            var page ='<a class="page" href="javascript:void(0);" onclick="show_page(id)"' + ' id="' + v.id + '">' + v.title + "</a>"
            var li = '<li class="page' + '">' + date + page + "</li>"
            insert = insert + li
        })
        insert = insert + "</ul>"

        $("#article").append(insert)
    })
});

function show_page(id){
    $.post('http://127.0.0.1:5000/api/page/get_page_detail',
    {
        id: id
    },
    function(ret)
    {
        $(".modal-body").text("");
        var title = ret.data.title;
        var body = ret.data.body;
        var date_create = ret.data.date_create;
        var date_modify = ret.data.date_modify;
        $(".modal-body").append(title + ":" + body)
    });

    $('#myModal').modal('show');
}

