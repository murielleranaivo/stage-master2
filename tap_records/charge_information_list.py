from pyasn1.type import univ

from tap_records.charge_information import ChargeInformation

class ChargeInformationList(univ.SequenceOf):
    componentType = ChargeInformation()