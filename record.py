from pyasn1.type import univ
from pyasn1.type import namedtype
from pyasn1.type import char

class Record(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('CALL_TYPE', univ.Integer()),
        namedtype.NamedType('SERVICE_CODE', univ.Integer()),
        namedtype.NamedType('NE_CODE', char.VisibleString()),
        namedtype.NamedType('IN_ROUTE', char.VisibleString()),
        namedtype.NamedType('OUT_ROUTE', char.VisibleString()),
        namedtype.NamedType('IMSI', char.VisibleString()),
        namedtype.NamedType('SGSN_ADDRESS', char.VisibleString()),
        namedtype.NamedType('A_NUMBER', char.VisibleString()),
        namedtype.NamedType('B_NUMBER', char.VisibleString()),
        namedtype.NamedType('C_NUMBER', char.VisibleString()),
        namedtype.NamedType('APN_ADDRESS', char.VisibleString()),
        namedtype.NamedType('PDP_ADDRESS', char.VisibleString()),
        namedtype.NamedType('CALL_DATE', char.VisibleString()),
        namedtype.NamedType('CALL_DURATION', univ.Integer()),
        namedtype.NamedType('DATA_VOLUME_INC', univ.Integer()),
        namedtype.NamedType('DATA_VOLUME_OUT', univ.Integer()),
        namedtype.NamedType('TELESERVICE', char.VisibleString()),
        namedtype.NamedType('BEARERSERVICE', char.VisibleString()),
        namedtype.NamedType('CAMEL_FLAG', char.VisibleString()),
        namedtype.NamedType('CAMEL_SERVICE_LEVEL', char.VisibleString()),
        namedtype.NamedType('CAMEL_SERVICE_KEY', char.VisibleString()),
        namedtype.NamedType('CAMEL_DEFAULT_CALL_HANDLING', char.VisibleString()),
        namedtype.NamedType('CAMEL_SERVER_ADDRESS', char.VisibleString()),
        namedtype.NamedType('CAMEL_MSC_ADDRESS', char.VisibleString()),
        namedtype.NamedType('CAMEL_CALL_REF_NUM', char.VisibleString()),
        namedtype.NamedType('CAMEL_INIT_CF_INDICATOR', char.VisibleString()),
        namedtype.NamedType('CAMEL_DESTINATION_NUM', char.VisibleString()),
        namedtype.NamedType('CAMEL_MODIFICATION', char.VisibleString()),
        namedtype.NamedType('SUPPLIMENTARY_NUM', char.VisibleString()),
        namedtype.NamedType('NETWORK_TIME', char.VisibleString()),
        namedtype.NamedType('REASON_FOR_CLEARDOWN', char.VisibleString()),
        namedtype.NamedType('PARTIAL_INDICATOR', char.VisibleString()),
        namedtype.NamedType('PARTIAL_SEQ_NUM', char.VisibleString()),
        namedtype.NamedType('IMEI_NUM', char.VisibleString()),
        namedtype.NamedType('CHRONO_NUM', char.VisibleString()),
        namedtype.NamedType('CHARGING_ID', char.VisibleString()),
        namedtype.NamedType('SUBSCRIBER_TYPE', char.VisibleString())
    )