from pyasn1.type import univ, namedtype

class TimeStamp(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('localTimeStamp', univ.OctetString()),
        namedtype.NamedType('utcTimeOffset', univ.OctetString())
    )
