from record import Record
from pyasn1.type import univ
from pyasn1.type import char
from pyasn1.codec.ber import encoder
import file_utils

cdr_records = []
cdrpath = file_utils.get_file_path("cdr", "txt")
with open(cdrpath, 'r') as file:
    cdr_records = file.readlines()
    
tap_records = []
for cdr_record in cdr_records:
    cdr_record = cdr_record.strip()
    cdr_fields = cdr_record.split("|")
    
    # Create a Record object and set its components
    record = Record()
    record.setComponentByName('CALL_TYPE', univ.Integer(int(cdr_fields[0])))
    record.setComponentByName('SERVICE_CODE', univ.Integer(int(cdr_fields[1])))
    record.setComponentByName('NE_CODE', char.VisibleString(cdr_fields[2]))
    record.setComponentByName('IN_ROUTE', char.VisibleString(cdr_fields[3]))
    record.setComponentByName('OUT_ROUTE', char.VisibleString(cdr_fields[4]))
    record.setComponentByName('IMSI', char.VisibleString(cdr_fields[5]))
    record.setComponentByName('SGSN_ADDRESS', char.VisibleString(cdr_fields[6]))
    record.setComponentByName('A_NUMBER', char.VisibleString(cdr_fields[7]))
    record.setComponentByName('B_NUMBER', char.VisibleString(cdr_fields[8]))
    record.setComponentByName('C_NUMBER', char.VisibleString(cdr_fields[9]))
    record.setComponentByName('APN_ADDRESS', char.VisibleString(cdr_fields[10]))
    record.setComponentByName('PDP_ADDRESS', char.VisibleString(cdr_fields[11]))
    record.setComponentByName('CALL_DATE', char.VisibleString(cdr_fields[12]))
    record.setComponentByName('CALL_DURATION', univ.Integer(int(cdr_fields[13])))
    record.setComponentByName('DATA_VOLUME_INC', univ.Integer(int(cdr_fields[14])))
    record.setComponentByName('DATA_VOLUME_OUT', univ.Integer(int(cdr_fields[15])))
    record.setComponentByName('TELESERVICE', char.VisibleString((cdr_fields[16])))
    record.setComponentByName('BEARERSERVICE', char.VisibleString((cdr_fields[17])))
    record.setComponentByName('CAMEL_FLAG', char.VisibleString(cdr_fields[18]))
    record.setComponentByName('CAMEL_SERVICE_LEVEL', char.VisibleString(cdr_fields[19]))
    record.setComponentByName('CAMEL_SERVICE_KEY', char.VisibleString(cdr_fields[20]))
    record.setComponentByName('CAMEL_DEFAULT_CALL_HANDLING', char.VisibleString(cdr_fields[21]))
    record.setComponentByName('CAMEL_SERVER_ADDRESS', char.VisibleString(cdr_fields[22]))
    record.setComponentByName('CAMEL_MSC_ADDRESS', char.VisibleString(cdr_fields[23]))
    record.setComponentByName('CAMEL_CALL_REF_NUM', char.VisibleString(cdr_fields[24]))
    record.setComponentByName('CAMEL_INIT_CF_INDICATOR', char.VisibleString(cdr_fields[25]))
    record.setComponentByName('CAMEL_DESTINATION_NUM', char.VisibleString(cdr_fields[26]))
    record.setComponentByName('CAMEL_MODIFICATION', char.VisibleString(cdr_fields[27]))
    record.setComponentByName('SUPPLIMENTARY_NUM', char.VisibleString(cdr_fields[28]))
    record.setComponentByName('NETWORK_TIME', char.VisibleString(cdr_fields[29]))
    record.setComponentByName('REASON_FOR_CLEARDOWN', char.VisibleString(cdr_fields[30]))
    record.setComponentByName('PARTIAL_INDICATOR', char.VisibleString(cdr_fields[31]))
    record.setComponentByName('PARTIAL_SEQ_NUM', char.VisibleString(cdr_fields[32]))
    record.setComponentByName('IMEI_NUM', char.VisibleString(cdr_fields[33]))
    record.setComponentByName('CHRONO_NUM', char.VisibleString(cdr_fields[34]))
    record.setComponentByName('CHARGING_ID', char.VisibleString(cdr_fields[35]))
    record.setComponentByName('SUBSCRIBER_TYPE', char.VisibleString(cdr_fields[36]))

    # Append the record to the list
    tap_record = encoder.encode(record)
    tap_records.append(tap_record)

# write records into encoded tap file

filepath = file_utils.get_file_path("demo", "tap")
print(filepath)
with open(filepath, "wb") as tap_file:
    for tap_record in tap_records:
        tap_file.write(tap_record)
