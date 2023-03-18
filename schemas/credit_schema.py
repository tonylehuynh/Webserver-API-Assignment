from main import ma
from marshmallow import fields



class CreditSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "description", "contribution_date", "musician_id", "musician_email", "song_id", "song_title")

    musician_id = fields.Integer(attribute="musician.id")
    musician_email = fields.String(attribute="musician.email")
    song_id = fields.Integer(attribute="song.id")
    song_title = fields.String(attribute="song.title")


credit_schema = CreditSchema()
credits_schema = CreditSchema(many=True)
