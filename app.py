import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from os import path
from forms import RegistrationForm, LoginForm
import email_validator
from werkzeug.security import generate_password_hash, check_password_hash


if path.exists("env.py"):
    import env

app = Flask(__name__)

MONGODB_URI = os.environ.get("bashrc")

app.config["MONGO_DBNAME"] = "ideas"
app.config["MONGO_URI"] = MONGODB_URI
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("pages/home.html")


#########################
# User related
#########################


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    users = mongo.db.users
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, "sha256")
        users.insert(
            {
                "username": request.form.get("username"),
                "email": request.form.get("email"),
                "password": hashed_password,
            }
        )
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("login"))
    return render_template("pages/users/register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    users = mongo.db.users
    if form.validate_on_submit():
        login_user = users.find_one({"email": form.email.data})
        login_username = users.find_one(
            {"email": form.email.data}, {"_id": 0, "username": 1}
        )
        if check_password_hash(login_user["password"], request.form["password"]):
            session["username"] = request.form["email"]
            if login_user["email"] == "admin@admin.com":
                session["username"] = "Master"
                print(session["username"])
            flash(
                f"You have been logged in! Welcome {login_username} with email: {form.email.data}!",
                "success",
            )
            return redirect(url_for("home"))
        flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("pages/users/login.html", title="Login", form=form)


@app.route("/account")
def account():
    if not session.get("username") is None:
        username = session.get("username")
        return render_template("pages/users/account.html")
    else:
        return redirect(url_for("register"))


# make all user data available at a later stage - nice to have


@app.route("/logout")
def logout():
    session.pop("username")
    return render_template("pages/home.html")


@app.route("/account_required")
def account_required():
    return render_template("pages/users/account-required.html")


#########################
# Ideas
#########################


@app.route("/ideas")
def ideas():
    return render_template(
        "pages/ideas/ideas.html", title="Ideas", ideas=mongo.db.ideas.find()
    )


@app.route("/idea-details/<idea_id>")
def idea_details(idea_id):
    the_idea = mongo.db.ideas.find_one({"_id": ObjectId(idea_id)})
    users = mongo.db.users.find()
    return render_template(
        "pages/ideas/idea_details.html",
        idea=the_idea,
        title="Idea details",
        users=users,
    )


# maybe use uathor of idea_owner to prevent confusion while passing variables/db names
@app.route("/addidea")
def addidea():
    if not session.get("username") is None:
        username = session.get("username")
        return render_template(
            "pages/ideas/add_idea.html",
            title="Add Idea",
            categories=mongo.db.categories.find(),
            users=mongo.db.users.find(),
        )
    else:
        return redirect(url_for("account_required"))


@app.route("/insertidea", methods=["POST"])
def insert_idea():
    ideas = mongo.db.ideas
    x = ideas.insert_one(request.form.to_dict())
    return redirect(url_for("idea_details", idea_id=x.inserted_id))


@app.route("/edit_idea/<idea_id>")
def edit_idea(idea_id):
    the_idea = mongo.db.ideas.find_one({"_id": ObjectId(idea_id)})
    all_categories = mongo.db.categories.find()
    all_users = mongo.db.users.find()
    return render_template(
        "pages/ideas/edit_idea.html",
        title="Edit Idea",
        idea=the_idea,
        categories=all_categories,
        users=all_users,
    )


@app.route("/update_idea/<idea_id>", methods=["POST"])
def update_idea(idea_id):
    ideas = mongo.db.ideas
    ideas.update(
        {"_id": ObjectId(idea_id)},
        {
            "username": request.form.get("username"),
            "idea_title": request.form.get("idea_title"),
            "category_name": request.form.get("category_name"),
            "idea_summary": request.form.get("idea_summary"),
            "idea_details": request.form.get("idea_details"),
        },
    )
    return redirect(url_for("idea_details", idea_id=idea_id))


@app.route("/delete_idea/<idea_id>")
def delete_idea(idea_id):
    mongo.db.ideas.remove({"_id": ObjectId(idea_id)})
    return redirect(url_for("ideas"))


# Problems


@app.route("/problems")
def problems():
    return render_template("pages/problems.html", title="Problems")


#########################
# Admin pages
#########################


@app.route("/admin")
def admin():
    if session.get("username") == "Master":
        return render_template(
            "pages/categories/admin.html",
            categories=mongo.db.categories.find(),
            tags=mongo.db.tags.find(),
        )
    else:
        return redirect(url_for("home"))


#########################
# Categories
#########################


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    return redirect(url_for("admin"))


@app.route("/edit_category/<category_id>")
def edit_category(category_id):
    return render_template(
        "pages/categories/edit_category.html",
        category=mongo.db.categories.find_one({"_id": ObjectId(category_id)}),
    )


@app.route("/update_category/<category_id>", methods=["POST"])
def update_category(category_id):
    mongo.db.categories.update(
        {"_id": ObjectId(category_id)},
        {"category_name": request.form.get("category_name")},
    )
    return redirect(url_for("admin"))


@app.route("/insert_category", methods=["POST"])
def insert_category():
    category_doc = {"category_name": request.form.get("category_name")}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for("admin"))


@app.route("/add_category")
def add_category():
    return render_template("pages/categories/add_category.html")


#########################
# Tags
#########################


@app.route("/insert_tag", methods=["POST"])
def insert_tag():
    tag_doc = {"tag_name": request.form.get("tag_name")}
    mongo.db.tags.insert_one(tag_doc)
    return redirect(url_for("add_tag"))


@app.route("/add_tag")
def add_tag():
    return render_template("pages/tags/add_tag.html", tags=mongo.db.tags.find())


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
