from accounting_info import AccountingInfo
from audit_control_info import AuditControlInfo
from basic_call_information import BasicCallInformation
from basic_service import BasicService
from basic_service_used import BasicServiceUsed
from basic_service_used_list import BasicServiceUsedList
from batch_control_info import BatchControlInfo
from call_event_detail import CallEventDetail
from call_event_details import CallEventDetails
from call_originator import CallOriginator
from call_type_group import CallTypeGroup
from charge_detail import ChargeDetail
from charge_detail_list import ChargeDetailList
from charge_information import ChargeInformation
from charge_information_list import ChargeInformationList
from chargeable_subscriber import ChargeableSubscriber
from currency_conversion import CurrencyConversion
from currency_conversion_info import CurrencyConversionInfo
from destination import Destination
from equipment_identifier import EquipmentIdentifier
from location_information import LocationInformation
from mobile_originated_call import MobileOriginatedCall
from mobile_terminated_call import MobileTerminatedCall
from network_info import NetworkInfo
from network_location import NetworkLocation
from operator_spec_information import OperatorSpecInformation
from rec_entity_info import RecEntityInfo
from rec_entity_information import RecEntityInformation
from record import Record
from service_code import ServiceCode
from sim_chargeable_subscriber import SimChargeableSubscriber
from tap_records.data_interchange import DataInterChange
from pyasn1.type import univ
from pyasn1.type import char
from pyasn1.codec.ber import encoder
import file_utils
from time_stamp import TimeStamp
from transfer_batch import TransferBatch
from utc_time_offset_info import UtcTimeOffsetInfo

key = b'5fp1lg8_jZKwQFpBHH9F2QYRRc3fn8cFmSsZu33Z6PI='

# Create a Record object and set its components
dataInterChange = DataInterChange()
transferBatch = TransferBatch()
batchControlInfo = BatchControlInfo()
batchControlInfo.setComponentByName('Sender', char.VisibleString('FRAF1'))
batchControlInfo.setComponentByName('Recipient', char.VisibleString('MDGTM'))
batchControlInfo.setComponentByName('FileSequenceNumber', univ.Integer(42711))

fileCreationTimeStamp = TimeStamp()
fileCreationTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503020450))
fileCreationTimeStamp.setComponentByName('UtcTimeOffset', univ.Integer(0))

batchControlInfo.setComponentByName('FileCreationTimeStamp', fileCreationTimeStamp)

transferCutOffTimeStamp = TimeStamp()
transferCutOffTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503020510))
transferCutOffTimeStamp.setComponentByName('UtcTimeOffset', univ.Integer(0))

batchControlInfo.setComponentByName('TransferCutOffTimeStamp', transferCutOffTimeStamp)

fileAvailableTimeStamp = TimeStamp()
fileAvailableTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503020510))
fileAvailableTimeStamp.setComponentByName('UtcTimeOffset', univ.Integer(0))

batchControlInfo.setComponentByName('FileAvailableTimeStamp', fileAvailableTimeStamp)

batchControlInfo.setComponentByName('SpecificationVersionNumber', univ.Integer(3))
batchControlInfo.setComponentByName('ReleaseVersionNumber', univ.Integer(11))

transferBatch.setComponentByName('BatchControlInfo', batchControlInfo)

accountingInfo = AccountingInfo()
accountingInfo.setComponentByName('LocalCurrency', char.VisibleString('EUR'))
accountingInfo.setComponentByName('TapCurrency', char.VisibleString('XDR'))

transferBatch.setComponentByName('AccountingInfo', accountingInfo)

currencyConversionInfo = CurrencyConversionInfo()
currencyConversion = CurrencyConversion() 
currencyConversion.setComponentByName('ExchangeRateCode', univ.Integer(0))
currencyConversion.setComponentByName('NumberOfDecimalPlaces', univ.Integer(5))
currencyConversion.setComponentByName('ExchangeRate', univ.Integer(122799))
currencyConversionInfo.setComponents(currencyConversion)

accountingInfo.setComponentByName('CurrencyConversionInfo', currencyConversionInfo)

accountingInfo.setComponentByName('TapDecimalPlaces', univ.Integer(5))

networkInfo = NetworkInfo()
utcTimeOffsetInfo = UtcTimeOffsetInfo()
utcTimeInfo1 = TimeStamp()
utcTimeInfo1.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))
utcTimeInfo1.setComponentByName('UtcTimeOffset', char.VisibleString('+0200'))
utcTimeOffsetInfo.setComponents(utcTimeInfo1)
networkInfo.setComponentByName('UtcTimeOffsetInfo', utcTimeOffsetInfo)
transferBatch.setComponentByName('NetworkInfo', networkInfo)

recEntityInfo = RecEntityInfo()

recEntityInformation = RecEntityInformation()
recEntityInformation.setComponentByName('RecEntityCode', univ.Integer(0))
recEntityInformation.setComponentByName('RecEntityType', univ.Integer(1))
recEntityInformation.setComponentByName('RecEntityId', univ.Integer(3312800))

recEntityInformation2 = RecEntityInformation()
recEntityInformation2.setComponentByName('RecEntityCode', univ.Integer(1))
recEntityInformation2.setComponentByName('RecEntityType', univ.Integer(1))
recEntityInformation2.setComponentByName('RecEntityId', univ.Integer(3312100))

recEntityInformation3 = RecEntityInformation()
recEntityInformation3.setComponentByName('RecEntityCode', univ.Integer(2))
recEntityInformation3.setComponentByName('RecEntityType', univ.Integer(1))
recEntityInformation3.setComponentByName('RecEntityId', univ.Integer(3312500))

recEntityInfo.setComponents(recEntityInformation, recEntityInformation2, recEntityInformation3 )

networkInfo.setComponentByName('RecEntityInfo', recEntityInfo)

callEventdetails = CallEventDetails()

mobileTerminatedCall = MobileTerminatedCall()
basicCallInformation = BasicCallInformation()
chargeableSubscriber = ChargeableSubscriber()
simchargeableSubscriber = SimChargeableSubscriber()
simchargeableSubscriber.setComponentByName('Imsi', univ.Integer(646040226565007))
simchargeableSubscriber.setComponentByName('Msisdn', univ.Integer(261341218543))
chargeableSubscriber.setComponentByName('SimChargeableSubscriber', simchargeableSubscriber)
basicCallInformation.setComponentByName('ChargeableSubscriber', chargeableSubscriber)

callOriginator = CallOriginator()
basicCallInformation.setComponentByName('CallOriginator', callOriginator)
callOriginator.setComponentByName('CallingNumber', univ.Integer(261340010069))
mobileTerminatedCall.setComponentByName('BasicCallInformation', basicCallInformation)

callEventStartTimeStamp = TimeStamp()
callEventStartTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503025648))
callEventStartTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicCallInformation.setComponentByName('TotalCallEventDuration', univ.Integer(0))
basicCallInformation.setComponentByName('CallEventStartTimeStamp', callEventStartTimeStamp)

locationInformation = LocationInformation()
networklocation = NetworkLocation()
networklocation.setComponentByName('RecEntityCode', univ.Integer(0))
networklocation.setComponentByName('CallReference', univ.Integer(6233882))
networklocation.setComponentByName('LocationArea', univ.Integer(1800))
networklocation.setComponentByName('CellId', univ.Integer(58553))
locationInformation.setComponentByName('NetworkLocation', networklocation)
mobileTerminatedCall.setComponentByName('LocationInformation', locationInformation)

equipmentIdentifier = EquipmentIdentifier()
equipmentIdentifier.setComponentByName('Imei', univ.Integer(356787102808534))
mobileTerminatedCall.setComponentByName('EquipmentIdentifier', equipmentIdentifier)

basicServiceUsedList = BasicServiceUsedList()
basicServiceUsed = BasicServiceUsed()
basicService = BasicService()

chargingTimeStamp = TimeStamp()
chargeInformationList = ChargeInformationList()

serviceCode = ServiceCode()

basicServiceUsed.setComponentByName('BasicService', basicService)
basicServiceUsedList.setComponents(basicServiceUsed)
basicService.setComponentByName('ServiceCode', serviceCode)
serviceCode.setComponentByName('TeleserviceCode', univ.Integer(21))

basicServiceUsed.setComponentByName('ChargingTimeStamp', chargingTimeStamp)
chargingTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503025648))
chargingTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicServiceUsed.setComponentByName('ChargeInformationList', chargeInformationList)
chargeInformation = ChargeInformation()
chargeInformationList.setComponents(chargeInformation)
chargeInformation.setComponentByName('ChargedItem', char.VisibleString('E'))
chargeInformation.setComponentByName('ExchangeRateCode', univ.Integer(0))
chargeDetailList = ChargeDetailList()
chargeInformation.setComponentByName('ChargeDetailList', chargeDetailList)
chargeDetail = ChargeDetail()
chargeDetailList.setComponents(chargeDetail)
chargeDetail.setComponentByName('ChargeType', univ.Integer(00))
chargeDetail.setComponentByName('Charge', univ.Integer(0))
chargeDetail.setComponentByName('ChargeUnits', univ.Integer(1))
chargeDetailTimeStamp = TimeStamp()
chargeDetail.setComponentByName('ChargeDetailTimeStamp', chargeDetailTimeStamp)
chargeDetailTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503025648))
chargeDetailTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

mobileTerminatedCall.setComponentByName('BasicServiceUsedList', basicServiceUsedList)

operatorSpecInformation = OperatorSpecInformation()
mobileTerminatedCall.setComponentByName('OperatorSpecInformation', operatorSpecInformation)
operatorSpecInformation.setComponentByName('OperatorSpecInformation', char.VisibleString('ORP_V:GSM4-1'))






mobileTerminatedCall2 = MobileTerminatedCall()
basicCallInformation = BasicCallInformation()
chargeableSubscriber = ChargeableSubscriber()
simchargeableSubscriber = SimChargeableSubscriber()
simchargeableSubscriber.setComponentByName('Imsi', univ.Integer(646040226565007))
simchargeableSubscriber.setComponentByName('Msisdn', univ.Integer(261341218543))
chargeableSubscriber.setComponentByName('SimChargeableSubscriber', simchargeableSubscriber)
basicCallInformation.setComponentByName('ChargeableSubscriber', chargeableSubscriber)

callOriginator = CallOriginator()
basicCallInformation.setComponentByName('CallOriginator', callOriginator)
callOriginator.setComponentByName('CallingNumber', univ.Integer(261340010069))
mobileTerminatedCall.setComponentByName('BasicCallInformation', basicCallInformation)

callEventStartTimeStamp = TimeStamp()
callEventStartTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503025657))
callEventStartTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicCallInformation.setComponentByName('TotalCallEventDuration', univ.Integer(0))
basicCallInformation.setComponentByName('CallEventStartTimeStamp', callEventStartTimeStamp)

locationInformation = LocationInformation()
networklocation = NetworkLocation()
networklocation.setComponentByName('RecEntityCode', univ.Integer(0))
networklocation.setComponentByName('CallReference', univ.Integer(5857066))
networklocation.setComponentByName('LocationArea', univ.Integer(1800))
networklocation.setComponentByName('CellId', univ.Integer(58553))
locationInformation.setComponentByName('NetworkLocation', networklocation)
mobileTerminatedCall.setComponentByName('LocationInformation', locationInformation)

equipmentIdentifier = EquipmentIdentifier()
equipmentIdentifier.setComponentByName('Imei', univ.Integer(356787102808534))
mobileTerminatedCall.setComponentByName('EquipmentIdentifier', equipmentIdentifier)

basicServiceUsedList = BasicServiceUsedList()
basicServiceUsed = BasicServiceUsed()
basicService = BasicService()

chargingTimeStamp = TimeStamp()
chargeInformationList = ChargeInformationList()

serviceCode = ServiceCode()

basicServiceUsed.setComponentByName('BasicService', basicService)
basicServiceUsedList.setComponents(basicServiceUsed)
basicService.setComponentByName('ServiceCode', serviceCode)
serviceCode.setComponentByName('TeleserviceCode', univ.Integer(21))

basicServiceUsed.setComponentByName('ChargingTimeStamp', chargingTimeStamp)
chargingTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503025657))
chargingTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicServiceUsed.setComponentByName('ChargeInformationList', chargeInformationList)
chargeInformation = ChargeInformation()
chargeInformationList.setComponents(chargeInformation)
chargeInformation.setComponentByName('ChargedItem', char.VisibleString('E'))
chargeInformation.setComponentByName('ExchangeRateCode', univ.Integer(0))
chargeDetailList = ChargeDetailList()
chargeInformation.setComponentByName('ChargeDetailList', chargeDetailList)
chargeDetail = ChargeDetail()
chargeDetailList.setComponents(chargeDetail)
chargeDetail.setComponentByName('ChargeType', univ.Integer(00))
chargeDetail.setComponentByName('Charge', univ.Integer(0))
chargeDetail.setComponentByName('ChargeUnits', univ.Integer(1))
chargeDetailTimeStamp = TimeStamp()
chargeDetail.setComponentByName('ChargeDetailTimeStamp', chargeDetailTimeStamp)
chargeDetailTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503025657))
chargeDetailTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

mobileTerminatedCall.setComponentByName('BasicServiceUsedList', basicServiceUsedList)

operatorSpecInformation = OperatorSpecInformation()
mobileTerminatedCall.setComponentByName('OperatorSpecInformation', operatorSpecInformation)
operatorSpecInformation.setComponentByName('OperatorSpecInformation', char.VisibleString('ORP_V:GSM4-2'))











mobileTerminatedCall3 = MobileTerminatedCall()
basicCallInformation = BasicCallInformation()
chargeableSubscriber = ChargeableSubscriber()
simchargeableSubscriber = SimChargeableSubscriber()
simchargeableSubscriber.setComponentByName('Imsi', univ.Integer(646040233830418))
simchargeableSubscriber.setComponentByName('Msisdn', univ.Integer(261346052320))
chargeableSubscriber.setComponentByName('SimChargeableSubscriber', simchargeableSubscriber)
basicCallInformation.setComponentByName('ChargeableSubscriber', chargeableSubscriber)

callOriginator = CallOriginator()
basicCallInformation.setComponentByName('CallOriginator', callOriginator)
callOriginator.setComponentByName('CallingNumber', univ.Integer(261340010000))
callOriginator.setComponentByName('SMSOriginator', univ.Integer(261388230377))
mobileTerminatedCall.setComponentByName('BasicCallInformation', basicCallInformation)

callEventStartTimeStamp = TimeStamp()
callEventStartTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031042))
callEventStartTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicCallInformation.setComponentByName('TotalCallEventDuration', univ.Integer(0))
basicCallInformation.setComponentByName('CallEventStartTimeStamp', callEventStartTimeStamp)

locationInformation = LocationInformation()
networklocation = NetworkLocation()
networklocation.setComponentByName('RecEntityCode', univ.Integer(1))
networklocation.setComponentByName('CallReference', univ.Integer(1579919))
networklocation.setComponentByName('LocationArea', univ.Integer(790))
networklocation.setComponentByName('CellId', univ.Integer(63717))
locationInformation.setComponentByName('NetworkLocation', networklocation)
mobileTerminatedCall.setComponentByName('LocationInformation', locationInformation)

equipmentIdentifier = EquipmentIdentifier()
equipmentIdentifier.setComponentByName('Imei', univ.Integer(3598021000040894))
mobileTerminatedCall.setComponentByName('EquipmentIdentifier', equipmentIdentifier)

basicServiceUsedList = BasicServiceUsedList()
basicServiceUsed = BasicServiceUsed()
basicService = BasicService()

chargingTimeStamp = TimeStamp()
chargeInformationList = ChargeInformationList()

serviceCode = ServiceCode()

basicServiceUsed.setComponentByName('BasicService', basicService)
basicServiceUsedList.setComponents(basicServiceUsed)
basicService.setComponentByName('ServiceCode', serviceCode)
serviceCode.setComponentByName('TeleserviceCode', univ.Integer(21))

basicServiceUsed.setComponentByName('ChargingTimeStamp', chargingTimeStamp)
chargingTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031042))
chargingTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicServiceUsed.setComponentByName('ChargeInformationList', chargeInformationList)
chargeInformation = ChargeInformation()
chargeInformationList.setComponents(chargeInformation)
chargeInformation.setComponentByName('ChargedItem', char.VisibleString('E'))
chargeInformation.setComponentByName('ExchangeRateCode', univ.Integer(0))
chargeDetailList = ChargeDetailList()
chargeInformation.setComponentByName('ChargeDetailList', chargeDetailList)
chargeDetail = ChargeDetail()
chargeDetailList.setComponents(chargeDetail)
chargeDetail.setComponentByName('ChargeType', univ.Integer(00))
chargeDetail.setComponentByName('Charge', univ.Integer(0))
chargeDetail.setComponentByName('ChargeUnits', univ.Integer(1))
chargeDetailTimeStamp = TimeStamp()
chargeDetail.setComponentByName('ChargeDetailTimeStamp', chargeDetailTimeStamp)
chargeDetailTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031042))
chargeDetailTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

mobileTerminatedCall.setComponentByName('BasicServiceUsedList', basicServiceUsedList)

operatorSpecInformation = OperatorSpecInformation()
mobileTerminatedCall.setComponentByName('OperatorSpecInformation', operatorSpecInformation)
operatorSpecInformation.setComponentByName('OperatorSpecInformation', char.VisibleString('ORP_V:GSM4-3'))











mobileTerminatedCall4 = MobileTerminatedCall()
basicCallInformation = BasicCallInformation()
chargeableSubscriber = ChargeableSubscriber()
simchargeableSubscriber = SimChargeableSubscriber()
simchargeableSubscriber.setComponentByName('Imsi', univ.Integer(646040233830418))
simchargeableSubscriber.setComponentByName('Msisdn', univ.Integer(261346052320))
chargeableSubscriber.setComponentByName('SimChargeableSubscriber', simchargeableSubscriber)
basicCallInformation.setComponentByName('ChargeableSubscriber', chargeableSubscriber)

callOriginator = CallOriginator()
basicCallInformation.setComponentByName('CallOriginator', callOriginator)
callOriginator.setComponentByName('CallingNumber', univ.Integer(261340010000))
callOriginator.setComponentByName('SMSOriginator', univ.Integer(261388230377))
mobileTerminatedCall.setComponentByName('BasicCallInformation', basicCallInformation)

callEventStartTimeStamp = TimeStamp()
callEventStartTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031045))
callEventStartTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicCallInformation.setComponentByName('TotalCallEventDuration', univ.Integer(0))
basicCallInformation.setComponentByName('CallEventStartTimeStamp', callEventStartTimeStamp)

locationInformation = LocationInformation()
networklocation = NetworkLocation()
networklocation.setComponentByName('RecEntityCode', univ.Integer(1))
networklocation.setComponentByName('CallReference', univ.Integer(2010796))
networklocation.setComponentByName('LocationArea', univ.Integer(790))
networklocation.setComponentByName('CellId', univ.Integer(63717))
locationInformation.setComponentByName('NetworkLocation', networklocation)
mobileTerminatedCall.setComponentByName('LocationInformation', locationInformation)

equipmentIdentifier = EquipmentIdentifier()
equipmentIdentifier.setComponentByName('Imei', univ.Integer(359802100040894))
mobileTerminatedCall.setComponentByName('EquipmentIdentifier', equipmentIdentifier)

basicServiceUsedList = BasicServiceUsedList()
basicServiceUsed = BasicServiceUsed()
basicService = BasicService()

chargingTimeStamp = TimeStamp()
chargeInformationList = ChargeInformationList()

serviceCode = ServiceCode()

basicServiceUsed.setComponentByName('BasicService', basicService)
basicServiceUsedList.setComponents(basicServiceUsed)
basicService.setComponentByName('ServiceCode', serviceCode)
serviceCode.setComponentByName('TeleserviceCode', univ.Integer(21))

basicServiceUsed.setComponentByName('ChargingTimeStamp', chargingTimeStamp)
chargingTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031045))
chargingTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicServiceUsed.setComponentByName('ChargeInformationList', chargeInformationList)
chargeInformation = ChargeInformation()
chargeInformationList.setComponents(chargeInformation)
chargeInformation.setComponentByName('ChargedItem', char.VisibleString('E'))
chargeInformation.setComponentByName('ExchangeRateCode', univ.Integer(0))
chargeDetailList = ChargeDetailList()
chargeInformation.setComponentByName('ChargeDetailList', chargeDetailList)
chargeDetail = ChargeDetail()
chargeDetailList.setComponents(chargeDetail)
chargeDetail.setComponentByName('ChargeType', univ.Integer(00))
chargeDetail.setComponentByName('Charge', univ.Integer(0))
chargeDetail.setComponentByName('ChargeUnits', univ.Integer(1))
chargeDetailTimeStamp = TimeStamp()
chargeDetail.setComponentByName('ChargeDetailTimeStamp', chargeDetailTimeStamp)
chargeDetailTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031045))
chargeDetailTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

mobileTerminatedCall.setComponentByName('BasicServiceUsedList', basicServiceUsedList)

operatorSpecInformation = OperatorSpecInformation()
mobileTerminatedCall.setComponentByName('OperatorSpecInformation', operatorSpecInformation)
operatorSpecInformation.setComponentByName('OperatorSpecInformation', char.VisibleString('ORP_V:GSM4-4'))











mobileOriginatedCall = MobileOriginatedCall()
basicCallInformation = BasicCallInformation()
chargeableSubscriber = ChargeableSubscriber()
simchargeableSubscriber = SimChargeableSubscriber()
simchargeableSubscriber.setComponentByName('Imsi', univ.Integer(646040222092540))
simchargeableSubscriber.setComponentByName('Msisdn', univ.Integer(261340383333))
chargeableSubscriber.setComponentByName('SimChargeableSubscriber', simchargeableSubscriber)
basicCallInformation.setComponentByName('ChargeableSubscriber', chargeableSubscriber)

destination = Destination()
basicCallInformation.setComponentByName('Destination', destination)
destination.setComponentByName('CalledNumber', univ.Integer(261340010000))
destination.setComponentByName('DialedDigits', univ.Integer(447786205094))
destination.setComponentByName('SMSDestinationNumber', univ.Integer(447786205094))
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
equipmentIdentifier.setComponentByName('Imei', univ.Integer(359176077876071))
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
serviceCode.setComponentByName('TeleserviceCode', univ.Integer(22))

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
chargeDetail.setComponentByName('ChargeUnits', univ.Integer(1))
chargeDetailTimeStamp = TimeStamp()
chargeDetail.setComponentByName('ChargeDetailTimeStamp', chargeDetailTimeStamp)
chargeDetailTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031413))
chargeDetailTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

mobileOriginatedCall.setComponentByName('BasicServiceUsedList', basicServiceUsedList)

operatorSpecInformation = OperatorSpecInformation()
mobileOriginatedCall.setComponentByName('OperatorSpecInformation', operatorSpecInformation)
operatorSpecInformation.setComponentByName('OperatorSpecInformation', char.VisibleString('ORP_V:GSM4-5'))











mobileTerminatedCall5 = MobileTerminatedCall()
basicCallInformation = BasicCallInformation()
chargeableSubscriber = ChargeableSubscriber()
simchargeableSubscriber = SimChargeableSubscriber()
simchargeableSubscriber.setComponentByName('Imsi', univ.Integer(646040233830418))
simchargeableSubscriber.setComponentByName('Msisdn', univ.Integer(261346052320))
chargeableSubscriber.setComponentByName('SimChargeableSubscriber', simchargeableSubscriber)
basicCallInformation.setComponentByName('ChargeableSubscriber', chargeableSubscriber)

callOriginator = CallOriginator()
basicCallInformation.setComponentByName('CallOriginator', callOriginator)
callOriginator.setComponentByName('CallingNumber', univ.Integer(261340010000))
callOriginator.setComponentByName('SMSOriginator', univ.Integer(261388230377))
mobileTerminatedCall.setComponentByName('BasicCallInformation', basicCallInformation)

callEventStartTimeStamp = TimeStamp()
callEventStartTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031219))
callEventStartTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicCallInformation.setComponentByName('TotalCallEventDuration', univ.Integer(0))
basicCallInformation.setComponentByName('CallEventStartTimeStamp', callEventStartTimeStamp)

locationInformation = LocationInformation()
networklocation = NetworkLocation()
networklocation.setComponentByName('RecEntityCode', univ.Integer(1))
networklocation.setComponentByName('CallReference', univ.Integer(4211819))
networklocation.setComponentByName('LocationArea', univ.Integer(790))
networklocation.setComponentByName('CellId', univ.Integer(63717))
locationInformation.setComponentByName('NetworkLocation', networklocation)
mobileTerminatedCall.setComponentByName('LocationInformation', locationInformation)

equipmentIdentifier = EquipmentIdentifier()
equipmentIdentifier.setComponentByName('Imei', univ.Integer(359802100040894))
mobileTerminatedCall.setComponentByName('EquipmentIdentifier', equipmentIdentifier)

basicServiceUsedList = BasicServiceUsedList()
basicServiceUsed = BasicServiceUsed()
basicService = BasicService()

chargingTimeStamp = TimeStamp()
chargeInformationList = ChargeInformationList()

serviceCode = ServiceCode()

basicServiceUsed.setComponentByName('BasicService', basicService)
basicServiceUsedList.setComponents(basicServiceUsed)
basicService.setComponentByName('ServiceCode', serviceCode)
serviceCode.setComponentByName('TeleserviceCode', univ.Integer(21))

basicServiceUsed.setComponentByName('ChargingTimeStamp', chargingTimeStamp)
chargingTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031219))
chargingTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

basicServiceUsed.setComponentByName('ChargeInformationList', chargeInformationList)
chargeInformation = ChargeInformation()
chargeInformationList.setComponents(chargeInformation)
chargeInformation.setComponentByName('ChargedItem', char.VisibleString('E'))
chargeInformation.setComponentByName('ExchangeRateCode', univ.Integer(0))
chargeDetailList = ChargeDetailList()
chargeInformation.setComponentByName('ChargeDetailList', chargeDetailList)
chargeDetail = ChargeDetail()
chargeDetailList.setComponents(chargeDetail)
chargeDetail.setComponentByName('ChargeType', univ.Integer(00))
chargeDetail.setComponentByName('Charge', univ.Integer(0))
chargeDetail.setComponentByName('ChargeUnits', univ.Integer(1))
chargeDetailTimeStamp = TimeStamp()
chargeDetail.setComponentByName('ChargeDetailTimeStamp', chargeDetailTimeStamp)
chargeDetailTimeStamp.setComponentByName('LocalTimeStamp', univ.Integer(20230503031219))
chargeDetailTimeStamp.setComponentByName('UtcTimeOffsetCode', univ.Integer(0))

mobileTerminatedCall.setComponentByName('BasicServiceUsedList', basicServiceUsedList)

operatorSpecInformation = OperatorSpecInformation()
mobileTerminatedCall.setComponentByName('OperatorSpecInformation', operatorSpecInformation)
operatorSpecInformation.setComponentByName('OperatorSpecInformation', char.VisibleString('ORP_V:GSM4-6'))










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

callEventdetails.setComponents(mobileTerminatedCall, mobileTerminatedCall2, mobileTerminatedCall3, mobileTerminatedCall4, mobileOriginatedCall, mobileTerminatedCall5 )

transferBatch.setComponentByName('CallEventdetails', callEventdetails)


transferBatch.setComponentByName('AuditControlInfo', auditControlInfo)
dataInterChange.setComponentByName('TransferBatch', transferBatch)

# Append the record to the list
tap_record = encoder.encode(dataInterChange)

filepath = file_utils.get_file_path("demo", "tap")
with open(filepath, "wb") as tap_file:
    tap_file.write(tap_record)
