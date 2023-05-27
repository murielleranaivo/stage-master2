from pyasn1.type import univ, namedtype

from tap_records.basic_service import BasicService
from tap_records.charge_information_list import ChargeInformationList
from tap_records.time_stamp import TimeStamp

class BasicServiceUsed(univ.Sequence):    
    componentType = namedtype.NamedType(
        namedtype.NamedType('BasicService', BasicService()),
        namedtype.NamedType('ChargingTimeStamp', TimeStamp()),
        namedtype.NamedType('ChargeInformationList', ChargeInformationList())
    )
    

