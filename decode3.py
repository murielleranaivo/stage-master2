from tap import parser

tap_file = 'CDFRAF1MDGTM42711'
tap_parser = parser.Parser()

for line in tap_parser.parse_file(tap_file):
    print(line)
    