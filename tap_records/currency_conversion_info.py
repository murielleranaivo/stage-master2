from pyasn1.type import univ

from tap_records.currency_conversion import CurrencyConversion

class CurrencyConversionInfo(univ.SequenceOf):
    componentType = CurrencyConversion()

