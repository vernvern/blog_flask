// artile - 事件 - 文章标题列表
$("[href='#article']").click(function(){
    $.post('http://127.0.0.1:5000/api/page/get_page_list',
    {},
    function(ret){
        $("#article").text("");
        var insert = '<ul class="page">'
        var pages = ret.data
        for(i=0; i<pages.length; i++){
            var page = pages[i];
            var date = new Date(page.date_modified);
            date = date.getFullYear() + '-' +
                (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-' +
                date.getDate();
            date = "<span class='date'>" + date + '</span>'
            var page ='<a class="page" href="javascript:void(0);" onclick="show_page(id)">' + page.title + "</a>"
            var li = '<li class="page' + '">' + date + page + "</li>"
            insert = insert + li
        }
        insert = insert + "</ul>"

        $("#article").append(insert)
    })
});


// index/artice - 事件 - 文章详情
function show_page(id){
    $.post('http://127.0.0.1:5000/api/page/get_page_detail',
    {
        id: id
    },
    function(ret)
    {
        var title = ret.data.title;
        var body = ret.data.body;
        var date_create = ret.data.date_create;
        var date_modify = ret.data.date_modify;

        // title
        $(".modal-title").text("");
        $(".modal-title").append(title);

        // body
        $(".modal-body").text("");
        $(".modal-body").append(body)
    });

    $('#myModal').modal('show');
}


// index - func - 文章简要列表
function get_simple_page_list(index=1, value=20){
    var accordion = "accordion" + index;
    $.post('http://127.0.0.1:5000/api/page/get_simple_page_list', {
        index: index,
        value: value
    },
    function(ret){
        var div_list = "";  // 文章简要
        pages = ret.data;
        for(var i=0;i<pages.length;i++){
            var div = '<div class="panel panel-default">' +
                      '<div class="panel-heading panel_heading"' +
                      ' role="tab" id="' + pages[i].id + '">' +
                      '<h4 class="panel-title">' +
                      '<a role="button" data-toggle="collapse" ' +
                      'data-parent="' + accordion + '" href="#collapse' +
                      pages[i].id +
                      '" aria-expanded=' + (i == 0 ? '"true"' : '"false"') +
                      ' aria-controls="collapse' + pages[i].id + '">' +
                      pages[i].title + '</a>' +
                      '</h4></div>' +
                      '<div id="collapse' + pages[i].id + '" ' +
                      'class="panel-collapse collapse ' +
                      (index==1 ? (i==0 ? 'in"' : '') : '') +
                      ' role="tabpanel" ' +
                      'aria-labelledby="heading' + pages[i].id + '">' +
                      '<div class="panel-body">' +
                      pages[i].body + '</br></br>' +
                      '<center>.</center>' +
                      '<center>.</center>' +
                      '<center>.</center></br>' +
                      '<center><a class="show_detail" href="javascript:void(0);" onclick="show_page(id)" id="' +
                      pages[i].id + '">查看全文</a></center>' +
                      '</div></div></div>'
            div_list = div_list + div;
        };
        var more = '<div class="panel-group" id="accordion' + (index - 0 + 1) + '" role="tablist" aria-multiselectable="true"></div>';

        $("#" + accordion).append(div_list);
        $("#" + accordion).after(more);

        $("#show_more_article").attr("value", index - 0 + 1);
    })}

// index - 事件 - 加载完页面触发
$(function(){
    get_simple_page_list(1, 20)
})

// index - 事件 - 查看更多
$("#show_more_article").click(function(){
    var index = $("#show_more_article").attr("value");
    get_simple_page_list(index, 20);

});
