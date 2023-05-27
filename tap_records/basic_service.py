from pyasn1.type import univ, namedtype

from tap_records.service_code import ServiceCode

class BasicService(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('ServiceCode', ServiceCode())
    )