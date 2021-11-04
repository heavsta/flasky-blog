from app import db
from app.models import Category
from app.categories.forms import CategoryForm
from flask import abort, Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

categories = Blueprint('categories', __name__)


@categories.route('/category/new', methods=['GET', 'POST'])
@login_required
def category_new():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        flash(f'Category "{form.name.data}" successfully created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create_category.html', title='Create a new Category', form=form)


@categories.route('/category/list')
@login_required
def category_list():
    categories = Category.query.all()
    return render_template('list_category.html', title='Categories' ,categories=categories)


@categories.route('/category/update/<int:id>', methods=['GET', 'POST'])
@login_required
def category_update(id):
    if current_user.role != 'admin':
        abort(403)
    category = Category.query.get_or_404(id)
    form = CategoryForm()
    if form.validate_on_submit():
        category.name = form.name.data
        db.session.commit()
        flash('Category successfully updated!', 'success')
        return redirect(url_for('categories.category_list'))
    elif request.method == 'GET':
        form.name.data = category.name
    return render_template('create_category.html', title='Update Category', legend='Update your Category', form=form, category=category)


@categories.route('/category/delete/<int:id>', methods=['POST'])
@login_required
def category_delete(id):
    if current_user.role != 'admin':
        abort(403)
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash('Category successfully deleted!', 'success')
    return redirect(url_for('categories.category_list'))