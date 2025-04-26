from marshmallow import Schema, validate, fields

from src.data.models.productphase import ProductPhase


class ProductRequest(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    description = fields.Str(required=True, validate=validate.Length(min=3, max=500))
    seller_id = fields.Str(required=True, data_key="sellerID")
    bid_minimum_price = fields.Float(required=True, validate=validate.Range(min=0.01), data_key="bidMinimumPrice")
    # product_phase = fields.Str(validate=validate.OneOf([phase.value for phase in ProductPhase]))
    # bid_start_time = fields.Str(required=True, data_key="bidStartTime")
    # bid_end_time = fields.Str(required=True, data_key="bidEndTime")