from pyasn1.type import univ, namedtype

from tap_records.mobile_terminated_call import MobileTerminatedCall
from tap_records.mobile_originated_call import MobileOriginatedCall

class CallEventDetail(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('mobileTerminatedCall', MobileTerminatedCall()),
        namedtype.NamedType('mobileOriginatedCall', MobileOriginatedCall())
    )
