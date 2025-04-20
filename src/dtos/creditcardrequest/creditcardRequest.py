from datetime import datetime

from marshmallow import fields, Schema, validate, validates, ValidationError

from src.data.models.validator import Validator


class CreditCardRequest(Schema):
    card_cvv = fields.Str(required=True, validate=validate.Length(equal=3),data_key="cardCVV")
    card_number = fields.Str(required=True, validate=validate.Length(min=13, max=18), data_key="cardNumber")
    expiry_date = fields.Str(
        required=True,
        validate=validate.Regexp(r"^(0[1-9]|1[0-2])\/?([0-9]{2})$"), data_key="expiryDate"
    )
    card_type = fields.Str(required=True, validate=validate.OneOf(["VISA_CARD", "MASTER_CARD", "VERVE"]), data_key="cardType")

    @validates("expiry_date")
    def validate_expiry_date(self, value):
        try:
            value = value.replace("/", "")
            month = int(value[:2])
            year = int(value[2:])
            year += 2000
            expiry = datetime(year, month, 1)
            now = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            if expiry < now:
                raise ValidationError("Credit card expiry date must be in the future.")
        except Exception:
            raise ValidationError("Invalid expiry date format.")