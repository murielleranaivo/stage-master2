from pyasn1.type import univ, namedtype

class UtcTimeOffsetInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('UtcTimeOffsetCode', univ.Integer()),
        namedtype.NamedType('UtcTimeOffset', univ.Integer())
    )

