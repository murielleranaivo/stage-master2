from pyasn1.type import univ, namedtype

from tap_records.network_location import NetworkLocation

class LocationInformation(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('NetworkLocation', NetworkLocation())
    )

