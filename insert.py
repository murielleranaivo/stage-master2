from datetime import datetime
from pyasn1.codec.der import decoder
from models.CdrModel import CdrModel
from providers import get_db
from record import Record

db = get_db()

# Function to parse the date string into a datetime object
def parse_date(date_string):
    return datetime.strptime(date_string, '%Y%m%d%H%M%S')

def insert_cdrs_to_db(cdrpath):
    cdr_records = []
    with open(cdrpath, 'r') as file:
        cdr_records = file.readlines()
        
    records = []
    for cdr_record in cdr_records:
        cdr_record = cdr_record.strip()
        cdr_fields = cdr_record.split("|")
        record = CdrModel(
            call_type=int(cdr_fields[0]),
            service_code=int(cdr_fields[1]),
            ne_code=cdr_fields[2].strip(),
            in_route=cdr_fields[3].strip(),
            out_route=cdr_fields[4].strip(),
            imsi=cdr_fields[5].strip(),
            sgsn_address=cdr_fields[6].strip(),
            a_number=cdr_fields[7].strip(),
            b_number=cdr_fields[8].strip(),
            c_number=cdr_fields[9].strip(),
            apn_address=cdr_fields[10].strip(),
            pdp_address=cdr_fields[11].strip(),
            call_date=parse_date(cdr_fields[12]),
            call_duration=int(cdr_fields[13]),
            data_volume_inc=int(cdr_fields[14]),
            data_volume_out=int(cdr_fields[15]),
            teleservice=cdr_fields[16].strip(),
            bearerservice=cdr_fields[17].strip(),
            camel_flag=cdr_fields[18].strip(),
            camel_service_level=cdr_fields[19].strip(),
            camel_service_key=cdr_fields[20].strip(),
            camel_default_call_handling=cdr_fields[21].strip(),
            camel_server_address=cdr_fields[22].strip(),
            camel_msc_address=cdr_fields[23].strip(),
            camel_call_ref_num=cdr_fields[24].strip(),
            camel_init_cf_indicator=cdr_fields[25].strip(),
            camel_destination_num=cdr_fields[26].strip(),
            camel_modification=cdr_fields[27].strip(),
            supplimentary_num=cdr_fields[28].strip(),
            network_time=cdr_fields[29].strip(),
            reason_for_cleardown=cdr_fields[30].strip(),
            partial_indicator=cdr_fields[31].strip(),
            partial_seq_num=cdr_fields[32].strip(),
            imei_num=cdr_fields[33].strip(),
            chrono_num=cdr_fields[34].strip(),
            charging_id=cdr_fields[35].strip(),
            subscriber_type=cdr_fields[36].strip()
        )
        records.append(record)
        
    db.session.add_all(records)
    db.session.commit()

def insert_tap_to_db(cdrpath):
    
    with open(cdrpath, 'rb') as f:
        # Read the binary data from the file
        binary_data = f.read()

    # Decode each binary record
    record_list = []
    while binary_data:
        # Decode the binary data using the Record class
        record, binary_data = decoder.decode(binary_data, asn1Spec=Record())
        # Append the decoded record to the list
        record_list.append(record)
        
    cdr_models = []
    for record in record_list:
        cdr_model = CdrModel(
            call_type=int(record.getComponentByName("CALL_TYPE")),
            service_code=int(record.getComponentByName("SERVICE_CODE")),
            ne_code=record.getComponentByName("NE_CODE"),
            in_route=record.getComponentByName("IN_ROUTE"),
            out_route=record.getComponentByName("OUT_ROUTE"),
            imsi=record.getComponentByName("IMSI"),
            sgsn_address=record.getComponentByName("SGSN_ADDRESS"),
            a_number=record.getComponentByName("A_NUMBER"),
            b_number=record.getComponentByName("B_NUMBER"),
            c_number=record.getComponentByName("C_NUMBER"),
            apn_address=record.getComponentByName("APN_ADDRESS"),
            pdp_address=record.getComponentByName("PDP_ADDRESS"),
            call_date=record.getComponentByName("CALL_DATE"),
            call_duration=int(record.getComponentByName("CALL_DURATION")),
            data_volume_inc=int(record.getComponentByName("DATA_VOLUME_INC")),
            data_volume_out=int(record.getComponentByName("DATA_VOLUME_OUT")),
            teleservice=record.getComponentByName("TELESERVICE"),
            bearerservice=record.getComponentByName("BEARERSERVICE"),
            camel_flag=record.getComponentByName("CAMEL_FLAG"),
            camel_service_level=record.getComponentByName("CAMEL_SERVICE_LEVEL"),
            camel_service_key=record.getComponentByName("CAMEL_SERVICE_KEY"),
            camel_default_call_handling=record.getComponentByName("CAMEL_DEFAULT_CALL_HANDLING"),
            camel_server_address=record.getComponentByName("CAMEL_SERVER_ADDRESS"),
            camel_msc_address=record.getComponentByName("CAMEL_MSC_ADDRESS"),
            camel_call_ref_num=record.getComponentByName("CAMEL_CALL_REF_NUM"),
            camel_init_cf_indicator=record.getComponentByName("CAMEL_INIT_CF_INDICATOR"),
            camel_destination_num=record.getComponentByName("CAMEL_DESTINATION_NUM"),
            camel_modification=record.getComponentByName("CAMEL_MODIFICATION"),
            supplimentary_num=record.getComponentByName("SUPPLIMENTARY_NUM"),
            network_time=record.getComponentByName("NETWORK_TIME"),
            reason_for_cleardown=record.getComponentByName("REASON_FOR_CLEARDOWN"),
            partial_indicator=record.getComponentByName("PARTIAL_INDICATOR"),
            partial_seq_num=record.getComponentByName("PARTIAL_SEQ_NUM"),
            imei_num=record.getComponentByName("IMEI_NUM"),
            chrono_num=record.getComponentByName("CHRONO_NUM"),
            charging_id=record.getComponentByName("CHARGING_ID"),
            subscriber_type=record.getComponentByName("SUBSCRIBER_TYPE")
        )
        cdr_models.append(cdr_model)
    
    db.session.add_all(cdr_models)
    db.session.commit()
