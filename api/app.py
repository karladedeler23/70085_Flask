from flask import Flask, render_template, request
import re

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


@app.route("/query")
def handle_query():
    return process_query(request.args.get("q"))


def process_query(word):
    if "dinosaurs" in word:
        return "Dinosaurs ruled the Earth 200 million years ago"

    if "asteroids" in word:
        return "Unknown"

    if word == "What is your name?":
        return "Howell_Karla_Joey"

    if "plus" in word:
        matches = re.findall(r'\d+', word)
        integers = [int(match) for match in matches]
        return str(sum(integers))

    if "largest" in word:
        matches = re.findall(r'\d+', word)
        integers = [int(match) for match in matches]
        return str(max(integers))

    if "multiplied" in word:
        matches = re.findall(r'\d+', word)
        integers = [int(match) for match in matches]
        return str(integers[0] * integers[1])

    def test_six(x):
        y = x**(1/6)
        y = int(y)
        if y**6 == x:
            return True
        else:
            return False

    if "square" in word and "cube" in word:
        matches = re.findall(r'\d+', word)
        integers = [int(match) for match in matches]
        for x in integers:
            if test_six(x):
                return str(x)
        return ""
    else:
        return str(100)
