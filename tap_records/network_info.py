from pyasn1.type import univ, namedtype
from tap_records.rec_entity_info import RecEntityInfo

from tap_records.utc_time_offset_info import UtcTimeOffsetInfo

class NetworkInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('utcTimeOffsetInfo', UtcTimeOffsetInfo()),
        namedtype.NamedType('recEntityInfo', RecEntityInfo())
    )