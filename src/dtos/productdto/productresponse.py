from marshmallow import Schema, fields


class ProductResponse(Schema):

    message = fields.Str()
    product_id = fields.Str()
    added_at = fields.DateTime()
    image_url = fields.Str()