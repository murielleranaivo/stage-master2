from pyasn1.type import univ, namedtype, char

class SimChargeableSubscriber(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('Imsi', char.VisibleString()),
        namedtype.NamedType('Msisdn', char.VisibleString())
    )