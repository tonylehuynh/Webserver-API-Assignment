from flask import Blueprint, jsonify, request, abort
from main import db
from models.songs import Song
from models.credits import Credit
from models.musicians import Musician
from schemas.song_schema import song_schema, songs_schema
from schemas.credit_schema import credit_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from functions import check_admin, validate_string_field
import datetime


songs = Blueprint('songs', __name__, url_prefix="/songs")


# GET route endpoints to query songs
@songs.route("/", methods=["GET"])
# Function to get list of all songs
def get_songs():
    songs_list = Song.query.all()
    result = songs_schema.dump(songs_list)
    return jsonify(result)


# POST route endpoint
@songs.route("/create", methods=["POST"])
@jwt_required()
# Function to create new record song
def create_song():
    song_fields = song_schema.load(request.json)
    # Check if song already exists
    title = validate_string_field(song_fields, "title")
    song = Song.query.filter_by(title=title).first()
    if song:
        return abort(400, description="Song already exists.")

    # Add new song
    new_song = Song()
    new_song.title = validate_string_field(song_fields, "title")
    new_song.genre = validate_string_field(song_fields, "genre")

    # validate duration if provided
    duration = song_fields.get("duration")
    if duration:
        try:
            duration = datetime.datetime.strptime(duration, "%H:%M:%S")
        except (ValueError, TypeError):
            return abort(400, description="Invalid time format for duration. Use HH:MM:SS format.")

    # validate date_finished if provided
    date_finished = song_fields.get("date_finished")
    if date_finished:
        try:
            date_finished = datetime.datetime.strptime(
                date_finished, "%Y-%m-%d")
        except (ValueError, TypeError):
            return abort(400, description="Invalid date format for date_finished. Use YYYY-MM-DD format.")

    new_song.duration = duration
    new_song.date_finished = date_finished

    db.session.add(new_song)
    db.session.commit()

    return jsonify(message="Song created successfully", song=song_schema.dump(new_song))


# PUT route endpoint
@songs.route("/<int:id>/", methods=["PUT"])
@jwt_required()
# Function to update song
def update_song(id):
    song_fields = song_schema.load(request.json)
    # Ensure musician user is admin
    check_admin()
    # Find the song
    song = Song.query.filter_by(id=id).first()
    if not song:
        return abort(400, description="Song id does not exist")
    # Update song details with new provided values
    if "title" in song_fields:
        song.title = validate_string_field(song_fields, "title")
    if "genre" in song_fields:
        song.genre = validate_string_field(song_fields, "genre")
    # validate duration if provided
    duration = song_fields.get("duration")
    if duration:
        try:
            duration = datetime.datetime.strptime(duration, "%H:%M:%S")
        except (ValueError, TypeError):
            return abort(400, description="Invalid time format for duration. Use HH:MM:SS format.")
        song.duration = duration
    # validate date_finished if provided
    date_finished = song_fields.get("date_finished")
    if date_finished:
        try:
            date_finished = datetime.datetime.strptime(
                date_finished, "%Y-%m-%d")
        except (ValueError, TypeError):
            return abort(400, description="Invalid date format for date_finished. Use YYYY-MM-DD format.")
        song.date_finished = date_finished

    db.session.commit()

    return jsonify(message="Song updated successfully", song=song_schema.dump(song))


# DELETE route endpoint to delete song from database
@songs.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_song(id):
    # Ensure musician is admin
    check_admin()
    # Find the song
    song = Song.query.filter_by(id=id).first()
    if not song:
        return abort(400, description="Song id does not exist")

    db.session.delete(song)
    db.session.commit()

    return jsonify(message="Song deleted successfully", song=song_schema.dump(song))


# CREDITS SECTION BELOW - CREATE NEW CREDIT WITH SONG ID & MUSICIAN ID ATTACHED


# POST route endpoint to create new song credit. Otherwise update song credit if already exists
@songs.route("/<int:id>/credit", methods=["POST"])
@jwt_required()
def create_credit(id):
    credit_fields = credit_schema.load(request.json)

    musician_id = get_jwt_identity()
    musician = Musician.query.get(musician_id)
    if not musician:
        return abort(401, description="Invalid musician id")

    # Find the Song
    song = Song.query.filter_by(id=id).first()
    if not song:
        return abort(400, description="Song id does not exist")

    # Check if musician is already credited for this song
    existing_credit = Credit.query.filter_by(
        musician_id=musician_id, song_id=id).first()
    if existing_credit:
        # Update existing credit if credit already exists
        existing_credit.description = validate_string_field(
            credit_fields, "description")

        contribution_date = credit_fields.get("contribution_date")
        try:
            contribution_date = datetime.datetime.strptime(
                contribution_date, "%Y-%m-%d")
        except (ValueError, TypeError):
            return abort(400, description="Invalid date format provided or not found for contribution_date. Please provide contribution_date field and use YYYY-MM-DD format.")

        existing_credit.contribution_date = contribution_date
        db.session.commit()

        return jsonify(credit_schema.dump(existing_credit))

    # Add new credit if credit does not exist for song and musician id
    new_credit = Credit()
    new_credit.song_id = id
    new_credit.musician_id = musician_id
    new_credit.description = validate_string_field(
        credit_fields, "description")

    contribution_date = credit_fields.get("contribution_date")
    try:
        contribution_date = datetime.datetime.strptime(
            contribution_date, "%Y-%m-%d")
    except (ValueError, TypeError):
        return abort(400, description="Invalid date format provided or not found for contribution_date. Please provide contribution_date field and use YYYY-MM-DD format.")
    new_credit.contribution_date = contribution_date

    db.session.add(new_credit)
    db.session.commit()

    return jsonify(message="Credit for song created successfully", credit=credit_schema.dump(new_credit))
