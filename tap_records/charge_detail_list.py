from pyasn1.type import univ

from tap_records.charge_detail import ChargeDetail

class ChargeDetailList(univ.SequenceOf):
    componentType = ChargeDetail()