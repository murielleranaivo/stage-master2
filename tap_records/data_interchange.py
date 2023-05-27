from pyasn1.type import univ, namedtype

from tap_records.transfer_batch import TransferBatch

class DataInterChange(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('TransferBatch', TransferBatch())
    )