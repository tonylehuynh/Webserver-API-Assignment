from main import db

class Song(db.Model):
    __tablename__= "songs"

    id = db.Column(db.Integer,primary_key=True)
    
    title = db.Column(db.String(), nullable=False)
    genre = db.Column(db.String())
    duration = db.Column(db.Time())
    date = db.Column(db.Date())
    
