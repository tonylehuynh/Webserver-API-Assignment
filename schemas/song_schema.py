from main import ma


class SongSchema(ma.Schema):
    class Meta:
        fields = ['id', 'title', 'genre', 'duration', 'date']


song_schema = SongSchema()
songs_schema = SongSchema(many=True)
