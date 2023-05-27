from pyasn1.type import univ, namedtype

from tap_records.currency_conversion_info import CurrencyConversionInfo

class AccountingInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('localCurrency', univ.OctetString()),
        namedtype.NamedType('tapCurrency', univ.OctetString()),
        namedtype.NamedType('currencyConversionInfo', CurrencyConversionInfo()),
        namedtype.NamedType('tapDecimalPlaces', univ.Integer())
    )
