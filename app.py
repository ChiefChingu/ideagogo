import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path

if path.exists("env.py"):
    import env

app = Flask(__name__)

MONGODB_URI = os.environ.get("bashrc")

app.config["MONGO_DBNAME"] = "ideas"
app.config["MONGO_URI"] = MONGODB_URI

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


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


# @app.route("/insertidea", methods=["POST"])
# def insert_idea():
#     ideas = mongo.db.ideas
#     ideas.insert_one(request.form.to_dict())
#     return redirect(url_for("idea-details"))


@app.route("/problems")
def problems():
    return render_template("problems.html", title="Problems")


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
