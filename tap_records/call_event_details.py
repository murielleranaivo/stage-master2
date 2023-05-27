from pyasn1.type import univ, namedtype

from tap_records.call_event_detail import CallEventDetail

class CallEventDetails(univ.SequenceOf):
    componentType = CallEventDetail()
