from record import Record
from pyasn1.codec.der import encoder
import file_utils

cdr_records = []
cdrpath = file_utils.get_file_path("cdr", "txt")
with open(cdrpath, 'r') as file:
    cdr_records = file.readlines()
    
tap_records = []
for cdr_record in cdr_records:
    cdr_record = cdr_record.strip()
    cdr_fields = cdr_record.split("|")
    cdr_type = 1
    call_id = cdr_fields[2] + cdr_fields[3]
    originating_num = cdr_fields[5].strip()
    terminating_num = cdr_fields[6].strip()
    service_class = cdr_fields[7]
    origination_time = cdr_fields[2] + cdr_fields[3]
    termination_time = cdr_fields[2] + cdr_fields[3]
    call_duration = int(cdr_fields[8])
    cause_code = cdr_fields[9]
    calling_party_id = cdr_fields[10]
    called_party_id = cdr_fields[11]
    recording_entity = "FF"
    location = "FF"
    recording_session_id = "0000"
    node_address = "FF"
    
    # create Record object
    record = Record()
    record.setComponentByName('cdrType', cdr_type)
    record.setComponentByName('callId', call_id)
    record.setComponentByName('originatingNum', originating_num)
    record.setComponentByName('terminatingNum', terminating_num)
    record.setComponentByName('serviceClass', service_class)
    record.setComponentByName('originationTime', origination_time)
    record.setComponentByName('terminationTime', termination_time)
    record.setComponentByName('callDuration', call_duration)
    record.setComponentByName('causeCode', cause_code)
    record.setComponentByName('callingPartyId', calling_party_id)
    record.setComponentByName('calledPartyId', called_party_id)
    record.setComponentByName('recordingEntity', recording_entity)
    record.setComponentByName('location', location)
    record.setComponentByName('recordingSessionId', recording_session_id)
    record.setComponentByName('nodeAddress', node_address)
    
    tap_record = encoder.encode(record)
    tap_records.append(tap_record)

# write records into encoded tap file

filepath = file_utils.get_file_path("demo", "tap")
print(filepath)
with open(filepath, "wb") as tap_file:
    for tap_record in tap_records:
        tap_file.write(tap_record)
