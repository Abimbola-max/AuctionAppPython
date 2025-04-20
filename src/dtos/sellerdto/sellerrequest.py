from dataclasses import dataclass

from marshmallow import fields, Schema, validate


class SellerRequestDTO(Schema):

    first_name = fields.Str(required=True, validate=validate.Length(min=3, max=20), data_key="firstName")
    last_name = fields.Str(required=True, validate=validate.Length(min=3, max=20), data_key="lastName")
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))
    account_number = fields.Str(required=True, validate=validate.Length(min=10, max=10), data_key="accountNumber")
    bank_name = fields.Str(required=True, validate=validate.Length(min=3, max=20), data_key="bankName")

