from marshmallow import Schema, fields, validate


class BidRequest(Schema):

    product_id = fields.String(required=True)
    amount = fields.Int(required=True, validate=validate.Range(min=100))
