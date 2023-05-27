from pyasn1.type import univ, namedtype

from tap_records.operator_spec_information import OperatorSpecInformation
from tap_records.time_stamp import TimeStamp

class AuditControlInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('EarliestCallTimeStamp', TimeStamp()),
        namedtype.NamedType('LatestCallTimeStamp', TimeStamp()),
        namedtype.NamedType('TotalCharge', univ.Integer()),
        namedtype.NamedType('TotalTaxValue', univ.Integer()),
        namedtype.NamedType('TotalDiscountValue', univ.Integer()),
        namedtype.NamedType('CallEventDetailsCount', univ.Integer()),
        namedtype.NamedType('OperatorSpecInformation', OperatorSpecInformation())
    )