from main import db

class Musician(db.Model):
    __tablename__= "musicians"
    
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    profession = db.Column(db.String(), nullable=False)
    phone_number = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    label_id = db.Column(db.Integer, db.ForeignKey("labels.id"), default=None)

    credits = db.relationship(
        "Credit",
        backref="musician",
        cascade="all, delete"
    )


