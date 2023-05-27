from pyasn1.type import univ, namedtype

class CallEventTimeStamp(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('localTimeStamp', univ.Integer()),
        namedtype.NamedType('utcTimeOffsetCode', univ.Integer()),
    )

