from flask import Blueprint, jsonify, request, abort
from main import db
from models.musicians import Musician
from models.credits import Credit
from schemas.musician_schema import musician_schema, musicians_schema
from schemas.credit_schema import credits_schema
from datetime import timedelta, datetime
from main import bcrypt
from flask_jwt_extended import jwt_required, create_access_token
from marshmallow.exceptions import ValidationError
from functions import validate_string_field, validate_label_id, check_admin
from sqlalchemy import and_, extract


musician = Blueprint('musician', __name__, url_prefix="/musician")


# GET ROUTES endpoints

# Retrieves all songs from database. Admin excluded
# If profession is specified in the URL, such as http://localhost:5000/musician/list?profession=Drummer, then it will return musicians with that specific profession. 
@musician.route("/list", methods=["GET"])
def get_musicians_by_profession():
    profession = request.args.get("profession")
    # If no profession is provided in URL, then return list of all musicians
    if profession is None:
        musicians_list = Musician.query.filter_by(admin=False).all()
        result = musicians_schema.dump(musicians_list)
        return jsonify(result)

    professions_list = db.session.query(Musician.profession).distinct()
    professions = [row[0] for row in professions_list]
    # If profession does not exist in database, return message.
    if profession not in professions:
        return jsonify({"message": f"Profession '{profession}' does not exist. Please note professsion is also case sensitive."})
    musicians_list = Musician.query.filter_by(
        profession=profession, admin=False).all()
    result = musicians_schema.dump(musicians_list)
    return jsonify(result)


# Retrieves all musicians from database with a label id
@musician.route("/with_label", methods=["GET"])
def get_musicians_with_label():
    musicians_list = Musician.query.filter(
        Musician.label_id.isnot(None), Musician.admin == False).all()
    result = musicians_schema.dump(musicians_list)
    return jsonify(result)


# Retrieves all musicians from database with no label id. Admin user is not to be included in list.
@musician.route("/no_label", methods=["GET"])
def get_musicians_without_label():
    musicians_list = Musician.query.filter(
        Musician.label_id == None, Musician.admin == False).all()
    result = musicians_schema.dump(musicians_list)
    return jsonify(result)

 
# Retrieve all credits associated with a musician ID, where ID is provided in the URL.
# Can also further filter the credits retrieved by contribution date in URL - example is: http://localhost:5000/musician/3/credits?contribution_date=2014
@musician.route("/<int:musician_id>/credits", methods=["GET"])
def get_musician_credits(musician_id):
    # Query for the musician by ID
    musician = Musician.query.get(musician_id)
    # If musician doesn't exist, return 404
    if not musician:
        return jsonify({"message": "Musician not found"}), 404

    # Get the contribution date parameter from the URL
    contribution_date_str = request.args.get("contribution_date")
    if contribution_date_str:
        try:
            contribution_date = datetime.strptime(
                contribution_date_str, '%Y').date()
        except ValueError:
            return jsonify({"message": f"Invalid contribution date: {contribution_date_str}. Use YYYY format."}), 400
        # Get the list of credits for the musician and contribution date
        credits_list = Credit.query.filter(and_(Credit.musician_id == musician.id, extract(
            'year', Credit.contribution_date) == contribution_date.year)).all()
    else:
        # Get the list of all credits for the musician
        credits_list = Credit.query.filter_by(musician_id=musician.id).all()

    # Create a dictionary with the musician name and credits
    musician_credits = {
        "musician_name": f"{musician.first_name} {musician.last_name}",
        "credits": credits_schema.dump(credits_list)
    }
    return jsonify(musician_credits)


# POST routes endpoints. This route registers and creates a new musician in the database with the fields provided in the request.
@musician.route("/register", methods=["POST"])
def musician_register():
    musician_fields = request.json
    # Check if email & password fields are present
    if "email" and "password" not in musician_fields:
        return abort(400, description="Email and password are required to register, with string values. Include the fields: email, password.")
    # Check if password length requirements are met
    try:
        musician_fields = musician_schema.load(musician_fields)
    except ValidationError as error:
        return abort(400, description=error.messages)
    # Check if musician already exists
    musician = Musician.query.filter_by(email=musician_fields["email"]).first()
    if musician:
        return abort(400, description="Musician & Email already registered")

    # Provided musician details for regisration
    musician = Musician()
    musician.first_name = validate_string_field(musician_fields, "first_name")
    musician.last_name = validate_string_field(musician_fields, "last_name")
    musician.profession = validate_string_field(musician_fields, "profession")
    musician.phone_number = validate_string_field(
        musician_fields, "phone_number")
    musician.email = validate_string_field(musician_fields, "email")
    # Add the password attribute hashed by bcrypt
    musician.password = bcrypt.generate_password_hash(
        musician_fields["password"]).decode("utf-8")
    musician.admin = False
    label_id = validate_label_id(musician_fields, "label_id")
    if label_id is not None:
        musician.label_id = label_id

    db.session.add(musician)
    db.session.commit()

    expiry = timedelta(days=1)
    access_token = create_access_token(
        identity=str(musician.id), expires_delta=expiry)

    return jsonify({"message": "Musician registered successfully",
                    "email": musician.email,
                    "access_token": access_token})


# This route will login a musician in the application if correct email and password fields are provided in the request. JSON access token will also be returned once successful. 
@musician.route("/login", methods=["POST"])
def musician_login():
    musician_fields = request.json
    email = validate_string_field(musician_fields, "email")
    password = validate_string_field(musician_fields, "password")

    musician = Musician.query.filter_by(email=email).first()
    if not musician or not bcrypt.check_password_hash(musician.password, password):
        return abort(401, description="Incorrect email or password")

    expiry = timedelta(days=1)
    access_token = create_access_token(
        identity=str(musician.id), expires_delta=expiry)
    return jsonify({"message": "Musician logged in successfully",
                    "email": musician.email,
                    "access_token": access_token})


# PUT route endpoint. This route updates an existing musician in the database with the fields provided in the request.
@musician.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_musician(id):
    musician_fields = musician_schema.load(request.json)
    # Ensure musician is admin
    check_admin()
    # Find the musician
    musician = Musician.query.filter_by(id=id).first()
    if not musician:
        return abort(400, description="Musician does not exist")
    # Update musician details with new provided values. Not all values need to be provided.
    if 'first_name' in musician_fields:
        musician.first_name = validate_string_field(
            musician_fields, "first_name")
    if 'last_name' in musician_fields:
        musician.last_name = validate_string_field(
            musician_fields, "last_name")
    if 'profession' in musician_fields:
        musician.profession = validate_string_field(
            musician_fields, "profession")
    if 'phone_number' in musician_fields:
        musician.phone_number = validate_string_field(
            musician_fields, "phone_number")
    if 'email' in musician_fields:
        musician.email = validate_string_field(musician_fields, "email")
    if 'password' in musician_fields:
        musician.password = validate_string_field(musician_fields, "password")
    if 'admin' in musician_fields:
        musician.admin = musician_fields["admin"]
    if 'label_id' in musician_fields:
        musician.label_id = validate_label_id(musician_fields, "label_id")
    db.session.commit()

    return jsonify(message="Musician updated successfully", musician=musician_schema.dump(musician))


# DELETE route endpoint. This route deletes a specified musician from the database, with the musician id provided in the URL.
@musician.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_musician(id):
    # Ensure musician is admin
    check_admin()
    # Find the musician
    musician = Musician.query.filter_by(id=id).first()
    if not musician:
        return abort(400, description="Musician does not exist")
    db.session.delete(musician)
    db.session.commit()

    return jsonify(message="Musician deleted successfully", musician=musician_schema.dump(musician))
