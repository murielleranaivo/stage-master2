from pyasn1.type import univ, namedtype

class CurrencyConversion(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('ExchangeRateCode', univ.Integer()),
        namedtype.NamedType('NumberOfDecimalPlaces', univ.Integer()),
        namedtype.NamedType('ExchangeRate', univ.Integer())
    )