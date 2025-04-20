from marshmallow import Schema, validate, fields


class ProductRequest(Schema):

    name = fields.Str(required=True, validate=validate.Length(min=3, max=20))
    description = fields.Str(required=True, validate=validate.Length(min=3, max=20))
    seller_id = fields.Str(required=True, data_key="sellerID")
    starting_price = fields.Float(required=True, validate=validate.Range(min=2000), data_key="startingPrice")
    bid_start_time = fields.DateTime(required=True, format="%Y-%m-%d %H:%M",data_key="bidStartTime")
    bid_end_time = fields.DateTime(required=True, format="%Y-%m-%d %H:%M",data_key="bidEndTime")