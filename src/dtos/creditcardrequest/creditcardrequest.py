from datetime import datetime

from marshmallow import fields, Schema, validate, validates, ValidationError



class CreditCardRequest(Schema):
    card_cvv = fields.Str(required=True, validate=validate.Length(equal=3), data_key="cardCVV")
    card_number = fields.Str(required=True, validate=validate.Length(min=13, max=18), data_key="cardNumber")
    expiry_date = fields.Str(
        required=True,
        validate=[validate.Regexp(r"^(0[1-9]|1[0-2])\/?([0-9]{2})$")],
        data_key="expiryDate"
    )
    card_type = fields.Str(required=True, validate=validate.OneOf(["VISA_CARD", "MASTER_CARD", "VERVE"]), data_key="cardType")