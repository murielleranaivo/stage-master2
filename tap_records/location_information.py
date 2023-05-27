from pyasn1.type import univ, namedtype
from tap_records.basic_service_used_list import BasicServiceUsedList

from tap_records.equipment_identifier import EquipmentIdentifier
from tap_records.network_location import NetworkLocation
from tap_records.operator_spec_information import OperatorSpecInformation

class LocationInformation(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('networkLocation', NetworkLocation()),
        namedtype.NamedType('equipmentIdentifier', EquipmentIdentifier()),
        namedtype.NamedType('basicServiceUsedList', BasicServiceUsedList()),
        namedtype.NamedType('operatorSpecInformation', OperatorSpecInformation())
    )

