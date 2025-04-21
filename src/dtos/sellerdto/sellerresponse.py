
from marshmallow import Schema, fields

class SellerResponseDTO(Schema):

    token = fields.Str()
    message = fields.Str()
    seller_id = fields.Str()