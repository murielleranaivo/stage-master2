from pyasn1.type import univ, namedtype, char

class EquipmentIdentifier(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('Imei', char.VisibleString())
    )

