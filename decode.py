from pyasn1.codec.der import decoder
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
    print(record)
    
# Write the decoded records to a CSV file
cdrpath = file_utils.get_file_path("cdr", "csv")
with open(cdrpath, "w", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(["cdrType", "callId", "originatingNum", "terminatingNum", "serviceClass", "originationTime", "terminationTime", "callDuration", "causeCode", "callingPartyId", "calledPartyId", "recordingEntity", "location", "recordingSessionId", "nodeAddress"])
    for record in record_list:
        row = [
            record.getComponentByName("cdrType"),
            record.getComponentByName("callId"),
            record.getComponentByName("originatingNum"),
            record.getComponentByName("terminatingNum"),
            record.getComponentByName("serviceClass"),
            record.getComponentByName("originationTime"),
            record.getComponentByName("terminationTime"),
            record.getComponentByName("callDuration"),
            record.getComponentByName("causeCode"),
            record.getComponentByName("callingPartyId"),
            record.getComponentByName("calledPartyId"),
            record.getComponentByName("recordingEntity"),
            record.getComponentByName("location"),
            record.getComponentByName("recordingSessionId"),
            record.getComponentByName("nodeAddress")
        ]
        writer.writerow(row)
