from main import ma
from marshmallow.validate import Length
from marshmallow import validates, ValidationError


class MusicianSchema(ma.Schema):
    class Meta:
        fields = ['id', 'first_name', 'last_name', 'profession',
                  'phone_number', 'email', 'password', 'admin', "label_id"]
        load_only = ['password', 'admin']
    # Set the password's length to a minimum of 6 characters.
    password = ma.String(validate=Length(
        min=6, error="Password must be at least 6 characters long"))
    
    @validates('admin')
    def validate_admin(self, value):
        if value not in [True, False]:
            raise ValidationError('Invalid value for admin field. Please provide a boolean value.')


musician_schema = MusicianSchema()
musicians_schema = MusicianSchema(many=True)
