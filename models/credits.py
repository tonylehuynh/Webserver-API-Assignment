from main import db

class Credit(db.Model):
    __tablename__= "credits"

    id = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.String(), nullable=False)
    contribution_date = db.Column(db.Date())

    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), nullable=False)
    musician_id = db.Column(db.Integer, db.ForeignKey("musicians.id"), nullable=False)