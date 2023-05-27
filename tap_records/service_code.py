from pyasn1.type import univ, namedtype

class ServiceCode(univ.Sequence):
    componentType=namedtype.NamedTypes(
        namedtype.NamedType('TeleServiceCode', univ.Integer())
    )