
class BasicServiceUsed(univ.Enumerated):
    namedValues = namedval.NamedValues(
        ('voice', 0),
        ('sms', 1),
        ('data', 2),
        ('fax', 3)
    )

