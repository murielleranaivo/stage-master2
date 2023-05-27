from pyasn1.type import univ, namedtype

class TimeStamp(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('LocalTimeStamp', univ.Integer()),
        namedtype.OptionalNamedType('UtcTimeOffset', univ.Integer()),
        namedtype.OptionalNamedType('UtcTimeOffsetCode', univ.Integer())
    )
