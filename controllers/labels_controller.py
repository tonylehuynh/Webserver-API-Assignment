from flask import Blueprint, jsonify, request, abort
from main import db
from models.labels import Label
from models.musicians import Musician
from schemas.label_schema import label_schema, labels_schema
from schemas.musician_schema import musicians_schema
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


@labels.route("/<int:label_id>/musicians", methods=["GET"])
# Function to get a particular record label and all associated musicians with the label. Can also filter by musician's profession too in the URL.
def get_label_and_musicians(label_id):
    label = Label.query.get(label_id)
    if label is None:
        abort(404, description="Label id does not exist")
    result = label_schema.dump(label)

    profession = request.args.get("profession")
    # If no profession is provided in URL, then return all musicians associated with the label
    if profession is None:
        musicians_list = Musician.query.filter_by(label_id=label_id).all()
        result = musicians_schema.dump(musicians_list)
        return jsonify(result)

    # If profession is provioded in URL - e.g. /musicians?profession=Drummer
    professions_list = db.session.query(Musician.profession).distinct()
    professions = [row[0] for row in professions_list]
    # If profession does not exist in database, return message.
    if profession not in professions:
        return jsonify({"message": f"Profession '{profession}' does not exist. Please note profession is also case sensitive."})
    musicians_list = Musician.query.filter_by(
        label_id=label_id, profession=profession, admin=False).all()
    result = musicians_schema.dump(musicians_list)
    return jsonify(result)


# POST route endpoint to create new label
@labels.route("/create", methods=["POST"])
@jwt_required()
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

    return jsonify(message="Label created successfully", label=label_schema.dump(new_label))


# PUT route endpoint to update label
@labels.route("/<int:id>/", methods=["PUT"])
@jwt_required()
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

    return jsonify(message="Label updated successfully", label=label_schema.dump(label))


# DELETE route endpoint to delete label from database
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

    return jsonify(message="Label deleted successfully", label=label_schema.dump(label))
