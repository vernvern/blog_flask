var address = 'http://45.76.100.76'

// artile - 事件 - 文章标题列表
$("[href='#article']").click(function(){
    $.post(address +'/api/page/get_page_list',
    {},
    function(ret){
        $("#article").text("");
        var insert = '<ul class="page">'
        var pages = ret.data
        for(i=0; i<pages.length; i++){
            var page = pages[i];
            var date = new Date(page.date_created);
            date = date.getFullYear() + '-' +
                (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-' +
                date.getDate();
            date = "<span class='date'>" + date + '</span>'
            var page ='<a class="page" href="javascraddresst:void(0);" onclick="show_page(id)" id=' + page.id + '>' + page.title + "</a>"
            var li = '<li class="page' + '">' + date + page + "</li>"
            insert = insert + li
        }
        insert = insert + "</ul>"

        $("#article").append(insert)
    })
});


// Article － 根据分类获取文章标题列表
$(".sort").click(function(){
    $.post(address +'/api/page/get_page_list',
    {
        sort=this.text();
    },
    function(ret){
        $("#article").text("");
        var insert = '<ul class="page">'
        var pages = ret.data
        for(i=0; i<pages.length; i++){
            var page = pages[i];
            var date = new Date(page.date_created);
            date = date.getFullYear() + '-' +
                (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-' +
                date.getDate();
            date = "<span class='date'>" + date + '</span>'
            var page ='<a class="page" href="javascraddresst:void(0);" onclick="show_page(id)" id=' + page.id + '>' + page.title + "</a>"
            var li = '<li class="page' + '">' + date + page + "</li>"
            insert = insert + li
        }
        insert = insert + "</ul>"

        $("#article").append(insert)
    })
});



// index/artice - 事件 - 文章详情
function show_page(id){
    $.post(address + '/api/page/get_page_detail',
    {
        id: id
    },
    function(ret)
    {
        var title = ret.data.title;
        var body = ret.data.body;
        var date_created = ret.data.date_created;
        var date_modified = ret.data.date_modified;
        var tags = ret.data.tags;
        var sort = ret.data.sort;

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
function get_simple_page_list(index=1, size=20){
    var accordion = "accordion" + index;
    $.post(address + '/api/page/get_simple_page_list', {
        index: index,
        size: size,
    },
    function(ret){
        var div_list = "";  // 文章简要
        pages = ret.data;
        for(var i=0;i<pages.length;i++){
            var div = '<div class="panel panel-default">' +
                      '<div class="panel-heading" role="tab" id="heading_' + pages[i].id + '">' +
                      '<h4 class="panel-title">' +
                      '<a role="button" data-toggle="collapse" data-parent="#'+ accordion + '" href="#' + pages[i].id + '" aria-expanded="' + (i==0?'true':'false') + '" aria-controls="' + pages[i].id + '" ' + (i==0?'':'class="collapsed"') + '>' +
                      pages[i].title +
                      '</a>' +
                      '</h4>' +
                      '</div>' +
                      '<div id=' + pages[i].id + ' class="panel-collapse collapse ' + (i==0?'in':'') + '" role="tabpanel" aria-labelledby="heading_' + pages[i].id + '">' +
                      '<div class="panel-body">' +
                      pages[i].body +
                      '<center>.</center>' +
                      '<center>.</center>' +
                      '<center>.</center></br>' +
                      '<center><a class="show_detail" href="javascraddresst:void(0);" onclick="show_page(id)" id="' + pages[i].id + '">查看全文</a></center>' +
                      '</div>' +
                      '</div>' +
                      '</div>';
            div_list = div_list + div;
        };
        var more = '<div class="panel-group" id="accordion' + (index - 0 + 1) + '" role="tablist" aria-multiselectable="true"></div>';

        $("#" + accordion).append(div_list);
        $("#" + accordion).after(more);

        $("#show_more_article").attr("value", index - 0 + 1);
    })}

// index - 事件 - 加载完页面触发
$(function(){
    get_simple_page_list(1, 20);
    get_sort_list();

    // 3d词云
    innit();
    animate();
})

// index - 事件 - 查看更多
$("#show_more_article").click(function(){
    var index = $("#show_more_article").attr("value");
    get_simple_page_list(index, 20);

});


// sort - 获取sort
function get_sort_list(){
    $.get(address +'/api/sort/get_sort_list',
    {},
    function(ret){
        var sorts = ret.data
        var _sorts = '<div class="row">';
        for(i=0; i<sorts.length; i++){
            sort = '<div class="col-md-5 col-md-offset-1 sort">' + sorts[i] + "</div>";
 sort            _sorts += sort;
        }
        _sorts += '</div>';
        $("#sort").prepend(_sorts);
    })
};



// 以下代码摘自whxaxes的https://github.com/whxaxes/canvas-test/blob/master/src/3D-demo/3Dtag.html
var tagEle = "querySelectorAll" in document ? document.querySelectorAll(".tag") : getClass("tag"),
    paper = "querySelectorAll" in document ? document.querySelector(".tagBall") : getClass("tagBall")[0];
RADIUS = 80,
    fallLength = 500,
    tags = [],
    angleX = Math.PI / 500,
    angleY = Math.PI / 500,
    CX = paper.offsetWidth / 2,
    CY = paper.offsetHeight / 2,
    EX = paper.offsetLeft + document.body.scrollLeft + document.documentElement.scrollLeft,
    EY = paper.offsetTop + document.body.scrollTop + document.documentElement.scrollTop;
function getClass(className) {
    var ele = document.getElementsByTagName("*");
    var classEle = [];
    for (var i = 0; i < ele.length; i++) {
        var cn = ele[i].className;
        if (cn === className) {
            classEle.push(ele[i]);
        }
    }
    return classEle;
}
function innit() {
    for (var i = 0; i < tagEle.length; i++) {
        var a, b;
        var k = -1 + (2 * (i + 1) - 1) / tagEle.length;
        var a = Math.acos(k);
        var b = a * Math.sqrt(tagEle.length * Math.PI);
        var x = RADIUS * Math.sin(a) * Math.cos(b);
        var y = RADIUS * Math.sin(a) * Math.sin(b);
        var z = RADIUS * Math.cos(a);
        var t = new tag(tagEle[i], x, y, z);
        var color = parseInt(Math.random() * 255);
        tagEle[i].style.color = "rgb(" + color + "," + color + "," + color + ")";
        tags.push(t);
        t.move();
    }
}
Array.prototype.forEach = function(callback) {
    for (var i = 0; i < this.length; i++) {
        callback.call(this[i]);
    }
}
function animate() {
    rotateX();
    rotateY();
    tags.forEach(function() {
        this.move();
    });
    requestAnimationFrame(animate);
}
if ("addEventListener" in window) {
    paper.addEventListener("mousemove", function(event) {
        var x = event.clientX - EX - CX;
        var y = event.clientY - EY - CY;
        angleY = x * 0.0001;
        angleX = y * 0.0001;
    });
}
else {
    paper.attachEvent("onmousemove", function(event) {
        var x = event.clientX - EX - CX;
        var y = event.clientY - EY - CY;
        angleY = x * 0.0001;
        angleX = y * 0.0001;
    });
}
function rotateX() {
    var cos = Math.cos(angleX);
    var sin = Math.sin(angleX);
    tags.forEach(function() {
        var y1 = this.y * cos - this.z * sin;
        var z1 = this.z * cos + this.y * sin;
        this.y = y1;
        this.z = z1;
    })
}
function rotateY() {
    var cos = Math.cos(angleY);
    var sin = Math.sin(angleY);
    tags.forEach(function() {
        var x1 = this.x * cos - this.z * sin;
        var z1 = this.z * cos + this.x * sin;
        this.x = x1;
        this.z = z1;
    })
}
var tag = function(ele, x, y, z) {
    this.ele = ele;
    this.x = x;
    this.y = y;
    this.z = z;
}
tag.prototype = {
    move: function() {
        var scale = fallLength / (fallLength - this.z);
        var alpha = (this.z + RADIUS) / (2 * RADIUS);
        var left = this.x + CX - this.ele.offsetWidth / 2 + "px";
        var top = this.y + CY - this.ele.offsetHeight / 2 + "px";
        var transform = 'translate(' + left + ', ' + top + ') scale(' + scale + ')';
        this.ele.style.opacity = alpha + 0.5;
        this.ele.style.zIndex = parseInt(scale * 100);
        this.ele.style.transform = transform;
        this.ele.style.webkitTransform = transform;
    }
}
