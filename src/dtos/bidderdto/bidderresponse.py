from marshmallow import Schema, fields


class BidderResponseDTO(Schema):

    message = fields.Str()
    bidder_id = fields.Str()