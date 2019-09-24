from flask import Flask, render_template, url_for, redirect, request, flash, session, g, abort
from myapp import app
from model import article_tags, Category, Post, Tag, Comment, pageby, db
from werkzeug import secure_filename
from random import shuffle
from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
import os
import json
import time
from datetime import datetime
from form import CommentForm

from werkzeug.contrib.atom import AtomFeed
# from flask.ext.cache import Cache


# cache = Cache(app, config={'CACHE_TYPE': 'simple'})
# app.config.from_object('config')
# per_page = app.config['PER_PAGE']


class PostFeed(AtomFeed):

    def add_post(self, post):

        self.add(post.post_title,
                 '',
                 content_type="html",
                 author=u'dan',
                 url=post.url,
                 updated=datetime.now(),
                 published=post.post_create_time)


class _DeHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text


def html2textile(html):
    return dehtml(html)

app.jinja_env.filters['html2textile'] = html2textile


def is_chinese(text):
    if text:
        for uchar in text:
            if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
                return True
    return False



