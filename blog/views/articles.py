from flask import Blueprint, render_template

articles_app = Blueprint("articles_app", __name__)


ARTICLES = ["Flask", "Django", "JSON:API"]

@articles_app.route("/", endpoint="list")
def articles_list():
    return render_template("articles/list.html", articles=ARTICLES)

from flask import Blueprint, render_template, request, current_app, redirect, url_for
from werkzeug.exceptions import NotFound

from blog.models.database import db
from blog.models import Author, Article
from blog.forms.article import CreateArticleForm

articles_app = Blueprint("articles_app", __name__)


@articles_app.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles)


@articles_app.route("/<int:article_id>/", endpoint="details")
def article_detals(article_id):
    article = Article.query.filter_by(id=article_id).one_or_none()
    if article is None:
       raise NotFound
    return render_template("articles/details.html", article=article)

@articles_app.route("/<int:article_id>/", endpoint="details")
def article_detals(article_id):
    article = Article.query.filter_by(id=article_id).options(
        joinedload(Article.tags) # подгружаем связанные теги!
    ).one_or_none()
    if article is None:
       raise NotFound
    return render_template("articles/details.html", article=article)


@articles_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    ...
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    ...
    if request.method == "POST" and form.validate_on_submit():
        if form.tags.data:
           selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
           for tag in selected_tags:
              article.tags.append(tag)
    ...

