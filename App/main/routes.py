from flask import Blueprint, request, render_template
from App.models.auth import User
from App.models.posts import Post


main_bp = Blueprint("main", __name__)


@main_bp.route('/')
@main_bp.route('/index') 
def index():
    # all_post = Post.query.join(User, Post.user_id == User.id).all()
    page = request.args.get('page', 1, type=int)

    all_post = Post.query.join(User).\
        with_entities(Post.id, Post.title, Post.description, Post.post_date, User.username).\
        order_by(Post.post_date.desc()).paginate(page=page, per_page=2)
    return render_template('main_templates/home.html', title='Home', posts=all_post)


@main_bp.route('/about')
def about():
    return render_template('main_templates/about.html', title='About Us')