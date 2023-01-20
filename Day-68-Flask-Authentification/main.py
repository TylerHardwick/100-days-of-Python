import werkzeug.security
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Flask-login configuring application
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        email_exists = db.session.query(User).filter_by(email=request.form["email"]).first()

        if email_exists:
            flash("You have already signed up. Please login instead.")
            return redirect(url_for("login"))
        new_user = User(
            email=request.form["email"],
            password=generate_password_hash(request.form["password"], method='pbkdf2:sha256', salt_length=8),
            name=request.form["name"]
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)




@app.route('/login', methods=['POST', 'GET'])

def login():
    if request.method == "POST":
        user = db.session.query(User).filter_by(email=request.form["email"]).first()
        if not user:
            flash("That email address does not exist. Please try again.")
            return redirect(url_for("login"))
        elif check_password_hash(user.password, request.form["password"]):
            print(f"{user.password} and {request.form['password']}")
            login_user(user)
            flash("Logged in successfully")
            return redirect(url_for("secrets"))
        else:
            flash("Password incorrect, please try again.")
            return redirect(url_for("login"))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    file_name = request.args.get("file_name")
    return send_from_directory("static/files", file_name, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
