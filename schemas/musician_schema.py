from main import ma
from marshmallow.validate import Length


class MusicianSchema(ma.Schema):
    class Meta:
        fields = ['id', 'first_name', 'last_name', 'profession',
                  'phone_number', 'email', 'password', 'admin', "label_id"]
        load_only = ['password', 'admin']
    # Set the password's length to a minimum of 6 characters.
    password = ma.String(validate=Length(
        min=6, error="Password must be at least 6 characters long"))


musician_schema = MusicianSchema()
musicians_schema = MusicianSchema(many=True)
