from marshmallow import fields, Schema


class HealthSchema(Schema):
    status = fields.String()
