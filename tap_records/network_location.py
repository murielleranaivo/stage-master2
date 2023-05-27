from pyasn1.type import univ, namedtype

class NetworkLocation(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('RecEntityCode', univ.Integer()),
        namedtype.NamedType('CallReference', univ.Integer()),
        namedtype.NamedType('LocationArea', univ.Integer()),
        namedtype.NamedType('CellId', univ.Integer()),
    )
