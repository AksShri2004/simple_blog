from flask import Flask, render_template
from post import Post


app = Flask(__name__)
data = Post().request

@app.route('/')
def home():
    return render_template("index.html", data = data)

@app.route("/post/<id>")
def post(id):
    id = int(id) - 1
    return render_template("post.html", id = id, data = data)

if __name__ == "__main__":
    app.run(debug=True)
