import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

### Documentation:
# https://documenter.getpostman.com/view/25359726/2s8ZDU64Uo


app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def convert_to_dict(self):
        dictionary = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record


@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    # Converts random_cafe table to dict to json and returns json file.
    cafe = random_cafe.convert_to_dict()
    return jsonify(cafe)


@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    # Converts cafe's into dictionaries and adds them to a list.
    list_of_cafes = [cafe.convert_to_dict() for cafe in cafes]
    return jsonify(list_of_cafes)


@app.route("/search")
def get_search_cafes():
    loc = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=loc).first()
    if cafe:
        cafe = cafe.convert_to_dict()
        return jsonify(cafe)
    else:
        return jsonify(error={"Not Found": "Sorry, we do not have any cafés currently listed at this location"})


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"))
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new café."})

## HTTP PUT/PATCH - Update Record


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def patch_update_price(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        new_price = request.args.get("new_price")
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(response={"error 404": "Sorry, we are unable to find a café with that id."}), 404



## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        api_key = request.args.get("api_key")
        if api_key == "TOPSecretAPIKey":
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the café."}), 200
        else:
            return jsonify(response={"error": "Sorry, that api-key is not authorised to make this change."
                                              "Please confirm that the api-key is correct."}), 403
    else:
        return jsonify(response={"error 404": "Sorry, we are unable to find a café with that id."}), 404




if __name__ == '__main__':
    app.run(debug=True)
