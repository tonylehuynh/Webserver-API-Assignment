from main import ma


class LabelSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'type']


label_schema = LabelSchema()
labels_schema = LabelSchema(many=True)
