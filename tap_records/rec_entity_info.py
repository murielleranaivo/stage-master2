
class RecEntityInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('entityId', univ.Integer()),
        namedtype.NamedType('entityName', univ.OctetString())
    )