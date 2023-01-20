from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import ast


app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Create SQL db
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///movie_library.db"
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer,nullable=True)
    review = db.Column(db.String(400), nullable=True)
    img_url = db.Column(db.String)


class UpdateForm(FlaskForm):
    update_rating = FloatField(label="Your rating out of 10 e.g 7.5")
    update_review = StringField(label="Your review")
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    movie_title = StringField(label="Movie Title")
    submit = SubmitField(label="Add Movie")

with app.app_context():
    db.create_all()


def find_movie(movie_title):
    tmdb_url = "https://api.themoviedb.org/3/search/movie?"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYjAxYzg2ZjA4ZmZmYjg3N2IxOWU0ZTllZjg1NDZjZSIsInN1YiI6IjYzYzA4MjI3MjNiZTQ2MDA4MTdjMjg4MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.M1jCpiymo_Go6cVaqoWOTMU9pmlbbiMwUX26sScg-i0"
    headers={"Authorization": f"Bearer {api_token}",
             "Content-Type": "application/json;charset=utf-8"}
    parameters = {
        "query": movie_title
    }
    tmdb_response = requests.get(tmdb_url, headers=headers, params=parameters).json()
    return tmdb_response


@app.route("/")
def home():
    # Pulls all movies from db by rating
    all_movies = Movie.query.order_by(Movie.rating).all()

    # Assigns ranking to movie based on order and commits to db
    for num in range(len(all_movies)):
        all_movies[num].ranking = len(all_movies) - num
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["POST", "GET"])
def edit():

    form = UpdateForm()
    movie_id = request.args.get("id")
    movie_to_edit = db.get_or_404(Movie, movie_id)

    # Update SQL DB
    if form.validate_on_submit():
        new_rating = form.update_rating.data
        new_review = form.update_review.data
        movie_to_edit.rating = new_rating
        if new_review != "":
            movie_to_edit.review = new_review
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie_to_edit)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.movie_title.data
        return redirect(url_for("select", movie=movie_title))
    return render_template("add.html", form=form)


@app.route("/select", methods=["GET", "POST"])
def select():
    movie = request.args.get("movie")
    list_of_movies = find_movie(movie)
    print(list_of_movies)
    return render_template("select.html", movies=list_of_movies)


@app.route("/update", methods=["POST", "GET"])
# add movie to SQL DB
def update_db():
    movie_string = request.args.get("movie")
    movie = ast.literal_eval(movie_string)
    print(movie)
    if movie:
        new_movie = Movie(
            title=movie["original_title"],
            year=movie["release_date"][:4],
            description=movie["overview"],
            img_url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}")
        db.session.add(new_movie)
        db.session.commit()
        select_movie = db.one_or_404(db.select(Movie).filter_by(title=movie["original_title"]))
        movie_id = select_movie.id
        return redirect(url_for("edit", id=movie_id))



if __name__ == '__main__':
    app.run(debug=True)
