from pyasn1.type import univ, namedtype

from tap_records.mobile_terminated_call import MobileTerminatedCall
from tap_records.mobile_originated_call import MobileOriginatedCall

class CallEventDetail(univ.Choice):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('MobileTerminatedCall', MobileTerminatedCall()),
        namedtype.NamedType('MobileOriginatedCall', MobileOriginatedCall())
    )
