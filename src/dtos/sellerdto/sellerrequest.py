from dataclasses import dataclass

from marshmallow import fields, Schema, validate

@dataclass
class SellerRequestDTO(Schema):

    first_name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    last_name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))
    user_type = fields.Str(required=True, validate=validate.OneOf(["seller", "bidder", "admin"]))

