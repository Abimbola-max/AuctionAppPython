from marshmallow import Schema, fields


class ProductResponse(Schema):

    message = fields.Str()
    product_id = fields.Str()
    created_at = fields.DateTime()