from pyasn1.codec.der import decoder
from datetime import datetime
from record import Record
import file_utils
import csv

# Open the file for reading
filepath = file_utils.get_file_path("demo", "tap")
print(filepath)
with open(filepath, 'rb') as f:
    # Read the binary data from the file
    binary_data = f.read()

# Decode each binary record
record_list = []
while binary_data:
    # Decode the binary data using the Record class
    record, binary_data = decoder.decode(binary_data, asn1Spec=Record())
    # Append the decoded record to the list
    record_list.append(record)

# Print the decoded records
for record in record_list:
    print(record.prettyPrint())

# Write the decoded records to a CSV file
cdrpath = file_utils.get_file_path("cdr", "csv")
with open(cdrpath, "w", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow([
        "CALL_TYPE", "SERVICE_CODE", "NE_CODE", "IN_ROUTE", "OUT_ROUTE", "IMSI", "SGSN_ADDRESS", "A_NUMBER", "B_NUMBER",
        "C_NUMBER", "APN_ADDRESS", "PDP_ADDRESS", "CALL_DATE", "CALL_DURATION", "DATA_VOLUME_INC", "DATA_VOLUME_OUT",
        "TELESERVICE", "BEARERSERVICE", "CAMEL_FLAG", "CAMEL_SERVICE_LEVEL", "CAMEL_SERVICE_KEY",
        "CAMEL_DEFAULT_CALL_HANDLING", "CAMEL_SERVER_ADDRESS", "CAMEL_MSC_ADDRESS", "CAMEL_CALL_REF_NUM",
        "CAMEL_INIT_CF_INDICATOR", "CAMEL_DESTINATION_NUM", "CAMEL_MODIFICATION", "SUPPLEMENTARY_NUM", "NETWORK_TIME",
        "REASON_FOR_CLEARDOWN", "PARTIAL_INDICATOR", "PARTIAL_SEQ_NUM", "IMEI_NUM", "CHRONO_NUM", "CHARGING_ID",
        "SUBSCRIBER_TYPE"
    ])
    for record in record_list:
        call_date = record.getComponentByName("CALL_DATE")
        if call_date:
            try:
                call_date = call_date.asOctets().decode()  # Convert VisibleString to string
                call_date = datetime.strptime(call_date, "%Y%m%d%H%M%S")
            except ValueError:
                call_date = None
        else:
            call_date = ""
        
        row = [
            record.getComponentByName("CALL_TYPE"),
            record.getComponentByName("SERVICE_CODE"),
            record.getComponentByName("NE_CODE"),
            record.getComponentByName("IN_ROUTE"),
            record.getComponentByName("OUT_ROUTE"),
            record.getComponentByName("IMSI"),
            record.getComponentByName("SGSN_ADDRESS"),
            record.getComponentByName("A_NUMBER"),
            record.getComponentByName("B_NUMBER"),
            record.getComponentByName("C_NUMBER"),
            record.getComponentByName("APN_ADDRESS"),
            record.getComponentByName("PDP_ADDRESS"),
            call_date,
            record.getComponentByName("CALL_DURATION"),
            record.getComponentByName("DATA_VOLUME_INC"),
            record.getComponentByName("DATA_VOLUME_OUT"),
            record.getComponentByName("TELESERVICE"),
            record.getComponentByName("BEARERSERVICE"),
            record.getComponentByName("CAMEL_FLAG"),
            record.getComponentByName("CAMEL_SERVICE_LEVEL"),
            record.getComponentByName("CAMEL_SERVICE_KEY"),
            record.getComponentByName("CAMEL_DEFAULT_CALL_HANDLING"),
            record.getComponentByName("CAMEL_SERVER_ADDRESS"),
            record.getComponentByName("CAMEL_MSC_ADDRESS"),
            record.getComponentByName("CAMEL_CALL_REF_NUM"),
            record.getComponentByName("CAMEL_INIT_CF_INDICATOR"),
            record.getComponentByName("CAMEL_DESTINATION_NUM"),
            record.getComponentByName("CAMEL_MODIFICATION"),
            record.getComponentByName("SUPPLIMENTARY_NUM"),
            record.getComponentByName("NETWORK_TIME"),
            record.getComponentByName("REASON_FOR_CLEARDOWN"),
            record.getComponentByName("PARTIAL_INDICATOR"),
            record.getComponentByName("PARTIAL_SEQ_NUM"),
            record.getComponentByName("IMEI_NUM"),
            record.getComponentByName("CHRONO_NUM"),
            record.getComponentByName("CHARGING_ID"),
            record.getComponentByName("SUBSCRIBER_TYPE")
        ]
        writer.writerow(row)