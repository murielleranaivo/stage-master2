from pyasn1.type import univ
from tap_records.time_stamp import TimeStamp

class UtcTimeOffsetInfo(univ.SequenceOf):
    componentType = TimeStamp()

