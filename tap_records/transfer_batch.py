from pyasn1.type import univ, namedtype

from tap_records.accounting_info import AccountingInfo
from tap_records.audit_control_info import AuditControlInfo
from tap_records.batch_control_info import BatchControlInfo
from tap_records.call_event_details import CallEventDetails
from tap_records.network_info import NetworkInfo

class TransferBatch(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('batchControlInfo', BatchControlInfo()),
        namedtype.NamedType('accountingInfo', AccountingInfo()),
        namedtype.NamedType('networkInfo', NetworkInfo()),
        namedtype.NamedType('callEventDetails', CallEventDetails()),
        namedtype.NamedType('auditControlInfo', AuditControlInfo())
    )