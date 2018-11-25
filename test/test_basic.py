from context import pretty_number as pn


def test_pretty_float():
    assert pn.pretty_float(0.00003243) == '3.243 × 10⁻⁵'
    assert pn.pretty_float(0.243) == '0.2430'
    assert pn.pretty_float(0.243, significant=2) == '0.24'
    assert pn.pretty_float(1.243, significant=2) == '1.2'
    assert pn.pretty_float(10, significant=2) == '10'
    assert pn.pretty_float(1000, significant=2) == '1.0 × 10³'
    assert pn.pretty_float(1243, significant=2) == '1.2 × 10³'
    assert pn.pretty_float(0.1, significant=2) == '0.10'
    assert pn.pretty_float(0.01, significant=2) == '0.010'
    assert pn.pretty_float(0.001, significant=2) == '1.0 × 10⁻³'
    assert pn.pretty_float(0.0012345, significant=2) == '1.2 × 10⁻³'
    assert pn.pretty_float(12345.678, significant=10) == '12,345.67800'
    assert pn.pretty_float(12345.678, significant=4) == '1.235 × 10⁴'

def test_pretty_int():
    assert pn.pretty_int(1234) == '1,234'
