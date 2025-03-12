from marshmallow import Schema, fields, ValidationError

class BaseSchema(Schema):
    # traceId = fields.String(required=True)
    def add(self):
        sample = {
            "traceId": "TIPS15654",
            "partner": "TIPS",
            "affiliate": "PH",
            "clientGroup": "GDEV",
            "clientId": "0001",
            "debtorAccountId": "TIPS1",
            "clientPaymentId": "5654",
            "provider": "BOA",
            "method": "RECIPIENTSELECT",
            "purpose": "CLAIM_PAYMENT",
            "requestedExecutionTime": "2025-03-11T10:21:05.737Z",
            "payeePaymentReference": "25000413-01",
            "memo": "25000413-01 ",
            "description": None,
            "currency": "USD",
            "amount": "300.00",
            "amountScale": 0,
            "roundingMode": "HALF_UP",
            "recipientExternalId": "91654",
            "recipientGivenName": "Test",
            "recipientFamilyName": "Test",
            "recipientAdditionalName": None,
            "recipientFullName": "Test Test",
            "deliveryEmail": "sdongare@extern.csatp.com",
            "deliveryCellPhone": None,
            "deliveryAddressOne": "6000 Chimney Rock Rd",
            "deliveryAddressTwo": "Gulfton Harris County 4000",
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
                    else fields.Boolean(required=True)