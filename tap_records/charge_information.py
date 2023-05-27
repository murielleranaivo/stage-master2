from pyasn1.type import univ, namedtype, char

from tap_records.call_type_group import CallTypeGroup

class ChargeInformation(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('ChargedItem', char.VisibleString()),
        namedtype.NamedType('ExchangeRateCode', univ.Integer()),
        namedtype.NamedType('CallTypeGroup', CallTypeGroup()),
        namedtype.NamedType('ChargeDetailList', univ.SequenceOf(
            componentType=univ.Sequence(
                componentType=namedtype.NamedTypes(
                    namedtype.NamedType('ChargeType', univ.Integer()),
                    namedtype.NamedType('Charge', univ.Integer()),
                    namedtype.NamedType('ChargedUnits', univ.Integer()),
                    namedtype.NamedType('ChargeDetailTimeStamp', univ.Sequence(
                        componentType=namedtype.NamedTypes(
                            namedtype.NamedType('LocalTimeStamp', univ.Integer()),
                            namedtype.NamedType('UtcTimeOffsetCode', univ.Integer())
                        )
                    ))
                )
            )
        ))
    )