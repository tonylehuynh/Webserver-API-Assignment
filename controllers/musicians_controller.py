from flask import Blueprint, jsonify, request, abort
from main import db
from models.musicians import Musician
from schemas.musician_schema import musician_schema, musicians_schema
from datetime import timedelta
from main import bcrypt
from flask_jwt_extended import create_access_token
from marshmallow.exceptions import ValidationError


musician = Blueprint('musician', __name__, url_prefix="/musician")


@musician.route("/register", methods=["POST"])
# Function to register musician
def musician_register():
    try:
        musician_fields = musician_schema.load(request.json)
    except ValidationError as error:
        return abort(400, description=error.messages)
    # Find the musician
    musician = Musician.query.filter_by(email=musician_fields["email"]).first()

    if musician:
        return abort(400, description="Musician & Email already registered")

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

    label_id = musician_fields.get("label_id")
    if label_id is not None:
        if not isinstance(label_id, int):
            return abort(400, description="Label ID must be an integer value. Otherwise do not include a label_id.")
        elif label_id < 1 or label_id > 5:
            return abort(400, description="Label ID must be between 1 and 5. Otherwise do not include a label_id.")

        musician.label_id = label_id

    db.session.add(musician)
    db.session.commit()

    expiry = timedelta(days=1)
    access_token = create_access_token(
        identity=str(musician.id), expires_delta=expiry)

    return jsonify({"email": musician.email, "access token": access_token})


# Function to ensure that string values are provided and no fields are missed.
def validate_string_field(data, field_name):
    field_value = data.get(field_name)
    if not isinstance(field_value, str):
        return abort(400, description=f"{field_name} must be a string value. Please ensure to include the field: {field_name}")
    return field_value
