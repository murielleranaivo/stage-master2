from pyasn1.type import univ, namedtype

from tap_records.basic_call_information import BasicCallInformation
from tap_records.basic_service_used_list import BasicServiceUsedList
from tap_records.equipment_identifier import EquipmentIdentifier
from tap_records.location_information import LocationInformation
from tap_records.operator_spec_information import OperatorSpecInformation

class MobileCall(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('BasicCallInformation', BasicCallInformation()),
        namedtype.NamedType('LocationInformation', LocationInformation()),
        namedtype.NamedType('EquipmentIdentifier', EquipmentIdentifier()),
        namedtype.NamedType('BasicServiceUsedList', BasicServiceUsedList()),
        namedtype.NamedType('OperatorSpecInformation', OperatorSpecInformation())
    )