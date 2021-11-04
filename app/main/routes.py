from app.models import Article
from datetime import datetime
from flask import Blueprint, render_template


main = Blueprint('main', __name__)

@main.route('/')
def index():
    articles = Article.query.order_by(Article.id.desc()).all()
    return render_template('index.html', title='Home', articles=articles, now=datetime.utcnow())