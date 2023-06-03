from tap_records.accounting_info import AccountingInfo
from tap_records.audit_control_info import AuditControlInfo
from tap_records.basic_call_information import BasicCallInformation
from tap_records.basic_service import BasicService
from tap_records.basic_service_used import BasicServiceUsed
from tap_records.basic_service_used_list import BasicServiceUsedList
from tap_records.batch_control_info import BatchControlInfo
from tap_records.call_event_detail import CallEventDetail
from tap_records.call_event_details import CallEventDetails
from tap_records.call_originator import CallOriginator
from tap_records.call_type_group import CallTypeGroup
from tap_records.charge_detail import ChargeDetail
from tap_records.charge_detail_list import ChargeDetailList
from tap_records.charge_information import ChargeInformation
from tap_records.charge_information_list import ChargeInformationList
from tap_records.chargeable_subscriber import ChargeableSubscriber
from tap_records.currency_conversion import CurrencyConversion
from tap_records.currency_conversion_info import CurrencyConversionInfo
from tap_records.destination import Destination
from tap_records.equipment_identifier import EquipmentIdentifier
from tap_records.location_information import LocationInformation
from tap_records.mobile_originated_call import MobileOriginatedCall
from tap_records.mobile_terminated_call import MobileTerminatedCall
from tap_records.network_info import NetworkInfo
from tap_records.network_location import NetworkLocation
from tap_records.operator_spec_information import OperatorSpecInformation
from tap_records.rec_entity_info import RecEntityInfo
from tap_records.rec_entity_information import RecEntityInformation
from tap_records.service_code import ServiceCode
from tap_records.sim_chargeable_subscriber import SimChargeableSubscriber
from tap_records.data_interchange import DataInterChange
from pyasn1.type import univ
from pyasn1.type import char
from pyasn1.codec.ber import encoder
import file_utils
from tap_records.time_stamp import TimeStamp
from tap_records.transfer_batch import TransferBatch
from tap_records.utc_time_offset_info import UtcTimeOffsetInfo

key = b'5fp1lg8_jZKwQFpBHH9F2QYRRc3fn8cFmSsZu33Z6PI='

# ===================
# | DataInterChange |
# ===================
dataInterChange = DataInterChange()

# =================
# | TransferBatch |
# =================
transferBatch = TransferBatch()

# -----------------------------------  BatchControlInfo ------------------------------------------

batchControlInfo = BatchControlInfo()
batchControlInfo.setComponentByName('Sender', char.VisibleString('FRAF1'))
batchControlInfo.setComponentByName('Recipient', char.VisibleString('MDGTM'))
batchControlInfo.setComponentByName('FileSequenceNumber', univ.Integer(42711))

batchControlInfo.setComponentByName('SpecificationVersionNumber', univ.Integer(3))
batchControlInfo.setComponentByName('ReleaseVersionNumber', univ.Integer(11))

# BatchControlInfo _> FileCreationTimeStamp
fileCreationTimeStamp = TimeStamp()
fileCreationTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503020450))
fileCreationTimeStamp.setComponentByName('UtcTimeOffset', char.VisibleString('0'))
batchControlInfo.setComponentByName('FileCreationTimeStamp', fileCreationTimeStamp)

# BatchControlInfo _> TransferCutOffTimeStamp
transferCutOffTimeStamp = TimeStamp()
transferCutOffTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503020510))
transferCutOffTimeStamp.setComponentByName('UtcTimeOffset', char.VisibleString('0'))
batchControlInfo.setComponentByName('TransferCutOffTimeStamp', transferCutOffTimeStamp)

# BatchControlInfo _> FileAvailableTimeStamp
fileAvailableTimeStamp = TimeStamp()
fileAvailableTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503020510))
fileAvailableTimeStamp.setComponentByName('UtcTimeOffset', char.VisibleString('0'))
batchControlInfo.setComponentByName('FileAvailableTimeStamp', fileAvailableTimeStamp)

transferBatch.setComponentByName('BatchControlInfo', batchControlInfo)

# --------------------------------------- AccountingInfo --------------------------------------------

accountingInfo = AccountingInfo()
accountingInfo.setComponentByName('LocalCurrency', char.VisibleString('EUR'))
accountingInfo.setComponentByName('TapCurrency', char.VisibleString('XDR'))

accountingInfo.setComponentByName('TapDecimalPlaces', univ.Integer(5))

# AccountingInfo _> CurrencyConversionInfo
currencyConversionInfo = CurrencyConversionInfo()

# AccountingInfo _> CurrencyConversionInfo _> CurrencyConversion
currencyConversion = CurrencyConversion() 
currencyConversion.setComponentByName('ExchangeRateCode', univ.Integer(0))
currencyConversion.setComponentByName('NumberOfDecimalPlaces', univ.Integer(5))
currencyConversion.setComponentByName('ExchangeRate', univ.Integer(122799))
currencyConversionInfo.setComponents(currencyConversion)
accountingInfo.setComponentByName('CurrencyConversionInfo', currencyConversionInfo)

transferBatch.setComponentByName('AccountingInfo', accountingInfo)

# ---------------------------------------- NetworkInfo ---------------------------------------------

networkInfo = NetworkInfo()

# NetworkInfo _> UtcTimeOffsetInfo
utcTimeOffsetInfo = UtcTimeOffsetInfo()

# NetworkInfo _> UtcTimeOffsetInfo _> 1
utcTimeInfo1 = TimeStamp()
utcTimeInfo1.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))
utcTimeInfo1.setComponentByName('UtcTimeOffset', char.VisibleString('+0200'))
utcTimeOffsetInfo.setComponents(utcTimeInfo1)
networkInfo.setComponentByName('UtcTimeOffsetInfo', utcTimeOffsetInfo)

# NetworkInfo _> RecEntityInfo
recEntityInfo = RecEntityInfo()

# NetworkInfo _> RecEntityInfo _> RecEntityInformation 1
recEntityInformation = RecEntityInformation()
recEntityInformation.setComponentByName('RecEntityCode', univ.Integer(0))
recEntityInformation.setComponentByName('RecEntityType', univ.Integer(1))
recEntityInformation.setComponentByName('RecEntityId', univ.Integer(3312800))

# NetworkInfo _> RecEntityInfo _> RecEntityInformation 2
recEntityInformation2 = RecEntityInformation()
recEntityInformation2.setComponentByName('RecEntityCode', univ.Integer(1))
recEntityInformation2.setComponentByName('RecEntityType', univ.Integer(1))
recEntityInformation2.setComponentByName('RecEntityId', univ.Integer(3312100))

# NetworkInfo _> RecEntityInfo _> RecEntityInformation 3
recEntityInformation3 = RecEntityInformation()
recEntityInformation3.setComponentByName('RecEntityCode', univ.Integer(2))
recEntityInformation3.setComponentByName('RecEntityType', univ.Integer(1))
recEntityInformation3.setComponentByName('RecEntityId', univ.Integer(3312500))

recEntityInfo.setComponents(recEntityInformation, recEntityInformation2, recEntityInformation3 )

networkInfo.setComponentByName('RecEntityInfo', recEntityInfo)

transferBatch.setComponentByName('NetworkInfo', networkInfo)

# -------------------------------------- CallEventDetails -------------------------------------------

callEventdetails = CallEventDetails()

#=========================
# MobileTerminatedCall 1 |
#=========================
mobileTerminatedCall = MobileTerminatedCall()

# MobileTerminatedCall _> BasicCallInformation
basicCallInformation = BasicCallInformation()

basicCallInformation.setComponentByName('TotalCallEventDuration', univ.Integer(0))

# MobileTerminatedCall _> BasicCallInformation _> ChargeableSubscriber
chargeableSubscriber = ChargeableSubscriber()

# MobileTerminatedCall _> BasicCallInformation _> ChargeableSubscriber _> SimChargeableSubscriber
simchargeableSubscriber = SimChargeableSubscriber()
simchargeableSubscriber.setComponentByName('Imsi', char.VisibleString('646040226565007'))
simchargeableSubscriber.setComponentByName('Msisdn', char.VisibleString('261341218543'))
chargeableSubscriber.setComponentByName('SimChargeableSubscriber', simchargeableSubscriber)
basicCallInformation.setComponentByName('ChargeableSubscriber', chargeableSubscriber)

# MobileTerminatedCall _> BasicCallInformation _> CallOriginator
callOriginator = CallOriginator()
callOriginator.setComponentByName('CallingNumber', char.VisibleString('261340010069'))
basicCallInformation.setComponentByName('CallOriginator', callOriginator)

# MobileTerminatedCall _> BasicCallInformation _> CallEventStartTimeStamp
callEventStartTimeStamp = TimeStamp()
callEventStartTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503025648))
callEventStartTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))
basicCallInformation.setComponentByName('CallEventStartTimeStamp', callEventStartTimeStamp)

mobileTerminatedCall.setComponentByName('BasicCallInformation', basicCallInformation)

# MobileTerminatedCall _> LocationInformation
locationInformation = LocationInformation()

# MobileTerminatedCall _> LocationInformation _> NetworkLocation
networklocation = NetworkLocation()
networklocation.setComponentByName('RecEntityCode', univ.Integer(0))
networklocation.setComponentByName('CallReference', univ.Integer(6233882))
networklocation.setComponentByName('LocationArea', univ.Integer(1800))
networklocation.setComponentByName('CellId', univ.Integer(58553))
locationInformation.setComponentByName('NetworkLocation', networklocation)

mobileTerminatedCall.setComponentByName('LocationInformation', locationInformation)

# MobileTerminatedCall _> EquipmentIdentifier
equipmentIdentifier = EquipmentIdentifier()
equipmentIdentifier.setComponentByName('Imei', char.VisibleString('356787102808534'))

mobileTerminatedCall.setComponentByName('EquipmentIdentifier', equipmentIdentifier)

# MobileTerminatedCall _> BasicServiceUsedList
basicServiceUsedList = BasicServiceUsedList()

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed
basicServiceUsed = BasicServiceUsed()

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> BasicService
basicService = BasicService()

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> BasicService > ServiceCode
serviceCode = ServiceCode()
serviceCode.setComponentByName('TeleServiceCode', univ.Integer(21))

basicService.setComponentByName('ServiceCode', serviceCode)
basicServiceUsed.setComponentByName('BasicService', basicService)

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> ChargingTimeStamp
chargingTimeStamp = TimeStamp()
chargingTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503025648))
chargingTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicServiceUsed.setComponentByName('ChargingTimeStamp', chargingTimeStamp)

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> ChargeInformationList
chargeInformationList = ChargeInformationList()

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> ChargeInformationList _> ChargeInformation
chargeInformation = ChargeInformation()
chargeInformation.setComponentByName('ChargedItem', char.VisibleString('E'))
chargeInformation.setComponentByName('ExchangeRateCode', univ.Integer(0))

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> ChargeInformationList _> ChargeInformation _> ChargeDetailList
chargeDetailList = ChargeDetailList()

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> ChargeInformationList _> ChargeInformation _> ChargeDetailList _> ChargeDetail
chargeDetail = ChargeDetail()
chargeDetail.setComponentByName('ChargeType', univ.Integer(00))
chargeDetail.setComponentByName('Charge', univ.Integer(0))
chargeDetail.setComponentByName('ChargedUnits', univ.Integer(1))

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> ChargeInformationList _> ChargeInformation _> ChargeDetailList _> ChargeDetail _> ChargeDetailTimeStamp
chargeDetailTimeStamp = TimeStamp()
chargeDetailTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503025648))
chargeDetailTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

chargeDetail.setComponentByName('ChargeDetailTimeStamp', chargeDetailTimeStamp)
chargeDetailList.setComponents(chargeDetail)
chargeInformation.setComponentByName('ChargeDetailList', chargeDetailList)
chargeInformationList.setComponents(chargeInformation)

basicServiceUsed.setComponentByName('ChargeInformationList', chargeInformationList)

basicServiceUsedList.setComponents(basicServiceUsed)

mobileTerminatedCall.setComponentByName('BasicServiceUsedList', basicServiceUsedList)

# MobileTerminatedCall _> OperatorSpecInformation
operatorSpecInformation = OperatorSpecInformation()
operatorSpecInformation.setComponentByName('OperatorSpecInformation', char.VisibleString('ORP_V:GSM4-1'))

mobileTerminatedCall.setComponentByName('OperatorSpecInformation', operatorSpecInformation)

#=========================
# MobileTerminatedCall 2 |
#=========================
mobileTerminatedCall2 = MobileTerminatedCall()

# MobileTerminatedCall _> BasicCallInformation
basicCallInformation2 = BasicCallInformation()

basicCallInformation2.setComponentByName('TotalCallEventDuration', univ.Integer(0))

# MobileTerminatedCall _> BasicCallInformation _> ChargeableSubscriber
chargeableSubscriber2 = ChargeableSubscriber()

# MobileTerminatedCall _> BasicCallInformation _> ChargeableSubscriber _> SimChargeableSubscriber
simchargeableSubscriber2 = SimChargeableSubscriber()
simchargeableSubscriber2.setComponentByName('Imsi', char.VisibleString('646040226565007'))
simchargeableSubscriber2.setComponentByName('Msisdn', char.VisibleString('261341218543'))
chargeableSubscriber2.setComponentByName('SimChargeableSubscriber', simchargeableSubscriber2)
basicCallInformation2.setComponentByName('ChargeableSubscriber', chargeableSubscriber2)

# MobileTerminatedCall _> BasicCallInformation _> CallOriginator
callOriginator2 = CallOriginator()
callOriginator2.setComponentByName('CallingNumber', char.VisibleString('261340010069'))
basicCallInformation2.setComponentByName('CallOriginator', callOriginator2)

# MobileTerminatedCall _> BasicCallInformation _> CallEventStartTimeStamp
callEventStartTimeStamp2 = TimeStamp()
callEventStartTimeStamp2.setComponentByName('LocalTimeStamp', univ.Integer(20230503025657))
callEventStartTimeStamp2.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))
basicCallInformation2.setComponentByName('CallEventStartTimeStamp', callEventStartTimeStamp2)

mobileTerminatedCall2.setComponentByName('BasicCallInformation', basicCallInformation2)

# MobileTerminatedCall _> LocationInformation
locationInformation2 = LocationInformation()

# MobileTerminatedCall _> LocationInformation _> NetworkLocation
networklocation2 = NetworkLocation()
networklocation2.setComponentByName('RecEntityCode', univ.Integer(0))
networklocation2.setComponentByName('CallReference', univ.Integer(5857066))
networklocation2.setComponentByName('LocationArea', univ.Integer(1800))
networklocation2.setComponentByName('CellId', univ.Integer(58553))
locationInformation2.setComponentByName('NetworkLocation', networklocation2)

mobileTerminatedCall2.setComponentByName('LocationInformation', locationInformation2)

# MobileTerminatedCall _> EquipmentIdentifier
equipmentIdentifier2 = EquipmentIdentifier()
equipmentIdentifier2.setComponentByName('Imei', char.VisibleString('356787102808534'))

mobileTerminatedCall2.setComponentByName('EquipmentIdentifier', equipmentIdentifier2)

# MobileTerminatedCall _> BasicServiceUsedList
basicServiceUsedList2 = BasicServiceUsedList()

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed
basicServiceUsed2 = BasicServiceUsed()

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> BasicService
basicService2 = BasicService()

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> BasicService > ServiceCode
serviceCode2 = ServiceCode()
serviceCode2.setComponentByName('TeleServiceCode', univ.Integer(21))

basicService2.setComponentByName('ServiceCode', serviceCode2)
basicServiceUsed2.setComponentByName('BasicService', basicService2)

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> ChargingTimeStamp
chargingTimeStamp2 = TimeStamp()
chargingTimeStamp2.setComponentByName('LocalTimeStamp', univ.Integer(20230503025657))
chargingTimeStamp2.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicServiceUsed2.setComponentByName('ChargingTimeStamp', chargingTimeStamp2)

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> ChargeInformationList
chargeInformationList2 = ChargeInformationList()

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> ChargeInformationList _> ChargeInformation
chargeInformation2 = ChargeInformation()
chargeInformation2.setComponentByName('ChargedItem', char.VisibleString('E'))
chargeInformation2.setComponentByName('ExchangeRateCode', univ.Integer(0))

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> ChargeInformationList _> ChargeInformation _> ChargeDetailList
chargeDetailList2 = ChargeDetailList()

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> ChargeInformationList _> ChargeInformation _> ChargeDetailList _> ChargeDetail
chargeDetail2 = ChargeDetail()
chargeDetail2.setComponentByName('ChargeType', univ.Integer(00))
chargeDetail2.setComponentByName('Charge', univ.Integer(0))
chargeDetail2.setComponentByName('ChargedUnits', univ.Integer(1))

# MobileTerminatedCall _> BasicServiceUsedList _> BasicServiceUsed _> ChargeInformationList _> ChargeInformation _> ChargeDetailList _> ChargeDetail _> ChargeDetailTimeStamp
chargeDetailTimeStamp2 = TimeStamp()
chargeDetailTimeStamp2.setComponentByName('LocalTimeStamp', univ.Integer(20230503025657))
chargeDetailTimeStamp2.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

chargeDetail2.setComponentByName('ChargeDetailTimeStamp', chargeDetailTimeStamp2)
chargeDetailList2.setComponents(chargeDetail2)
chargeInformation2.setComponentByName('ChargeDetailList', chargeDetailList2)
chargeInformationList2.setComponents(chargeInformation2)

basicServiceUsed2.setComponentByName('ChargeInformationList', chargeInformationList2)

basicServiceUsedList2.setComponents(basicServiceUsed2)

mobileTerminatedCall2.setComponentByName('BasicServiceUsedList', basicServiceUsedList2)

# MobileTerminatedCall _> OperatorSpecInformation
operatorSpecInformation2 = OperatorSpecInformation()
operatorSpecInformation2.setComponentByName('OperatorSpecInformation', char.VisibleString('ORP_V:GSM4-2'))

mobileTerminatedCall2.setComponentByName('OperatorSpecInformation', operatorSpecInformation2)





mobileOriginatedCall = MobileOriginatedCall()
basicCallInformation = BasicCallInformation()
chargeableSubscriber = ChargeableSubscriber()
simchargeableSubscriber = SimChargeableSubscriber()
simchargeableSubscriber.setComponentByName('Imsi', char.VisibleString('646040222092540'))
simchargeableSubscriber.setComponentByName('Msisdn', char.VisibleString('261340383333'))
chargeableSubscriber.setComponentByName('SimChargeableSubscriber', simchargeableSubscriber)
basicCallInformation.setComponentByName('ChargeableSubscriber', chargeableSubscriber)

destination = Destination()
basicCallInformation.setComponentByName('Destination', destination)
destination.setComponentByName('CalledNumber', char.VisibleString('261340010000'))
destination.setComponentByName('DialledDigits', char.VisibleString('447786205094'))
destination.setComponentByName('SMSDestinationNumber', char.VisibleString('447786205094'))
mobileOriginatedCall.setComponentByName('BasicCallInformation', basicCallInformation)

callEventStartTimeStamp = TimeStamp()
callEventStartTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031413))
callEventStartTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicCallInformation.setComponentByName('TotalCallEventDuration', univ.Integer(0))
basicCallInformation.setComponentByName('CallEventStartTimeStamp', callEventStartTimeStamp)

locationInformation = LocationInformation()
networklocation = NetworkLocation()
networklocation.setComponentByName('RecEntityCode', univ.Integer(2))
networklocation.setComponentByName('CallReference', univ.Integer(5236971))
networklocation.setComponentByName('LocationArea', univ.Integer(1058))
networklocation.setComponentByName('CellId', univ.Integer(11976))
locationInformation.setComponentByName('NetworkLocation', networklocation)
mobileOriginatedCall.setComponentByName('LocationInformation', locationInformation)

equipmentIdentifier = EquipmentIdentifier()
equipmentIdentifier.setComponentByName('Imei', char.VisibleString('359176077876071'))
mobileOriginatedCall.setComponentByName('EquipmentIdentifier', equipmentIdentifier)

basicServiceUsedList = BasicServiceUsedList()
basicServiceUsed = BasicServiceUsed()
basicService = BasicService()

chargingTimeStamp = TimeStamp()
chargeInformationList = ChargeInformationList()

serviceCode = ServiceCode()

basicServiceUsed.setComponentByName('BasicService', basicService)
basicServiceUsedList.setComponents(basicServiceUsed)
basicService.setComponentByName('ServiceCode', serviceCode)
serviceCode.setComponentByName('TeleServiceCode', univ.Integer(22))

basicServiceUsed.setComponentByName('ChargingTimeStamp', chargingTimeStamp)
chargingTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031413))
chargingTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicServiceUsed.setComponentByName('ChargeInformationList', chargeInformationList)
chargeInformation = ChargeInformation()
chargeInformationList.setComponents(chargeInformation)
chargeInformation.setComponentByName('ChargedItem', char.VisibleString('E'))
chargeInformation.setComponentByName('ExchangeRateCode', univ.Integer(0))

callTypeGroup = CallTypeGroup()
chargeInformation.setComponentByName('CallTypeGroup', callTypeGroup)
callTypeGroup.setComponentByName('CallTypeLevel1', univ.Integer(2))
callTypeGroup.setComponentByName('CallTypeLevel2', univ.Integer(0))
callTypeGroup.setComponentByName('CallTypeLevel3', univ.Integer(0))

chargeDetailList = ChargeDetailList()
chargeInformation.setComponentByName('ChargeDetailList', chargeDetailList)
chargeDetail = ChargeDetail()
chargeDetailList.setComponents(chargeDetail)
chargeDetail.setComponentByName('ChargeType', univ.Integer(00))
chargeDetail.setComponentByName('Charge', univ.Integer(20358))
chargeDetail.setComponentByName('ChargedUnits', univ.Integer(1))
chargeDetailTimeStamp = TimeStamp()
chargeDetail.setComponentByName('ChargeDetailTimeStamp', chargeDetailTimeStamp)
chargeDetailTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031413))
chargeDetailTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

mobileOriginatedCall.setComponentByName('BasicServiceUsedList', basicServiceUsedList)

operatorSpecInformation = OperatorSpecInformation()
mobileOriginatedCall.setComponentByName('OperatorSpecInformation', operatorSpecInformation)
operatorSpecInformation.setComponentByName('OperatorSpecInformation', char.VisibleString('ORP_V:GSM4-5'))





auditControlInfo = AuditControlInfo()

earliestCallTimeStamp = TimeStamp()
auditControlInfo.setComponentByName('EarliestCallTimeStamp', earliestCallTimeStamp)
earliestCallTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503025648))
earliestCallTimeStamp.setComponentByName('UtcTimeOffset', char.VisibleString('+0200'))

latestCallTimeStamp = TimeStamp()
auditControlInfo.setComponentByName('LatestCallTimeStamp', latestCallTimeStamp)
latestCallTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031413))
latestCallTimeStamp.setComponentByName('UtcTimeOffset', char.VisibleString('+0200'))
auditControlInfo.setComponentByName('TotalCharge', univ.Integer(20358))
auditControlInfo.setComponentByName('TotalTaxValue', univ.Integer(0))
auditControlInfo.setComponentByName('TotalDiscountValue', univ.Integer(0))
auditControlInfo.setComponentByName('CallEventDetailsCount', univ.Integer(6))

auditControlInfo.setComponentByName('OperatorSpecInformation', operatorSpecInformation)
operatorSpecInformation.setComponentByName('OperatorSpecInformation', char.VisibleString('NextGenCreatedFile'))

callEventdetails.setComponents(
    CallEventDetail().setComponentByName('MobileTerminatedCall', mobileTerminatedCall),
    CallEventDetail().setComponentByName('MobileTerminatedCall', mobileTerminatedCall2),
    CallEventDetail().setComponentByName('MobileOriginatedCall', mobileOriginatedCall),
)

transferBatch.setComponentByName('CallEventDetails', callEventdetails)


transferBatch.setComponentByName('AuditControlInfo', auditControlInfo)

dataInterChange.setComponentByName('TransferBatch', transferBatch)

# Append the record to the list
tap_record = encoder.encode(dataInterChange)

filepath = file_utils.get_file_path("demo", "tap")
with open(filepath, "wb") as tap_file:
    tap_file.write(tap_record)
