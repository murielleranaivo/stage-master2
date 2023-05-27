from pyasn1.type import univ, namedtype, char

class SimChargeableSubscriber(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('imsi', char.VisibleString()),
        namedtype.NamedType('msisdn', char.VisibleString())
    )