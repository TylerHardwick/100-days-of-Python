from flask import Flask, render_template, url_for
import requests


blog_posts = requests.get("https://api.npoint.io/9bfd6fe087e3fbceda27").json()





# Web Server
app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template("index.html", posts=blog_posts)


@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route("/contact")
def get_contact():
    return render_template("contact.html")

@app.route("/post/<int:post_num>")
def get_blog_post(post_num):
    return render_template("post.html", posts=blog_posts, post_num=post_num)



if __name__ == "__main__":
    app.run(debug=True)
