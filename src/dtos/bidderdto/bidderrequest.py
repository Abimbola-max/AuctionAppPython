from marshmallow import Schema, fields, validate

from src.dtos.creditcardrequest.creditcardrequest import CreditCardRequest


class BidderRequestDTO(Schema):

    first_name = fields.Str(required=True, validate=validate.Length(min=3, max=20), data_key="firstName")
    last_name = fields.Str(required=True, validate=validate.Length(min=3, max=20), data_key="lastName")
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))
    credit_card_information = fields.Nested(CreditCardRequest, required=True,data_key="creditCardInformation")