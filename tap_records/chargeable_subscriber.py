from pyasn1.type import univ, namedtype

from tap_records.sim_chargeable_subscriber import SimChargeableSubscriber

class ChargeableSubscriber(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('simChargeableSubscriber', SimChargeableSubscriber()),
    )
