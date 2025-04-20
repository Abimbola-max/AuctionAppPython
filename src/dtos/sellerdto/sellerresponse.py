
from marshmallow import Schema, fields

class SellerResponseDTO(Schema):

    message = fields.Str()
    seller_id = fields.Str()