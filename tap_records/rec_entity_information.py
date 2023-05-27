from pyasn1.type import univ, namedtype, char

class RecEntityInformation(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('RecEntityCode', univ.Integer()),
        namedtype.NamedType('RecEntityType', char.VisibleString()),
        namedtype.NamedType('RecEntityId', univ.Integer()),
    )