from marshmallow import fields, Schema

class BidResponse(Schema):

    message = fields.String()
    product_id = fields.String()
    amount = fields.Integer()
    bid_time = fields.DateTime(format='iso')
    bidder_id = fields.Str()
