from blog import db

from .base import BaseModel


class Page(db.Model, BaseModel):
    title = db.Column(db.String(100))
    body = db.Column(db.Text, default='')
    sort_id = db.Column(db.Integer, db.ForeignKey('sort.id'), nullable=True)
    sort = db.relationship('Sort')
    is_show = db.Column(db.Boolean, default=True)

    def __init__(self, title, body):
        self.title = title
        self.body = body
        super(Page, self).__init__()


class Tag(db.Model, BaseModel):
    mark = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(100))

    def __init__(self, mark, description=None):
        self.mark = mark
        self.description = description
        super(Page, self).__init__()


class Sort(db.Model, BaseModel):
    mark = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(100), default='')

    def __init__(self, mark, description=None):
        self.mark = mark
        self.description = description
        super(Sort, self).__init__()


class PageAndTag(db.Model, BaseModel):
    __tablename__ = 'page_and_tag'
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'))
    page = db.relationship('Page')
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    tag = db.relationship('Tag')

    def __init__(self, page_id, tag_id):
        self.page_id = page_id
        self.tag_id = tag_id
        super(PageAndTag, self).__init__()
