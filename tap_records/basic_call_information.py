from pyasn1.type import univ, namedtype

from tap_records.call_event_time_stamp import CallEventTimeStamp
from tap_records.call_originator import CallOriginator
from tap_records.chargeable_subscriber import ChargeableSubscriber

class BasicCallInformation(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('ChargeableSubscriber', ChargeableSubscriber()),
        namedtype.NamedType('CallOriginator', CallOriginator()),
        namedtype.NamedType('CallEventStartTimeStamp', CallEventTimeStamp()),
        namedtype.NamedType('TotalCallEventDuration', univ.Integer())
    )

