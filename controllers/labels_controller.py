from flask import Blueprint, jsonify, request, abort
from main import db
from models.labels import Label
from models.musicians import Musician
from schemas.label_schema import label_schema, labels_schema
from flask_jwt_extended import jwt_required, get_jwt_identity


labels = Blueprint('labels', __name__, url_prefix="/labels")


@labels.route("/", methods=["GET"])
# Function to get list of all record labels
def get_labels():
    labels_list = Label.query.all()
    result = labels_schema.dump(labels_list)
    return jsonify(result)


# POST route endpoint to create a new label only if musician is admin
@labels.route("/create", methods=["POST"])
@jwt_required()
def create_label():
    label_fields = label_schema.load(request.json)

    # Ensure musician is admin before being able to create new label
    musician_id = get_jwt_identity()
    musician = Musician.query.get(musician_id)
    if not musician:
        return abort(401, description="Invalid musician. Please provide valid access token")
    if not musician.admin:
        return abort(401, description="Unauthorised musician. Not admin")

    # Check if label already exists
    label = Label.query.filter_by(name=label_fields["name"]).first()
    if label:
        return abort(400, description="Label already exists.")

    # Add new label
    new_label = Label()
    new_label.name = label_fields["name"]
    new_label.type = label_fields["type"]
    db.session.add(new_label)
    db.session.commit()

    return jsonify(label_schema.dump(new_label))
