from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from db import collection

app = Flask(__name__)

# HOME
@app.route("/")
def index():
    users = collection.find()
    return render_template("index.html", users=users)


# CREATE
@app.route("/create", methods=["POST"])
def create_user():
    name = request.form["name"]
    email = request.form["email"]
    age = int(request.form["age"])

    collection.insert_one({
        "name": name,
        "email": email,
        "age": age
    })
    return redirect(url_for("index"))


# UPDATE
@app.route("/update/<id>", methods=["POST"])
def update_user(id):
    name = request.form["name"]
    age = int(request.form["age"])

    collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"name": name, "age": age}}
    )
    return redirect(url_for("index"))


# DELETE
@app.route("/delete/<id>")
def delete_user(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)