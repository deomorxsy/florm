 # -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

#from flask_login import login_required, login_user, logout_user

#from app.extensions import login_manager
from app.public.forms import LoginForm
from app.user.forms import RegisterForm
from app.models.user import User
from app.utils import flash_errors

blueprint = Blueprint("public", __name__, static_folder="../static")

@login_manager.user_loader
def load_user(user_id):
    """ load user by id """
    return User.get_by_id(int(user_id))

@blueprint.route("/", methods=["GET", "POST"])
def home():
    """ home page """
    form = LoginForm(request.form)
    current_app.logger.info("hello from home page")
    # handle logging in
    if request.method == "POST":
        if form.validate_on_submit():
            login_user(form.user)
            flash("you are logged in.", "sucess")

            redirect_url = request.args.get("next") or url_for("user.members")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/home.html", form=form)


@blueprint.route("/logout/")
@login_required
def logout():
    """ logout """
    logout_user()
    flash("you are logged out", "info")
    return redirect(url_for("public.home"))

@blueprint.route("/register/", methods=["GET", "POST"])
def register():
    """register new user"""
    form = RegisterForm(request.form)
    if form.validate_on_submit):
        User.create(
                username = form.username.data,
                email = form.email.data,
                password = form.password.data,
                active = True,
                )
        flash("thank you for registering, you can log in now ;D")
        return redirect(url_for("public.home"))
    else:
        flash_errors(form)
    return render_template("public/register.html", form=form)

@blueprint.route("/about/")
def about():
    """ about page """
    form = LoginForm(request.form)
    return render_template("public/about.html")
