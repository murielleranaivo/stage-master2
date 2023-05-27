from pyasn1.type import univ, namedtype

class CallEventTimeStamp(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('LocalTimeStamp', univ.Integer()),
        namedtype.NamedType('UtcTimeOffsetCode', univ.Integer()),
    )

