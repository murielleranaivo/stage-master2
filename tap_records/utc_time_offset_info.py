

class UtcTimeOffsetInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('utcTimeOffset', univ.Integer()),
        namedtype.NamedType('timezone', univ.Integer())
    )

