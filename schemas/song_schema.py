from main import ma


class SongSchema(ma.Schema):
    class Meta:
        fields = ['id', 'title', 'genre', 'duration', 'date_finished']


song_schema = SongSchema()
songs_schema = SongSchema(many=True)
