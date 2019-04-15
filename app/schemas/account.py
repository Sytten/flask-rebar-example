from marshmallow import fields, Schema
from flask_rebar import RequestSchema


class CreateAccountSchema(RequestSchema):
    email = fields.String(required=True)
    country = fields.String(required=True)
    default_currency = fields.String(required=True)


class AccountSchema(Schema):
    id = fields.String()
    email = fields.String()
    country = fields.String()
    default_currency = fields.String()
