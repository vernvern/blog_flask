from blog.toolkit.route.route import http


@http('/index')
def index():
    return 'hello world'


@http('/test1', methods=['POST'])
def test1():
    return 'hello world1'


@http()
def test2():
    return {'data': []}
