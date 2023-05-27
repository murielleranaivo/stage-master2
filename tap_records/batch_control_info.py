from pyasn1.type import univ, namedtype, char

from tap_records.time_stamp import TimeStamp

class BatchControlInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('Sender', char.VisibleString()),
        namedtype.NamedType('Recipient', char.VisibleString()),
        namedtype.NamedType('FileSequenceNumber', univ.Integer()),
        namedtype.NamedType('FileCreationTimeStamp', TimeStamp()),
        namedtype.NamedType('TransferCutOffTimeStamp', TimeStamp()),
        namedtype.NamedType('FileAvailableTimeStamp', TimeStamp()),
        namedtype.NamedType('SpecificationVersionNumber', univ.Integer()),
        namedtype.NamedType('ReleaseVersionNumber', univ.Integer())
    )
