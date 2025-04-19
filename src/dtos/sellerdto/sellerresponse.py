from marshmallow import Schema


class SellerResponseDTO(Schema):

    message: str
    seller_id: