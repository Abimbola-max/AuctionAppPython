from marshmallow import Schema, fields


class BidderResponseDTO(Schema):

    token = fields.Str()
    message = fields.Str()
