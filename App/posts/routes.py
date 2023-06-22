from flask import Blueprint, render_template, url_for, redirect, request, flash, abort
from flask_login import login_required, current_user
from App.posts.forms import PostForm, UpdatePostForm
from App.models.posts import Post
from App.models.auth import User 

posts_bp = Blueprint('posts', __name__, static_folder='static')


@posts_bp.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    """This route create new post"""
    form = PostForm(request.form)
    if request.method == 'POST' and form.validate():
        post = Post(title=form.title.data,
                    description=form.description.data, user_id=current_user.id)
        post.insert()
        flash("New post successfully added", "success")
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        ...
    return render_template('posts_templates/create_post.html', title='New Post', form=form)


@posts_bp.route('/show_post/<int:post_id>', methods=['GET', 'POST'])
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
        return redirect(url_for('main.index'))
    return render_template('posts_templates/show_post.html', title='Show Post', post=post, form=form)


@posts_bp.route('/post/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    if request.method == 'POST':
        post = Post.query.filter_by(id=post_id).first()
        if post:
            post.delete()
            flash("Post successfully deleted", "success")
            return redirect(url_for('main.index'))
        else:
            abort(404)