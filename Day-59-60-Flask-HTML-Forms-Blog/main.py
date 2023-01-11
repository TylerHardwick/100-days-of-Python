from flask import Flask, render_template, request
import requests
import smtplib


my_email = "Email here"
password = "Email Password here"

blog_posts = requests.get("https://api.npoint.io/9bfd6fe087e3fbceda27").json()




# Web Server
app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template("index.html", posts=blog_posts)


@app.route("/about")
def get_about():
    return render_template("about.html")



@app.route("/post/<int:post_num>")
def get_blog_post(post_num):
    return render_template("post.html", posts=blog_posts, post_num=post_num)


@app.route("/contact", methods=["POST", "GET"])
def receive_data():
    method = request.method
    if method == "POST":
        sent_header = "Successfully sent your message."
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        # Send Email

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="To Email here",
                                msg=f"Subject:New Message from your Blog!\n\n "
                                    f"Name: {name}\n Email: {email}\n Phone: {phone}\n\n {message}")
            print("Message emailed to Tyler.")


        return render_template("contact.html", sent_header=sent_header)
    else:
        sent_header = "Contact Me"
        return render_template("contact.html", sent_header=sent_header)




if __name__ == "__main__":
    app.run(debug=True)
