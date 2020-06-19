import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from os import path
from forms import RegistrationForm, LoginForm
import email_validator
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date


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
            session["username"] = login_username["username"]
            if login_user["email"] == "admin@admin.com":
                session["username"] = "Master"
            flash(
                f"You have been logged in! Welcome {login_username} with email: {form.email.data}!",
                "success",
            )
            return redirect(url_for("ideas"))
        flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("pages/users/login.html", title="Login", form=form)


# make all user data available at a later stage - nice to have
# @app.route("/account")
# def account():
#     if not session.get("username") is None:
#         username = session.get("username")
#         return render_template("pages/users/account.html", title="Account")
#     else:
#         return redirect(url_for("register"))


@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("ideas"))


@app.route("/account_required")
def account_required():
    return render_template("pages/users/account-required.html", title="Hold on...")


#########################
# Images
#########################


@app.route("/file/<filename>")
def file(filename):
    return mongo.send_file(filename)


@app.route("/insert_image/<idea_id>", methods=["POST"])
def insert_image(idea_id):
    ideas = mongo.db.ideas
    if "image" in request.files:
        image = request.files["image"]
        mongo.save_file(image.filename, image)
        ideas.update(
            {"_id": ObjectId(idea_id)}, {"$set": {"image_name": image.filename}}
        )
    return redirect(url_for("idea_details", idea_id=idea_id))


#########################
# Ideas
#########################


@app.route("/ideas", methods=["GET", "POST"])
def ideas():
    ideas = mongo.db.ideas
    for doc in ideas.find().sort("total_votes", -1).limit(1):
        votes = doc

    return render_template(
        "pages/ideas/ideas.html",
        title="Ideas",
        ideas=mongo.db.ideas.find(),
        categories=mongo.db.categories.find().sort("category_name"),
        tags=mongo.db.tags.find().sort("tag_name"),
        votes=votes,
    )


@app.route("/<idea_id>")
def idea_details(idea_id):
    ideas = mongo.db.ideas
    the_idea = mongo.db.ideas.find_one({"_id": ObjectId(idea_id)})
    users = mongo.db.users.find()
    username = session.get("username")
    ideas.update_one(
        {"_id": ObjectId(idea_id)}, {"$inc": {"views": 1},},
    )
    # Control statement to check output in terminal
    # print(the_idea)

    return render_template(
        "pages/ideas/idea_details.html",
        idea=the_idea,
        title="Idea details",
        users=users,
    )


@app.route("/addidea")
def addidea():
    if not session.get("username") is None:
        username = session.get("username")
        return render_template(
            "pages/ideas/add_idea.html",
            title="Add Idea",
            categories=mongo.db.categories.find().sort("category_name"),
            users=mongo.db.users.find(),
            all_tags=mongo.db.tags.find().sort("tag_name"),
            all_tags_two=mongo.db.tags.find().sort("tag_name"),
            all_tags_three=mongo.db.tags.find().sort("tag_name"),
        )
    else:
        return redirect(url_for("account_required"))


@app.route("/insertidea", methods=["POST"])
def insert_idea():
    ideas = mongo.db.ideas

    x = ideas.insert_one(request.form.to_dict())
    idea_id = x.inserted_id
    ideas.update({"_id": ObjectId(idea_id)}, {"$set": {"total_votes": 0, "views": 0}})
    if "image" in request.files:
        image = request.files["image"]
        mongo.save_file(image.filename, image)
        ideas.update(
            {"_id": ObjectId(idea_id)}, {"$set": {"image_name": image.filename}}
        )

    today = date.today()
    date_added = today.strftime("%B %d, %Y")
    ideas.update({"_id": ObjectId(idea_id)}, {"$set": {"date_added": date_added}})

    return redirect(url_for("idea_details", idea_id=x.inserted_id))


@app.route("/edit_idea/<idea_id>")
def edit_idea(idea_id):
    the_idea = mongo.db.ideas.find_one({"_id": ObjectId(idea_id)})
    all_categories = mongo.db.categories.find().sort("category_name")
    all_users = mongo.db.users.find()
    all_tags = mongo.db.tags.find().sort("tag_name")
    all_tags_two = mongo.db.tags.find().sort("tag_name")
    all_tags_three = mongo.db.tags.find().sort("tag_name")
    return render_template(
        "pages/ideas/edit_idea.html",
        title="Edit Idea",
        idea=the_idea,
        categories=all_categories,
        users=all_users,
        all_tags=all_tags,
        all_tags_two=all_tags_two,
        all_tags_three=all_tags_three,
    )


@app.route("/update_idea/<idea_id>", methods=["POST"])
def update_idea(idea_id):
    ideas = mongo.db.ideas
    ideas.update(
        {"_id": ObjectId(idea_id)},
        {
            "$set": {
                "idea_title": request.form.get("idea_title"),
                "category_name": request.form.get("category_name"),
                "idea_summary": request.form.get("idea_summary"),
                "idea_details": request.form.get("idea_details"),
                "idea_tag1": request.form.get("idea_tag1"),
                "idea_tag2": request.form.get("idea_tag2"),
                "idea_tag3": request.form.get("idea_tag3"),
            }
        },
    )
    return redirect(url_for("idea_details", idea_id=idea_id))


@app.route("/delete_idea/<idea_id>")
def delete_idea(idea_id):
    mongo.db.ideas.remove({"_id": ObjectId(idea_id)})
    return redirect(url_for("ideas"))


#########################
# Search routes
#########################


@app.route("/search_by_category", methods=["POST"])
def search_by_category():
    ideas = mongo.db.ideas
    searched_category = request.form.get("category_name")
    results_searched_category = ideas.find({"category_name": searched_category})
    return render_template(
        "pages/search/category_search.html",
        queried_category=results_searched_category,
        ideas=mongo.db.ideas.find(),
        categories=mongo.db.categories.find().sort("category_name"),
        searched_category=searched_category,
    )


@app.route("/search_by_tag", methods=["POST"])
def search_by_tag():
    ideas = mongo.db.ideas
    searched_tag = request.form.get("tag_name")
    results_searched_tag = ideas.find(
        {
            "$or": [
                {"idea_tag1": searched_tag},
                {"idea_tag2": searched_tag},
                {"idea_tag3": searched_tag},
            ]
        }
    )
    return render_template(
        "pages/search/tag_search.html",
        queried_tag=results_searched_tag,
        ideas=mongo.db.ideas.find(),
        tags=mongo.db.tags.find().sort("tag_name"),
        searched_tag=searched_tag,
    )


#########################
# Upvote & downvote
#########################


@app.route("/upvote/<idea_id>", methods=["POST"])
def upvote_idea(idea_id):
    if not session.get("username") is None:

        ideas = mongo.db.ideas
        username = session.get("username")

        # push username of vote to idea document
        ideas.update_one(
            {"_id": ObjectId(idea_id)},
            {
                "$inc": {"total_votes": 1},
                "$push": {"user_votes": {"$each": [username]}},
            },
        )

        # push idea id to user profile
        users = mongo.db.users
        users.update_one(
            {"username": username},
            {"$push": {"voted_ideas": {"$each": [ObjectId(idea_id)]}},},
        )

        flash(
            f"Thanks for voting!", "success",
        )

        return redirect(url_for("idea_details", idea_id=idea_id))
    else:
        return redirect(url_for("account_required"))


@app.route("/downvote/<idea_id>", methods=["POST"])
def downvote_idea(idea_id):
    username = session.get("username")
    ideas = mongo.db.ideas

    # pull username of vote from idea document
    ideas.update_one(
        {"_id": ObjectId(idea_id)},
        {"$inc": {"total_votes": -1}, "$pull": {"user_votes": username},},
    )

    # pull idea id from user profile
    username = session.get("username")
    users = mongo.db.users
    users.update_one(
        {"username": username}, {"$pull": {"voted_ideas": [ObjectId(idea_id)]}},
    )

    flash(
        f"Vote is removed!", "success",
    )

    return redirect(url_for("idea_details", idea_id=idea_id))


#########################
# Contact & About
#########################


@app.route("/contact")
def contact():
    username = session.get("username")
    users = mongo.db.users
    loggedInUser = users.find_one({"username": session.get("username")})
    print(loggedInUser)
    return render_template(
        "pages/contact.html", title="Contact", loggedInUser=loggedInUser
    )


# return render_template("pages/contact.html", title="Contact", user=loggedInUser)

#########################
# Admin pages
#########################


@app.route("/admin")
def admin():
    if session.get("username") == "Master":
        return render_template(
            "pages/categories/admin.html",
            categories=mongo.db.categories.find().sort("category_name"),
            tags=mongo.db.tags.find().sort("tag_name"),
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
    return redirect(url_for("add_category"))


@app.route("/add_category")
def add_category():
    return render_template(
        "pages/categories/add_category.html", categories=mongo.db.categories.find()
    )


#########################
# Tags
#########################


@app.route("/delete_tag/<tag_id>")
def delete_tag(tag_id):
    mongo.db.tags.remove({"_id": ObjectId(tag_id)})
    return redirect(url_for("admin"))


@app.route("/edit_tag/<tag_id>")
def edit_tag(tag_id):
    return render_template(
        "pages/tags/edit_tag.html",
        tag=mongo.db.tags.find_one({"_id": ObjectId(tag_id)}),
    )


@app.route("/update_tag/<tag_id>", methods=["POST"])
def update_tag(tag_id):
    mongo.db.tags.update(
        {"_id": ObjectId(tag_id)}, {"tag_name": request.form.get("tag_name")},
    )
    return redirect(url_for("admin"))


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
