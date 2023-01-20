from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///library.db"
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()



@app.route('/', methods=["GET", "POST"])
def home():
    with app.app_context():
        all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["book"], author=request.form["author"], rating= request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit/id_<book_id>", methods=["GET", "POST"])
def edit(book_id):
    if request.method == "POST":

        # Update record:
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for("home"))

    with app.app_context():
        selected_book = db.session.execute(db.select(Book).filter_by(id=book_id)).scalar()
    return render_template("edit.html",book=selected_book, book_id=book_id)

@app.route("/delete")
def delete():
    book_id = request.args.get("book_id")
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))






if __name__ == "__main__":
    app.run(debug=True)

