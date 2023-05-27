from pyasn1.type import univ, namedtype, char

class OperatorSpecInformation(univ.SequenceOf):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('OperatorSpecInformation', char.VisibleString()),
    )