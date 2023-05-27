from pyasn1.type import univ, namedtype

from tap_records.rec_entity_information import RecEntityInformation

class RecEntityInfo(univ.SequenceOf):
    componentType = RecEntityInformation()