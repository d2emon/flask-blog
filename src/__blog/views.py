from flask import g, request, render_template, redirect, flash, url_for
from flask_login import login_required, current_user, login_user, logout_user
from app import app, db, login_manager
from .models import Category, Tag, Post, User
from .forms import PostForm, EForm


import random


def page():
    page_str = request.args.get('page_id')
    try:
        page = int(page_str)
    except (ValueError, TypeError):
        page = 1
    return page


@login_manager.user_loader
def load_user(user_id):
    return User()


@app.before_request
def load_sidebar():
    g.user = current_user

    # categories = Category.query.getall()
    g.categories = Category.query.all()

    # hot = Post.query.hottest()[:20]
    g.hotarticles = Post.query.all()[:20]
    # new = Post.query.newpost()[:20]
    g.newpost = Post.query.all()[:20]

    # tag = Tag.query.getall()
    tag = Tag.query.all()
    random.shuffle(tag)
    g.tags = tag[:20]

    # comments = Comment.query.newcomment()[:20]


@app.route('/')
@app.route('/page/<int:page_id>')
def index(page_id=1):
    # post = Post.query.getpost_perpage(page_id, app.config.PER_PAGE)
    post = Post.query  # filter_by(id=page_id, app.config.PER_PAGE)
    articles = post.paginate(page(), app.config.get('RECORDS_ON_PAGE'))

    return render_template(
        '/index/index.html',
        articles=articles,
        nav_current="index"
    )


@app.route('/about')
def about():
    return render_template(
        '/index/about.html',
    )


@app.route('/category/<int:cat_id>')
@app.route('/category/<int:cat_id>/page/<int:page_id>')
def category(cat_id, page_id=1):
    cat = Category.query.get_or_404(cat_id)

    # p = pageby(cat.posts, page_id, per_page, Post.created_at.desc())
    articles = cat.posts.paginate(page(), app.config.get('RECORDS_ON_PAGE'))

    return render_template(
        '/index/category.html',
        id=cat_id,
        cat=cat,
        articles=articles,
    )


@app.route('/tag/<int:tag_id>')
@app.route('/tag/<int:tag_id>/page/<int:page_id>')
def tag(tag_id, page_id=1):
    tagall = Tag.query.get_or_404(tag_id)
    name = tagall.name
    # p = Post.query.search_tag(name)
    p = Post.query
    articles = p.paginate(page(), app.config.get('RECORDS_ON_PAGE'))

    return render_template(
        '/index/tag.html',
        id=tag_id,
        tagall=tagall,
        articles=articles,
    )


@app.route('/article/<int:post_id>')
def article(post_id):
    # articles = Post.query.getall()
    articles = Post.query.all()
    random.shuffle(articles)
    articles = articles[:5]

    post = Post.query.get_or_404(post_id)
    # form = CommentForm()
    # postcoments = post.comments.all()
    post.views += 1

    db.session.add(post)
    db.session.commit()

    return render_template(
        '/index/post.html',
        post=post,
        articles=articles,
        # postcoments=postcoments,
        # form=form
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        user = User()
        logged = user.login(
            request.form['username'],
            request.form['password'],
        )
        if logged:
            login_user(user)
            flash('You were logged in')
            return redirect(url_for('addpost'))
    return render_template('/index/login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('index'))


@app.route('/addpost', methods=['GET', 'POST'])
@login_required
def addpost():
    if request.method == 'POST':
        tagtemp = []
        taglist = request.form['tags'].split(',')
        for i in taglist:
            tagtemp.append(Tag(name=i))

        post = Post(
            # name=request.form['postname'],
            title=request.form['title'],
            content=request.form['content'],
            category_id=request.form['category'],
            tags=tagtemp,
            tags_name=request.form['tags']
        )
        db.session.add(post)
        db.session.commit()

    return render_template(
        '/index/newpost.html',
        post_form=PostForm(),
        e_form=EForm(),
    )
