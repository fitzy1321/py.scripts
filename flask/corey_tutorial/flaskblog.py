import os

from flask import Flask, render_template

posts = [
    {
        "author": "Joe Fitz",
        "title": "FIRST!",
        "content": "My 'FIRST!' blog post. How exciting!",
        "date_posted": "October 10, 2019",
    },
    {
        "author": "Jane Doe",
        "title": "Why author 1 is childish",
        "content": "I have like opnioins and stuff. LISTEN TO ME!",
        "date_posted": "October 10, 2019",
    },
]

template_dir = os.path.abspath("./templates/")
app = Flask(__name__, template_folder=template_dir)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
