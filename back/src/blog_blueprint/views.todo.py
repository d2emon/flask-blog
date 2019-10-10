from flask import current_app, render_template, url_for, redirect, request, flash, session, abort
from app.model import Category, Post, Tag, Comment, pageby, db
from werkzeug import secure_filename
from random import shuffle
import json
import time
from form import CommentForm


@current_app.route('/')
@current_app.route('/page/<int:pageid>')
# @cache.cached(timeout=300)
def index(pageid=1):
    categorys = Category.query.getall()

    p = Post.query.getpost_perpage(pageid, per_page)
    hot = Post.query.hottest()[:20]
    new = Post.query.newpost()[:20]

    tag = Tag.query.getall()
    shuffle(tag)
    tag = tag[:20]

    comments = Comment.query.newcomment()[:20]
    articles = p.items
    if not p.total:
        pagination = [0]
    elif p.total % per_page:
        pagination = range(1, p.total / per_page + 2)
    else:
        pagination = range(1, p.total / per_page + 1)

    return render_template('/index.html',
                           categorys=categorys,
                           articles=articles,
                           hotarticles=hot,
                           newpost=new,
                           tags=tag,
                           comments=comments,
                           pageid=pageid,
                           pagination=pagination[pageid - 1:pageid + 10],
                           last_page=pagination[-1],
                           nav_current="index"
                           )


@current_app.route('/about')
# @cache.cached(timeout=300)
def about():
    categorys = Category.query.getall()
    hot = Post.query.hottest()[:20]
    new = Post.query.newpost()[:20]

    tag = Tag.query.getall()
    shuffle(tag)
    tag = tag[:20]

    comments = Comment.query.newcomment()[:20]

    return render_template('/about.html',
                           categorys=categorys,
                           hotarticles=hot,
                           newpost=new,
                           tags=tag,
                           comments=comments)


@app.route('/category/<int:cateid>')
@app.route('/category/<int:cateid>/page/<int:pageid>')
# @cache.cached(timeout=300)
def category(cateid=1, pageid=1):
    categorys = Category.query.getall()
    hot = Post.query.hottest()[:20]
    new = Post.query.newpost()[:20]
    tag = Tag.query.getall()
    shuffle(tag)
    tag = tag[:20]
    comments = Comment.query.newcomment()[:20]

    cate = Category.query.get_or_404(cateid)

    p = pageby(cate.posts, pageid, per_page, Post.post_create_time.desc())

    articles = p.items
    if not p.total:
        pagination = [0]
    elif p.total % per_page:
        pagination = range(1, p.total / per_page + 2)
    else:
        pagination = range(1, p.total / per_page + 1)

    return render_template('/category.html',
                           id=cateid,
                           cate=cate,
                           categorys=categorys,
                           articles=articles,
                           hotarticles=hot,
                           newpost=new,
                           tags=tag,
                           comments=comments,
                           pageid=pageid,
                           pagination=pagination[pageid - 1:pageid + 10],
                           last_page=pagination[-1]
                           )


@current_app.route('/tag/<int:tagid>')
@current_app.route('/tag/<int:tagid>/page/<int:pageid>')
# @cache.cached(timeout=300)
def tag(tagid=1, pageid=1):
    categorys = Category.query.getall()
    hot = Post.query.hottest()[:20]
    new = Post.query.newpost()[:20]
    tag = Tag.query.getall()
    shuffle(tag)
    tag = tag[:20]
    comments = Comment.query.newcomment()[:20]

    tagall = Tag.query.get_or_404(tagid)
    name = tagall.name
    p = Post.query.search_tag(name)
    p = pageby(p, pageid, per_page, Post.post_create_time.desc())

    articles = p.items
    if not p.total:
        pagination = [0]
    elif p.total % per_page:
        pagination = range(1, p.total / per_page + 2)
    else:
        pagination = range(1, p.total / per_page + 1)

    return render_template('/tag.html',
                           id=tagid,
                           tagall=tagall,
                           categorys=categorys,
                           articles=articles,
                           hotarticles=hot,
                           newpost=new,
                           tags=tag,
                           comments=comments,
                           pageid=pageid,
                           pagination=pagination[pageid - 1:pageid + 10],
                           last_page=pagination[-1]
                           )


@current_app.route('/search')
@current_app.route('/search/page/<int:pageid>')
# @cache.cached(timeout=240)
def search(pageid=1):

    categorys = Category.query.getall()
    hot = Post.query.hottest()[:20]
    new = Post.query.newpost()[:20]
    tag = Tag.query.getall()
    shuffle(tag)
    tag = tag[:20]
    comments = Comment.query.newcomment()[:20]

    searchword = request.args.get('s', '')
    if not searchword:
        return redirect(url_for('error_404'))

    searchresult = Post.query.search(searchword)

    p = pageby(searchresult, pageid, per_page, Post.post_create_time.desc())

    articles = p.items
    if not p.total:
        pagination = [0]
    elif p.total % per_page:
        pagination = range(1, p.total / per_page + 2)
    else:
        pagination = range(1, p.total / per_page + 1)

    return render_template('/search.html',
                           key=searchword,
                           categorys=categorys,
                           articles=articles,
                           hotarticles=hot,
                           newpost=new,
                           tags=tag,
                           comments=comments,
                           pageid=pageid,
                           pagination=pagination[pageid - 1:pageid + 10],
                           last_page=pagination[-1]
                           )


@app.route('/article/<int:postid>')
# @cache.cached(timeout=300)
def article(postid=5):
    categorys = Category.query.getall()
    hot = Post.query.hottest()[:20]
    new = Post.query.newpost()[:20]
    tag = Tag.query.getall()
    shuffle(tag)
    tag = tag[:20]
    comments = Comment.query.newcomment()[:20]
    articles = Post.query.getall()
    shuffle(articles)
    articles = articles[:5]

    post = Post.query.get_or_404(postid)
    form = CommentForm()
    postcoments = post.comments.all()
    post.view_num += 1
    db.session.commit()
    return render_template('/post.html',
                           post=post,
                           articles=articles,
                           categorys=categorys,
                           hotarticles=hot,
                           newpost=new,
                           tags=tag,
                           comments=comments,
                           postcoments=postcoments,
                           form=form
                           )


@app.route('/<postname>.html')
# @cache.cached(timeout=300)
def article_byname(postname):
    categorys = Category.query.getall()
    hot = Post.query.hottest()[:20]
    new = Post.query.newpost()[:20]
    tag = Tag.query.getall()
    shuffle(tag)
    tag = tag[:20]
    comments = Comment.query.getall()[:20]
    articles = Post.query.getall()
    shuffle(articles)
    articles = articles[:5]

    post = Post.query.getpost_byname(postname)

    if not post:
        return redirect(url_for('error_404'))
    form = CommentForm()
    postcoments = post.comments.all()
    post.view_num += 1
    db.session.commit()

    return render_template('/post.html',
                           post=post,
                           articles=articles,
                           categorys=categorys,
                           hotarticles=hot,
                           newpost=new,
                           tags=tag,
                           comments=comments,
                           postcoments=postcoments,
                           form=form
                           )


@app.route('/addcomment', methods=['POST'])
def addcomment():
    form = CommentForm()
    error = 'Sorry, Post Comments Error!'

    if form.validate_on_submit():
        author_ip = request.environ.get('HTTP_X_FORWARDED_FOR') or '127.0.0.1'
        comment = Comment(author_ip=author_ip)
        form.populate_obj(comment)
        db.session.add(comment)
        post = Post.query.getpost_id(comment.post_id)
        post.comment_count += 1
        db.session.commit()
        return redirect(url_for('article', postid=comment.post_id))

    return render_template('/error.html', content=error)


@current_app.route('/error')
def error(content='404'):
    return render_template('/error.html', content=content)


@current_app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('newpost'))
    return render_template('auth/login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))


@app.route('/newpost')
def newpost():
    categories = Category.query.getall()
    return render_template('/newpost.html', categories=categories)


@app.route('/addpost', methods=['POST'])
def addpost():
    if not session.get('logged_in'):
        abort(401)
    elif request.method == 'POST':
        tagtemp = []
        taglist = request.form['tags'].split(',')
        for i in taglist:
            tagtemp.append(Tag(name=i))

        db.session.add(Post(tags=tagtemp, post_content=request.form['content'], post_title=request.form[
                       'title'], category_id=request.form['category'], post_name=request.form['postname'], tags_name=request.form['tags']))
        db.session.commit()

    return redirect(url_for('newpost'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('imgFile', None)

        if file and allowed_file(file.filename):
            filename = str(int(time.time())) + '_' + \
                secure_filename(file.filename)
            file.save(app.config['UPLOAD_FOLDER'] + filename)
            data = {'error': 0, 'url': app.config['UPLOAD_FOLDER'] + filename}
            return json.dumps(data)
    return 'FAIL!'


@app.route('/epost', methods=['GET'])
def epost():
    num = request.args.get('post', '')
    if num:
        p = Post.query.get_or_404(num)
        return render_template('/editpost.html', p=p)
    return redirect(url_for('error_404'))


@current_app.route('/apost', methods=['POST'])
def apost():
    if not session.get('logged_in'):
        abort(401)
    elif request.method == 'POST':
        p = Post.query.getpost_id(request.form['num'])
        p.post_title = request.form['title']
        p.post_name = request.form['postname']
        p.post_content = request.form['content']
        db.session.commit()
    return redirect(url_for('newpost'))


@current_app.route('/rss_lastnews')
@cache.cached(timeout=86400)
def rss_last():
    feed = PostFeed("pythonpub - lastnews",
                    feed_url=request.url,
                    url=request.url_root)
    new = Post.query.newpost().limit(15)
    for post in new:
        feed.add_post(post)

    return feed.get_response()

