from pyasn1.type import univ, namedtype

class EquipmentIdentifier(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('imei', univ.OctetString())
    )

