from pyasn1.type import univ, namedtype, char

class Destination(univ.Sequence):
    component = namedtype.NamedTypes(
        namedtype.NamedType('CalledNumber', char.VisibleString()),
        namedtype.OptionalNamedType('DialledDigits', char.VisibleString()),
        namedtype.OptionalNamedType('SMSDestinationNumber', char.VisibleString()),
    )