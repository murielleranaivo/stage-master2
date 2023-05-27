from pyasn1.type import univ, namedtype, char

class CallOriginator(univ.Sequence):
    component = namedtype.NamedType(
        namedtype.NamedType(('callingNumber', char.VisibleString()))
    )
