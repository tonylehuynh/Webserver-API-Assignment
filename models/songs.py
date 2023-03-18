from main import db

class Song(db.Model):
    __tablename__= "songs"

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(), nullable=False)
    genre = db.Column(db.String(), nullable=False)
    duration = db.Column(db.Time())
    date_finished = db.Column(db.Date())

    credits = db.relationship(
        "Credit",
        backref="song",
        cascade="all, delete"
    )
