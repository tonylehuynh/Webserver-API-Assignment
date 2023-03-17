from main import ma


class CreditSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "description", "contribution_date")


credit_schema = CreditSchema()
credits_schema = CreditSchema(many=True)
