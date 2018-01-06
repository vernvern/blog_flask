from blog import db

from .base import BaseModel


class Page(db.Model, BaseModel):
    title = db.Column(db.String(100), unique=True)
    body = db.Column(db.Text, default='')
    sort_id = db.Column(db.Integer, db.ForeignKey('sort.id'), nullable=True)
    sort = db.relationship('Sort')
    is_show = db.Column(db.Boolean, default=True)

    def __str__(self):
        return '{0}: {1}'.format(self.title, self.body[:20])


class Tag(db.Model, BaseModel):
    mark = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(100))


class Sort(db.Model, BaseModel):
    mark = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(100), default='')


class PageAndTag(db.Model, BaseModel):
    __tablename__ = 'page_and_tag'
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'))
    page = db.relationship('Page')
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    tag = db.relationship('Tag')
