from pyasn1.type import univ, namedtype, char

from tap_records.currency_conversion_info import CurrencyConversionInfo

class AccountingInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('LocalCurrency', char.VisibleString()),
        namedtype.NamedType('TapCurrency', char.VisibleString()),
        namedtype.NamedType('CurrencyConversionInfo', CurrencyConversionInfo()),
        namedtype.NamedType('TapDecimalPlaces', univ.Integer())
    )
