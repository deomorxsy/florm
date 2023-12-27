# -*- coding: utf-8 -*-
""" User views """
from flask import Blueprint, render_template
from flask_login import login_required

#from app.user.forms import RegisterForm
# blueprint = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")

blueprint = Blueprint(
        "user", __name__,
        url_prefix="/users",
        static_folder="../static"
        )


@blueprint.route("/")
@login_required
def members():
    """ list members """
    return render_template("users/members.html")
