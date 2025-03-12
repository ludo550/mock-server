from marshmallow import Schema, fields, ValidationError

class BaseSchema(Schema):
    # traceId = fields.String(required=True)
    def add(self):
        sample = {
                    "paymentIdentification": {
                        "instructionIdentification": "test-01",
                        "endToEndIdentification": "TIPS15660"
                    },
                    "paymentMethod": "TRF",
                    "requestedExecutionDate": "2025-03-12",
                    "amount": {
                        "value": "20.00"
                    },
                    "debtorAccount": {
                        "identification": "TIPS1-ACCT-NUM",
                        "currency": "USD"
                    },
                    "debtorAgent": None,
                    "debtor": {
                        "name": "TBD",
                        "type": "TBD",
                        "postalAddress": {
                            "addressLine": [
                                "AddressOne",
                                "AddressTwo"
                            ],
                            "city": "TBD-City",
                            "countrySubDivision": "CA",
                            "postalCode": "92121",
                            "country": "US"
                        },
                        "contactDetails": {
                            "phoneNumber": None,
                            "emailAddress": "TBD"
                        },
                        "identifiers": [
                            {
                                "identification": "TDB1",
                                "schemeName": "TDB1"
                            },
                            {
                                "identification": "TDB2",
                                "schemeName": "TDB2"
                            }
                        ]
                    },
                    "ultimateDebtor": None,
                    "creditor": {
                        "name": "Test Test",
                        "type": "IND",
                        "postalAddress": {
                            "addressLine": [
                                "6000 Chimney Rock Rd",
                                "Gulfton Harris County 4000"
                            ],
                            "city": "Houston",
                            "countrySubDivision": "TX",
                            "postalCode": "77081",
                            "country": "US"
                        },
                        "contactDetails": {
                            "mobileNumber": None,
                            "emailAddress": "test@extern.csatp.com",
                            "name": "Test Test"
                        }
                    },
                    "creditorAccount": {
                        "currency": "USD"
                    },
                    "paymentType": {
                        "localInstrument": "CHOICE",
                        "categoryOfPurpose": "CLAIM_PAYMENT"
                    },
                    "checkInstruction": {
                        "memoField": "test-01 "
                    },
                    "unstructuredRemittance": "test-01 "
                }
        for k, v in sample.items():
            self.fields[k] = self.load_fields[k] = self.declared_fields[k] = fields.String(required=True) \
                if isinstance(v, str) \
                    else fields.Integer(required=True) if isinstance(v, int) \
                    else fields.Float(required=True) if isinstance(v, float) \
                    else fields.Boolean(required=True) if isinstance(v, bool) \
                    else fields.String(required=False, allow_none=True)
