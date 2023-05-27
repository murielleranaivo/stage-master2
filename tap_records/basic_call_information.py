from pyasn1.type import univ, namedtype

from tap_records.call_event_time_stamp import CallEventTimeStamp
from tap_records.call_originator import CallOriginator
from tap_records.chargeable_subscriber import ChargeableSubscriber

class BasicCallInformation(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('chargeableSubscriber', ChargeableSubscriber()),
        namedtype.NamedType('callOriginator', CallOriginator()),
        namedtype.NamedType('callEventStartTimeStamp', CallEventTimeStamp()),
        namedtype.NamedType('totalCallEventDuration', univ.Integer())
    )

