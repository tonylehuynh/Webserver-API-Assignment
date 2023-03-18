from flask import Blueprint, jsonify, request, abort
from main import db
from models.musicians import Musician
from schemas.musician_schema import musician_schema, musicians_schema
from datetime import timedelta
from main import bcrypt
from flask_jwt_extended import jwt_required, create_access_token
from marshmallow.exceptions import ValidationError
from functions import validate_string_field, validate_label_id, check_admin


musician = Blueprint('musician', __name__, url_prefix="/musician")


# GET ROUTES endpoints
@musician.route("/list", methods=["GET"])
# Function to get list of all musicians
def get_musicians():
    musicians_list = Musician.query.all()
    result = musicians_schema.dump(musicians_list)
    return jsonify(result)


# POST routes endpoints
@musician.route("/register", methods=["POST"])
# Function to register musician
def musician_register():
    musician_fields = request.json
    # Check if email & password fields are present
    if "email" and "password" not in musician_fields:
        return abort(400, description="Email and password are required to register. Include the fields: email, password")
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


@musician.route("/login", methods=["POST"])
# Function to login as a musician by providing email and password.
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


# PUT route endpoint to update musician details
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


# DELETE route endpot to delete musician from database
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
