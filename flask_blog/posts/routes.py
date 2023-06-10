from flask import Flask, Blueprint, render_template, url_for, redirect, request, flash, abort
from flask_login import login_required, current_user
from posts.forms import PostForm, UpdatePostForm
from posts.models import Post
from auth.models import User
from flask_modals import render_template_modal


posts = Blueprint('posts', __name__, static_folder='static')


@posts.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    """This route create new post"""
    form = PostForm(request.form)
    if request.method == 'POST' and form.validate():
        post = Post(title=form.title.data,
                    description=form.description.data, user_id=current_user.id)
        post.insert()
        flash("New post successfully added", "success")
        return redirect(url_for('index'))
    elif request.method == 'GET':
        ...
    return render_template('create_post.html', title='New Post', form=form)


@posts.route('/show_post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    form = UpdatePostForm(request.form)
    if request.method == 'GET':
        post = Post.query.filter_by(id=post_id).join(User).first()
    elif request.method == 'POST' and form.validate():
        post = Post.query.filter_by(id=post_id).first()
        post.title = form.title.data
        post.description = form['description'].data
        post.update()
        flash("Post successfully updated", "success")
        return redirect(url_for('index'))
    return render_template_modal('show_post.html', title='Show Post', post=post, form=form)


@posts.route('/post/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    if request.method == 'POST':
        post = Post.query.filter_by(id=post_id).first()
        if post:
            post.delete()
            flash("Post successfully deleted", "success")
            return redirect(url_for('index'))
        else:
            abort(404)