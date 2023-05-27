from pyasn1.type import univ, namedtype
from tap_records.time_stamp import TimeStamp

class ChargeDetail(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('ChargeType', univ.Integer()),
        namedtype.NamedType('Charge', univ.Integer()),
        namedtype.NamedType('ChargedUnits', univ.Integer()),
        namedtype.NamedType('ChargeDetailTimeStamp', TimeStamp())
    )