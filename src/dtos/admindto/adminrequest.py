from marshmallow import Schema, validate, fields


class AdminRequest(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=5))