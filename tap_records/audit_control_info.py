from pyasn1.type import univ, namedtype
from tap_records.call_event_time_stamp import CallEventTimeStamp

from tap_records.operator_spec_information import OperatorSpecInformation

class AuditControlInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('earliestCallTimeStamp', CallEventTimeStamp()),
        namedtype.NamedType('latestCallTimeStamp', CallEventTimeStamp()),
        namedtype.NamedType('totalCharge', univ.Integer()),
        namedtype.NamedType('totalTaxValue', univ.Integer()),
        namedtype.NamedType('totalDiscountValue', univ.Integer()),
        namedtype.NamedType('callEventDetailsCount', univ.Integer()),
        namedtype.NamedType('operatorSpecInformation', OperatorSpecInformation())
    )