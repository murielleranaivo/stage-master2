from pyasn1.type import univ, namedtype, char

from tap_records.call_type_group import CallTypeGroup
from tap_records.charge_detail_list import ChargeDetailList

class ChargeInformation(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('ChargedItem', char.VisibleString()),
        namedtype.NamedType('ExchangeRateCode', univ.Integer()),
        namedtype.OptionalNamedType('CallTypeGroup', CallTypeGroup()),
        namedtype.NamedType('ChargeDetailList', ChargeDetailList())
    )