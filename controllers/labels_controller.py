from flask import Blueprint, jsonify, request, abort
from main import db
from models.labels import Label
from models.musicians import Musician
from schemas.label_schema import label_schema, labels_schema
from flask_jwt_extended import jwt_required
from functions import check_admin, validate_string_field


labels = Blueprint('labels', __name__, url_prefix="/labels")


# GET route endpoints to query record labels
@labels.route("/", methods=["GET"])
# Function to get list of all record labels
def get_labels():
    labels_list = Label.query.all()
    result = labels_schema.dump(labels_list)
    return jsonify(result)


# POST route endpoint
@labels.route("/create", methods=["POST"])
@jwt_required()
# Function to create new record label
def create_label():
    label_fields = label_schema.load(request.json)
    # Ensure musician is admin before being able to create new label
    check_admin()
    # Check if label already exists
    name = validate_string_field(label_fields, "name")
    label = Label.query.filter_by(name=name).first()
    if label:
        return abort(400, description="Label already exists.")

    # Add new label
    new_label = Label()
    new_label.name = name
    new_label.type = validate_string_field(label_fields, "type")
    db.session.add(new_label)
    db.session.commit()

    return jsonify(label_schema.dump(new_label))


# PUT route endpoint
@labels.route("/<int:id>/", methods=["PUT"])
@jwt_required()
# Function to update label
def update_label(id):
    label_fields = label_schema.load(request.json)
    # Ensure musician is admin
    check_admin()
    # Find the label
    label = Label.query.filter_by(id=id).first()
    if not label:
        return abort(400, description="Label does not exist")
    # Update label details with new provided values
    label.name = validate_string_field(label_fields, "name")
    label.type = validate_string_field(label_fields, "type")
    db.session.commit()

    return jsonify(label_schema.dump(label))


# DELETE route endpot to delete label from database
@labels.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_label(id):
    # Ensure musician is admin
    check_admin()

    # Find all musicians referencing the label and set their label_id to NULL due to the foreign key constraint
    musicians = Musician.query.filter_by(label_id=id).all()
    for musician in musicians:
        musician.label_id = None
    db.session.commit()

    # Find the label
    label = Label.query.filter_by(id=id).first()
    if not label:
        return abort(400, description="Label does not exist")
    # Delete the label from the database and commit
    db.session.delete(label)
    db.session.commit()

    return jsonify(label_schema.dump(label))
