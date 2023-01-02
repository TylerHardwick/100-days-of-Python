from flask import Flask, render_template
import requests

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"
app = Flask(__name__)


@app.route("/")
def home():
    blog_posts = requests.get(BLOG_URL).json()

    return render_template("index.html", posts=blog_posts)


@app.route("/post/<int:blog_id>")
def post(blog_id):
    blog_posts = requests.get(BLOG_URL).json()
    return render_template("post.html", posts=blog_posts, blog_id=blog_id)




if __name__ == "__main__":
    app.run(debug=True)
