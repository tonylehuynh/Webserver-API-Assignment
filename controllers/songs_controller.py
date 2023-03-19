from flask import Blueprint, jsonify, request, abort
from main import db
from models.songs import Song
from models.credits import Credit
from models.musicians import Musician
from schemas.song_schema import song_schema, songs_schema
from schemas.credit_schema import credit_schema, credits_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from functions import check_admin, validate_string_field
from datetime import datetime, timedelta


songs = Blueprint('songs', __name__, url_prefix="/songs")


# GET ROUTE endpoints

# Retrieves all songs from database
@songs.route("/", methods=["GET"])
def get_songs():
    songs_list = Song.query.all()
    result = songs_schema.dump(songs_list)
    return jsonify(result)


# Retrieves all songs from the database with the specified genre provided in the URL
@songs.route("/<genre>", methods=["GET"])
def get_songs_by_genre(genre):
    valid_genres = db.session.query(Song.genre).distinct().all()
    if (genre,) not in valid_genres:
        return jsonify({"message": f"Genre '{genre}' does not exist. Please note genre is also case sensitive."})
    songs_list = Song.query.filter_by(genre=genre).all()
    result = songs_schema.dump(songs_list)
    return jsonify(result)


# Retrieves all songs from the database with the specified date_finished (year) provided in the URL
@songs.route("/year/<int:year>", methods=["GET"])
def get_songs_by_year(year):
    try:
        start_date = datetime(year=year, month=1, day=1).date()
        end_date = datetime(year=year+1, month=1, day=1).date()
    except ValueError:
        return jsonify({"message": f"Invalid year: {year}"})

    songs_list = Song.query.filter(
        Song.date_finished >= start_date, Song.date_finished < end_date).all()
    result = songs_schema.dump(songs_list)
    return jsonify(result)


# Retrieves all songs from the database with the specified duration (minutes) provided in the URL
@songs.route("/duration/<int:minutes>", methods=["GET"])
def get_songs_by_duration(minutes):
    # Convert minutes to a timedelta object
    duration = timedelta(minutes=minutes)

    # Query for songs with duration within the specified range
    songs_list = Song.query.filter(
        Song.duration >= duration,
        Song.duration < duration + timedelta(minutes=1)
    ).all()

    # Dump the list of songs to JSON and return the response
    result = songs_schema.dump(songs_list)
    return jsonify(result)


# Retrieves all credits associated with a specified song ID provided in the URL
@songs.route("/<int:song_id>/credits", methods=["GET"])
def get_song_credits(song_id):
    # Query for the song by ID
    song = Song.query.get(song_id)
    # If song doesn't exist, return 404
    if not song:
        return jsonify({"message": "Song not found"}), 404
    # Get the list of credits for the song
    credits_list = Credit.query.filter_by(song_id=song.id).all()
    # Create a dictionary with the song title and credits
    song_credits = {
        "song_title": song.title,
        "credits": credits_schema.dump(credits_list)
    }
    return jsonify(song_credits)


# POST route endpoint. This route creates a new song in the database with the fields provided in the request.
@songs.route("/create", methods=["POST"])
@jwt_required()
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
            duration = datetime.strptime(duration, "%H:%M:%S")
        except (ValueError, TypeError):
            return abort(400, description="Invalid time format for duration. Use HH:MM:SS format.")

    # validate date_finished if provided
    date_finished = song_fields.get("date_finished")
    if date_finished:
        try:
            date_finished = datetime.strptime(
                date_finished, "%Y-%m-%d")
        except (ValueError, TypeError):
            return abort(400, description="Invalid date format for date_finished. Use YYYY-MM-DD format.")

    new_song.duration = duration
    new_song.date_finished = date_finished

    db.session.add(new_song)
    db.session.commit()

    return jsonify(message="Song created successfully", song=song_schema.dump(new_song))


# PUT route endpoint. This route updates an existing song in the database with the fields provided in the request.
@songs.route("/<int:id>/", methods=["PUT"])
@jwt_required()
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
            duration = datetime.strptime(duration, "%H:%M:%S")
        except (ValueError, TypeError):
            return abort(400, description="Invalid time format for duration. Use HH:MM:SS format.")
        song.duration = duration
    # validate date_finished if provided
    date_finished = song_fields.get("date_finished")
    if date_finished:
        try:
            date_finished = datetime.strptime(
                date_finished, "%Y-%m-%d")
        except (ValueError, TypeError):
            return abort(400, description="Invalid date format for date_finished. Use YYYY-MM-DD format.")
        song.date_finished = date_finished

    db.session.commit()

    return jsonify(message="Song updated successfully", song=song_schema.dump(song))


# DELETE route endpoint. This route deletes a specified song from the database, with the song id provided in the URL.
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


# POST route endpoint.
# This route creates a new credit associated with a specified song and musician in the database. Otherwise update song credit if it already exists.
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
            contribution_date = datetime.strptime(
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
        contribution_date = datetime.strptime(
            contribution_date, "%Y-%m-%d")
    except (ValueError, TypeError):
        return abort(400, description="Invalid date format provided or not found for contribution_date. Please provide contribution_date field and use YYYY-MM-DD format.")
    new_credit.contribution_date = contribution_date

    db.session.add(new_credit)
    db.session.commit()

    return jsonify(message="Credit for song created successfully", credit=credit_schema.dump(new_credit))
