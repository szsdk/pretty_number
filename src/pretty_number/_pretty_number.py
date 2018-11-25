from math import floor, log10
_to_super = dict(zip("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻"))


def pretty_float(f, significant=4):
    if significant is None and decimal is None:
        decimal = 3
    exponet = floor(log10(f))
    s_exp = ''.join([_to_super[i] for i in str(exponet)])
    m = f * 10 ** (-exponet)

    if -3 < exponet < significant:
        return f"{{:,.{significant-exponet-1}f}}".format(f)
    return f"%1.{significant-1}f × 10{s_exp}" % m


def pretty_int(i):
    return '{:,}'.format(i)


def pretty_number(n):
    if isinstance(n, int):
        return pretty_int(n)
    if isinstance(n, float):
        return pretty_float(n)
