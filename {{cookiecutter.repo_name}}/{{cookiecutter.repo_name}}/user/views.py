from flask import Blueprint, render_template

from {{cookiecutter.repo_name}}.utils import login_required


blueprint = Blueprint("user", __name__, url_prefix='/users',
                        static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    return render_template("users/members.html")