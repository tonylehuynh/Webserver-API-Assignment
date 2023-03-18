from flask import Blueprint, jsonify, request, abort
from main import db
from models.credits import Credit
from schemas.credit_schema import credit_schema
from flask_jwt_extended import jwt_required
from functions import check_admin, validate_string_field
import datetime


credits = Blueprint('credits', __name__, url_prefix="/credits")


# PUT route endpoint to update credits as admin
@credits.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_credit(id):
    credit_fields = credit_schema.load(request.json)
    # Ensure musician user is admin
    check_admin()
    # Find the credit
    credit = Credit.query.filter_by(id=id).first()
    if not credit:
        return abort(400, description="Credit id does not exist")

    # Update credit details with new provided values
    if "description" in credit_fields:
        credit.description = validate_string_field(
            credit_fields, "description")
    # validate contribution_date if provided
    contribution_date = credit_fields.get("contribution_date")
    if contribution_date:
        try:
            contribution_date = datetime.datetime.strptime(
                contribution_date, "%Y-%m-%d")
        except (ValueError, TypeError):
            return abort(400, description="Invalid date format for contribution_date. Use YYYY-MM-DD format.")
        credit.contribution_date = contribution_date

    db.session.commit()

    return jsonify(message="Credit updated successfully", credit=credit_schema.dump(credit))


# DELETE route endpoint to delete credit from database
@credits.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_credit(id):
    # Ensure musician is admin
    check_admin()
    # Find the credit
    credit = Credit.query.filter_by(id=id).first()
    if not credit:
        return abort(400, description="Credit id does not exist")

    db.session.delete(credit)
    db.session.commit()

    return jsonify(message="Credit deleted successfully", credit=credit_schema.dump(credit))
