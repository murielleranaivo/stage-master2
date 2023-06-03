from pyasn1.type import univ, namedtype, char

class TimeStamp(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('LocalTimeStamp', univ.Integer()),
        namedtype.OptionalNamedType('UtcTimeOffset', char.VisibleString()),
        namedtype.OptionalNamedType('UtcTimeOffsetCode', univ.Integer())
    )
