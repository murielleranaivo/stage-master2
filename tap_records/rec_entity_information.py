from pyasn1.type import univ, namedtype

class RecEntityInformation(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('RecEntityCode', univ.Integer()),
        namedtype.NamedType('RecEntityType', univ.Integer()),
        namedtype.NamedType('RecEntityId', univ.Integer()),
    )