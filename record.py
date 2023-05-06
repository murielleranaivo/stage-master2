from pyasn1.type import univ
from pyasn1.type import namedtype
from pyasn1.type import namedval
from pyasn1.type import char
from pyasn1.type import useful

class Record(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('cdrType', univ.Integer(namedValues=namedval.NamedValues(('sgsnMmeRecord', 18), ('sgsnRecord', 19), ('ggsnRecord', 20), ('chargingGatewayRecord', 21)))),
        namedtype.NamedType('callId', univ.OctetString()),
        namedtype.NamedType('originatingNum', char.GeneralString()),
        namedtype.NamedType('terminatingNum', char.GeneralString()),
        namedtype.NamedType('serviceClass', univ.Integer()),
        namedtype.NamedType('originationTime', useful.GeneralizedTime()),
        namedtype.NamedType('terminationTime', useful.GeneralizedTime()),
        namedtype.NamedType('callDuration', univ.Integer()),
        namedtype.NamedType('causeCode', char.GeneralString()),
        namedtype.NamedType('callingPartyId', char.GeneralString()),
        namedtype.NamedType('calledPartyId', char.GeneralString()),
        namedtype.NamedType('recordingEntity', char.GeneralString()),
        namedtype.NamedType('location', char.GeneralString()),
        namedtype.NamedType('recordingSessionId', char.GeneralString()),
        namedtype.NamedType('nodeAddress', char.GeneralString())
    )