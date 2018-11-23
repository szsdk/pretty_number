from math import floor, log10
_to_super = dict(zip("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻"))


def pretty_float(f):
    exponet = floor(log10(f))
    if -2 < exponet <= 3:
        return f"{f:.4f}"
    m = f * 10 ** (-exponet)
    s_exp = ''.join([_to_super[i] for i in str(exponet)])
    return f"{m:.4f} × 10{s_exp}"


def pretty_int(i):
    return '{:,}'.format(i)


def pretty_number(n):
    if isinstance(n, int):
        return pretty_int(n)
    if isinstance(n, float):
        return pretty_float(n)
