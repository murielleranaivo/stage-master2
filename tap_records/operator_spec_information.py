from pyasn1.type import univ, namedtype, char

class OperatorSpecInformation(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('OperatorSpecInformation', char.VisibleString()),
    )