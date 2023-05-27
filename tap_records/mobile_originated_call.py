from pyasn1.type import univ, namedtype

from tap_records.basic_call_information import BasicCallInformation
from tap_records.location_information import LocationInformation

class MobileOriginatedCall(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('basicCallInformation', BasicCallInformation()),
        namedtype.NamedType('locationInformation', LocationInformation())
    )