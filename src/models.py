import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
import enum


Base = declarative_base()


class User (Base):
    __tablename__ = 'user'

    #columns
    id = Column (Integer, primary_key=True)
    password = Column(String(256))
    user_name = Column (String(20), nullable=False)
    nick_name = Column (String(20), nullable=False)

    #relationships
    post= relationship ('Post', backref='user')
    comments = relationship ('Comment', backref='user')
    comment_likes = relationship ('CommentLike', backref='user')
    post_likes = relationship ('PostLike', backref='user')

    def to_dict(self):
       return {}


class Follower (Base):
    __tablename__ = 'follower'

    #columns
    user_from_id = Column (Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column (Integer, ForeignKey('user.id'), primary_key=True)

    #relationships
    user = relationship ('User', backref='user')


#define Enum
class Media_enum(enum.Enum):
    image = "image"
    video = "video"


class Media (Base):
    __tablename__ = 'media'
    id = Column (Integer, primary_key=True)
    type = Column (Enum(Media_enum))
    url = Column (String)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


    #relationships
    user = relationship ('User', backref='user')
    post = relationship ('Post', backref='post')


class Post (Base):
    __tablename__ = 'post'

    #columns
    id = Column (Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'))
    image_url = Column (String(), nullable=False)
    date_published = Column (DateTime(), nullable=False)
    content = Column (String (2200))

    #relationships
    likes = relationship ('PostLike', backref='post')
    comments = relationship ('Comment', backref='post')


class Comment (Base):
    __tablename__ = 'comment'

    #columns
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey ('post.id'))
    user_id = Column (Integer, ForeignKey ('user.id'))
    content = Column (String (300), nullable=False)
    date_publisher = Column (DateTime(), nullable=False)

    #relationships
    likes = relationship ('CommentLike', backref='comment')


class PostLike (Base):
    __tablename__ = 'post_like'

    #columns
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey ('post.id'))
    user_id = Column (Integer, ForeignKey ('user.id'))


class CommentLike (Base):
    __tablename__ = 'comment_like'

    #columns
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey ('post.id'))
    user_id = Column (Integer, ForeignKey ('user.id'))
    comment_id = Column (Integer, ForeignKey ('comment.id'))

    #relationships
    post = relationship ('Post', backref='post')
    user = relationship ('User', backref='user')
    comment = relationship ('Comment', backref='comment')


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
