from pyasn1.type import univ

from tap_records.basic_service_used import BasicServiceUsed

class BasicServiceUsedList(univ.SequenceOf):
    componentType = BasicServiceUsed()