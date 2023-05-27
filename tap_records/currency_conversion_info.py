from pyasn1.type import univ, namedtype, namedval, tag

class CurrencyConversionInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('exchangeRate', univ.Real()),
        namedtype.NamedType('exchangeRateDate', univ.OctetString())
    )

