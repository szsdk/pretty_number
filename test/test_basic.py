from context import pretty_number as pn


def test_pretty_float():
    assert pn.pretty_float(0.00003243) == '3.2430 × 10⁻⁵'
    assert pn.pretty_float(0.243) == '0.2430'
