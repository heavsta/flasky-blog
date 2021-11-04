from app import db
from app.articles.forms import CommentForm, PostForm
from app.articles.utils import save_img_raw
from app.models import Article, Category, Comment
from datetime import datetime
from flask import abort, Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

articles = Blueprint('articles', __name__)


@articles.route('/post/new', methods=['GET', 'POST'])
@login_required
def post_new():
    categories = Category.query.order_by('name').all()
    form = PostForm()
    # inserting in choices the list of tuples for the SelectField
    form.category.choices = [(category.id, category.name) for category in categories]
    if form.validate_on_submit():
        picture = save_img_raw(form.picture.data)
        post = Article(title=form.title.data, category_id=form.category.data, content=form.content.data, author_id=current_user.id, picture=picture)
        db.session.add(post)
        db.session.commit()
        flash('Your article has been created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create_post.html', title='Create a new Article', legend='Post a new Article', form=form)


@articles.route('/post/show/<int:id>')
def post_show(id):
    post = Article.query.get_or_404(id)
    form = CommentForm()
    return render_template('post.html', title=post.title, post=post, form=form, now=datetime.utcnow())


@articles.route('/post/list')
@login_required
def post_list():
    posts = current_user.articles
    return render_template('list_post.html', title=current_user.username + '\'s Articles' ,posts=posts)


@articles.route('/post/update/<int:id>', methods=['GET', 'POST'])
@login_required
def post_update(id):
    post = Article.query.get_or_404(id)
    if current_user.id != post.author_id:
        abort(403)
    form = PostForm(coerce=int)
    categories = Category.query.order_by('name').all()
    form.category.choices = [(category.id, category.name) for category in categories]
    if form.validate_on_submit():
        post.title = form.title.data
        post.category_id = form.category.data
        post.content = form.content.data
        if form.picture.data:
            post.picture = save_img_raw(form.picture.data)
        db.session.commit()
        flash('Article successfully updated!', 'success')
        return redirect(url_for('articles.post_show', id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.category.data = post.category_id
        form.content.data = post.content
        form.picture.data = post.picture
    return render_template('create_post.html', title='Update Post', legend='Update your Article', form=form, post=post)


@articles.route('/post/delete/<int:id>', methods=['POST'])
@login_required
def post_delete(id):
    post = Article.query.get_or_404(id)
    if current_user.id != post.author_id:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Article successfully deleted!', 'success')
    return redirect(url_for('articles.post_list'))


@articles.route('/comment/new/<int:post_id>', methods=['POST'])
@login_required
def comment_new(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, author_id=current_user.id, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment was successfully posted!', 'success')
        return redirect(url_for('articles.post_show', id=post_id))
    else:
        flash('Something went wrong...', 'danger')
        return redirect(url_for('articles.post_show', id=post_id))
