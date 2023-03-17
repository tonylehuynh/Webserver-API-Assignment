from main import db

class Label(db.Model):
    __tablename__= "labels"
    
    id = db.Column(db.Integer,primary_key=True)
    
    name = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), nullable=False)
    
