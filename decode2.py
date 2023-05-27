from pyasn1.codec.ber import decoder
from pyasn1_modules import rfc1155, rfc1157, rfc1902

with open('CDFRAF1MDGTM42711', 'rb') as file:
    ber_encoded_data = file.read()

# Decode the BER-encoded data
decoded_data, _ = decoder.decode(ber_encoded_data, asn1Spec=rfc1155.ObjectName())

# Access and extract the desired information from the decoded data
# Modify the code based on the structure defined in the ASN.1 specification
basic_call_information = decoded_data['basicCallInformation']
location_information = decoded_data['locationInformation']