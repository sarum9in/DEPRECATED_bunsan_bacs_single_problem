import decimal

def multiple(multiplificator, *dicts):
    ret = dict()
    for d in dicts:
        for key, arg in d.items():
            ret[key] = multiplificator(arg)
    return ret


def power_multiplificator(base):
    def multiplificator(exponent):
        return lambda x: x*decimal.getcontext().power(base, exponent)
    return multiplificator


_si_multiple = \
{
    "da": 1,
    "h": 2,
    "k": 3,
    "M": 6,
    "G": 9,
    "T": 12,
    "P": 15,
    "E": 18,
    "Z": 21,
    "Y": 24
}


_si_submultiple = \
{
    "d": -1,
    "c": -2,
    "m": -3,
    "µ": -6,
    "mu": -6,
    "n": -9,
    "p": -12,
    "f": -15,
    "a": -18,
    "z": -21,
    "y": -24
}


_binary_muliple = \
{
    "Ki": 10,
    "Mi": 20,
    "Gi": 30,
    "Ti": 40,
    "Pi": 50,
    "Ei": 60,
    "Zi": 70,
    "Yi": 80
}


si_multiple = multiple(power_multiplificator(10), _si_multiple, _si_submultiple)
binary_multiple = multiple(power_multiplificator(2), _binary_muliple)
