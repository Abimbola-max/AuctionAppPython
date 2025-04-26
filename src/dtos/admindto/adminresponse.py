from marshmallow import Schema, fields


class AdminResponse(Schema):

    id = fields.Str(attribute="id")
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
