# This file contains miscellaenous functions that are used by various controllers in this application. 
from flask import abort
from main import db
from models.musicians import Musician
from models.labels import Label
from flask_jwt_extended import get_jwt_identity


# Function to ensure that string values are provided and no fields are missed.
def validate_string_field(data, field_name):
    field_value = data.get(field_name)
    if not isinstance(field_value, str):
        return abort(400, description=f"{field_name} must be a string value. Please ensure to include the field: {field_name}")
    return field_value


# Function to ensure that label_id foreign key provided is valid.
def validate_label_id(musician_fields, field_name):
    label_id = musician_fields.get(field_name)
    if label_id is not None:
        if not isinstance(label_id, int):
            return abort(400, description=f"{field_name} must be an integer value. Otherwise do not include {field_name} if you are not with a record label.")
        max_label_id = db.session.query(db.func.max(Label.id)).scalar()
        if label_id < 1 or label_id > max_label_id:
            return abort(400, description=f"{field_name} must be between 1 and {max_label_id}. Otherwise do not include {field_name} if you are not with a record label.")
    return label_id


# Function to check if musician user is an admin before proceeding
def check_admin():
    musician_id = get_jwt_identity()
    musician = Musician.query.get(musician_id)
    if not musician:
        return abort(401, description="Invalid musician. Please provide valid access token")
    if not musician.admin:
        return abort(401, description="Unauthorised musician. Not admin")