from record import Record
from pyasn1.type import univ
from pyasn1.type import char
from pyasn1.codec.ber import encoder
import file_utils
from encryption import encrypt_file

key = b'5fp1lg8_jZKwQFpBHH9F2QYRRc3fn8cFmSsZu33Z6PI='

def encode_records_to_tap(cdr_records):
    
    tap_records = []
    for cdr_record in cdr_records:
        
        # Create a Record object and set its components
        record = Record()
        record.setComponentByName('CALL_TYPE', univ.Integer(cdr_record.call_type))
        record.setComponentByName('SERVICE_CODE', univ.Integer(cdr_record.service_code))
        record.setComponentByName('NE_CODE', char.VisibleString(cdr_record.ne_code))
        record.setComponentByName('IN_ROUTE', char.VisibleString(cdr_record.in_route))
        record.setComponentByName('OUT_ROUTE', char.VisibleString(cdr_record.out_route))
        record.setComponentByName('IMSI', char.VisibleString(cdr_record.imsi))
        record.setComponentByName('SGSN_ADDRESS', char.VisibleString(cdr_record.sgsn_address))
        record.setComponentByName('A_NUMBER', char.VisibleString(cdr_record.a_number))
        record.setComponentByName('B_NUMBER', char.VisibleString(cdr_record.b_number))
        record.setComponentByName('C_NUMBER', char.VisibleString(cdr_record.c_number))
        record.setComponentByName('APN_ADDRESS', char.VisibleString(cdr_record.apn_address))
        record.setComponentByName('PDP_ADDRESS', char.VisibleString(cdr_record.pdp_address))
        record.setComponentByName('CALL_DATE', char.VisibleString(cdr_record.call_date))
        record.setComponentByName('CALL_DURATION', univ.Integer(cdr_record.call_duration))
        record.setComponentByName('DATA_VOLUME_INC', univ.Integer(cdr_record.data_volume_inc))
        record.setComponentByName('DATA_VOLUME_OUT', univ.Integer(cdr_record.data_volume_out))
        record.setComponentByName('TELESERVICE', char.VisibleString(cdr_record.teleservice))
        record.setComponentByName('BEARERSERVICE', char.VisibleString(cdr_record.bearerservice))
        record.setComponentByName('CAMEL_FLAG', char.VisibleString(cdr_record.camel_flag))
        record.setComponentByName('CAMEL_SERVICE_LEVEL', char.VisibleString(cdr_record.camel_service_level))
        record.setComponentByName('CAMEL_SERVICE_KEY', char.VisibleString(cdr_record.camel_service_key))
        record.setComponentByName('CAMEL_DEFAULT_CALL_HANDLING', char.VisibleString(cdr_record.camel_default_call_handling))
        record.setComponentByName('CAMEL_SERVER_ADDRESS', char.VisibleString(cdr_record.camel_server_address))
        record.setComponentByName('CAMEL_MSC_ADDRESS', char.VisibleString(cdr_record.camel_msc_address))
        record.setComponentByName('CAMEL_CALL_REF_NUM', char.VisibleString(cdr_record.camel_call_ref_num))
        record.setComponentByName('CAMEL_INIT_CF_INDICATOR', char.VisibleString(cdr_record.camel_init_cf_indicator))
        record.setComponentByName('CAMEL_DESTINATION_NUM', char.VisibleString(cdr_record.camel_destination_num))
        record.setComponentByName('CAMEL_MODIFICATION', char.VisibleString(cdr_record.camel_modification))
        record.setComponentByName('SUPPLIMENTARY_NUM', char.VisibleString(cdr_record.supplimentary_num))
        record.setComponentByName('NETWORK_TIME', char.VisibleString(cdr_record.network_time))
        record.setComponentByName('REASON_FOR_CLEARDOWN', char.VisibleString(cdr_record.reason_for_cleardown))
        record.setComponentByName('PARTIAL_INDICATOR', char.VisibleString(cdr_record.partial_indicator))
        record.setComponentByName('PARTIAL_SEQ_NUM', char.VisibleString(cdr_record.partial_seq_num))
        record.setComponentByName('IMEI_NUM', char.VisibleString(cdr_record.imei_num))
        record.setComponentByName('CHRONO_NUM', char.VisibleString(cdr_record.chrono_num))
        record.setComponentByName('CHARGING_ID', char.VisibleString(cdr_record.charging_id))
        record.setComponentByName('SUBSCRIBER_TYPE', char.VisibleString(cdr_record.subscriber_type))

        # Append the record to the list
        tap_record = encoder.encode(record)
        tap_records.append(tap_record)

    # write records into encoded tap file

    filepath = file_utils.get_file_path("demo", "tap")
    print(filepath)
    with open(filepath, "wb") as tap_file:
        for tap_record in tap_records:
            tap_file.write(tap_record)
            
    #encrypt_file(key, filepath, filepath)