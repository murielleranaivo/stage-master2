from pyasn1.type import univ, namedtype

from tap_records.call_originator import CallOriginator
from tap_records.chargeable_subscriber import ChargeableSubscriber
from tap_records.destination import Destination
from tap_records.time_stamp import TimeStamp

class BasicCallInformation(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('ChargeableSubscriber', ChargeableSubscriber()),
        namedtype.OptionalNamedType('CallOriginator', CallOriginator()),
        namedtype.OptionalNamedType('Destination', Destination()),
        namedtype.NamedType('CallEventStartTimeStamp', TimeStamp()),
        namedtype.NamedType('TotalCallEventDuration', univ.Integer())
    )

