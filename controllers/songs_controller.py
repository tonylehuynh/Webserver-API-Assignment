from flask import Blueprint, jsonify, request, abort
from main import db
from models.songs import Song
from schemas.song_schema import song_schema, songs_schema
from flask_jwt_extended import jwt_required
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

    return jsonify(song_schema.dump(new_song))


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

    return jsonify(song_schema.dump(song))


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

    return jsonify(song_schema.dump(song))
