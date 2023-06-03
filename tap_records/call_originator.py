from pyasn1.type import univ, namedtype, char

class CallOriginator(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('CallingNumber', char.VisibleString()),
        namedtype.OptionalNamedType('SMSOriginator', char.VisibleString())
    )
