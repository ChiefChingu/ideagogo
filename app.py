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
    return render_template("home.html")


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
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    users = mongo.db.users
    if form.validate_on_submit():
        login_user = users.find_one({"email": form.email.data})
        if check_password_hash(login_user["password"], request.form["password"]):
            session["username"] = request.form["email"]
            flash(f"You have been logged in! Welcome {form.email.data}!", "success")
            return redirect(url_for("home"))
        flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/ideas")
def ideas():
    return render_template("ideas.html", title="Ideas", ideas=mongo.db.ideas.find())


@app.route("/idea-details/<idea_id>")
def idea_details(idea_id):
    the_idea = mongo.db.ideas.find_one({"_id": ObjectId(idea_id)})
    return render_template("idea-details.html", title="Idea details", idea=the_idea)


@app.route("/addidea")
def addidea():
    return render_template("addidea.html", title="Add Idea")


@app.route("/insertidea", methods=["POST"])
def insert_idea():
    ideas = mongo.db.ideas
    x = ideas.insert_one(request.form.to_dict())
    return redirect(url_for("idea_details", idea_id=x.inserted_id))


@app.route("/edit_idea/<idea_id>")
def edit_idea(idea_id):
    the_idea = mongo.db.ideas.find_one({"_id": ObjectId(idea_id)})
    return render_template("editidea.html", title="Edit Idea", idea=the_idea)


@app.route("/update_idea/<idea_id>", methods=["POST"])
def update_idea(idea_id):
    ideas = mongo.db.ideas
    ideas.update(
        {"_id": ObjectId(idea_id)},
        {
            "idea_title": request.form.get("idea_title"),
            "idea_summary": request.form.get("idea_summary"),
        },
    )
    return redirect(url_for("idea_details", idea_id=idea_id))


@app.route("/delete_idea/<idea_id>")
def delete_idea(idea_id):
    mongo.db.ideas.remove({"_id": ObjectId(idea_id)})
    return redirect(url_for("ideas"))


@app.route("/problems")
def problems():
    return render_template("problems.html", title="Problems")


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
