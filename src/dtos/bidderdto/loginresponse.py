from marshmallow import Schema, fields


class LoginResponse(Schema):

    message = fields.Str()
    first_name = fields.Str()
    token = fields.Str()
    bidder_id = fields.Str()