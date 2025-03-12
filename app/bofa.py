from marshmallow import Schema, fields, ValidationError

class BaseSchema(Schema):
    # traceId = fields.String(required=True)
    def add(self):
        sample = {
            "traceId": "dummy",
            "partner": "dummy",
            "affiliate": "dummy",
            "clientGroup": "dummy",
            "clientId": "0001",
            "debtorAccountId": "dummy",
            "clientPaymentId": "dummy",
            "provider": "BOA",
            "method": "RECIPIENTSELECT",
            "purpose": "CLAIM_PAYMENT",
            "requestedExecutionTime": "2025-03-11T10:21:05.737Z",
            "payeePaymentReference": "dummy",
            "memo": "dummy ",
            "description": None,
            "currency": "USD",
            "amount": "300.00",
            "amountScale": 0,
            "roundingMode": "HALF_UP",
            "recipientExternalId": "dummy",
            "recipientGivenName": "Test",
            "recipientFamilyName": "Test",
            "recipientAdditionalName": None,
            "recipientFullName": "Test Test",
            "deliveryEmail": "dummy@dummy.com",
            "deliveryCellPhone": None,
            "deliveryAddressOne": "dummy street",
            "deliveryAddressTwo": "dummy street",
            "deliveryCity": "Houston",
            "deliveryState": "TX",
            "deliveryPostalCode": "77081",
            "deliveryCountry": "US"
        }
        for k, v in sample.items():
            self.fields[k] = self.load_fields[k] = self.declared_fields[k] = fields.String(required=True) \
                if isinstance(v, str) \
                    else fields.Integer(required=True) if isinstance(v, int) \
                    else fields.Float(required=True) if isinstance(v, float) \
                    else fields.Boolean(required=True) if isinstance(v, bool) \
                    else fields.String(required=False, allow_none=True)
