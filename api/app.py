from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    link = "https://picsum.photos/" + input_name + "/" + input_age
    return render_template("hello.html", link=link)


@app.route("/query", methods=["GET"])
def process_query(word):
    if word == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"

    if word == "asteroids":
        return "Unknown"
