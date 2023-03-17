from main import ma
from marshmallow.validate import Length


class MusicianSchema(ma.Schema):
    class Meta:
        fields = ['id', 'first_name', 'last_name', 'profession',
                  'phone_number', 'email', 'password', 'admin']
        load_only = ['password', 'admin']
    # Set the password's length to a minimum of 6 characters
    password = ma.String(validate=Length(min=6))


musician_schema = MusicianSchema()
musicians_schema = MusicianSchema(many=True)
