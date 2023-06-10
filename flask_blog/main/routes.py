from flask import Flask, Blueprint, request, render_template, redirect
from auth.models import User
from posts.models import Post

main = Blueprint("main", __name__)


@main.route('/')
@main.route('/index')
def index():
    # all_post = Post.query.join(User, Post.user_id == User.id).all()
    page = request.args.get('page', 1, type=int)

    all_post = Post.query.join(User).\
        with_entities(Post.id, Post.title, Post.description, Post.post_date, User.username).\
        order_by(Post.post_date.desc()).paginate(page=page, per_page=2)
    return render_template('home.html', title='Home', posts=all_post)


@main.route('/about')
def about():
    return render_template('about.html', title='About Us')