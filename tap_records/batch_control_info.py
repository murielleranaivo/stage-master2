from pyasn1.type import univ, namedtype

from tap_records.time_stamp import TimeStamp

class BatchControlInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('sender', univ.OctetString()),
        namedtype.NamedType('recipient', univ.OctetString()),
        namedtype.NamedType('fileSequenceNumber', univ.Integer()),
        namedtype.NamedType('fileCreationTimeStamp', TimeStamp()),
        namedtype.NamedType('transferCutOffTimeStamp', TimeStamp()),
        namedtype.NamedType('fileAvailableTimeStamp', TimeStamp()),
        namedtype.NamedType('specificationVersionNumber', univ.Integer()),
        namedtype.NamedType('releaseVersionNumber', univ.Integer())
    )
