from pyasn1.type import univ, namedtype, char

class CallTypeGroup(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('CallTypeLevel1', univ.Integer()),
        namedtype.NamedType('CallTypeLevel2', univ.Integer()),
        namedtype.NamedType('CallTypeLevel3', univ.Integer())
    )