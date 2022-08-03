"""Boolean"""

def test_booleans():
    true_boolean = True
    false_boolean = False

    assert true_boolean
    assert not false_boolean

    assert isinstance(true_boolean, bool)
    assert isinstance(false_boolean, bool)

    # Let's try to cast boolean to string.
    assert str(true_boolean) == "True"
    assert str(false_boolean) == "False"


def test_float_numbers():
    """Float type
    Float, or "floating point number" is a number, positive or negative,
    containing one or more decimals.
    """

    float_number = 7.0
    # Another way of declaring float is using float() function.
    float_number_via_function = float(7)
    float_negative = -35.59

    assert float_number == float_number_via_function
    assert isinstance(float_number, float)
    assert isinstance(float_number_via_function, float)
    assert isinstance(float_negative, float)

def test_number_operators():
    """Basic operations"""

    # Addition.
    assert 2 + 4 == 6

    # Multiplication.
    assert 2 * 4 == 8

    # Division always returns a floating point number.
    assert 12 / 3 == 4.0
    assert 12 / 5 == 2.4
    assert 17 / 3 == 5.666666666666667

    # Modulo operator returns the remainder of the division.
    assert 12 % 3 == 0
    assert 13 % 3 == 1

    # Floor division discards the fractional part.
    assert 17 // 3 == 5

    # Raising the number to specific power.
    assert 5 ** 2 == 25  # 5 squared
    assert 2 ** 7 == 128  # 2 to the power of 7

    # There is full support for floating point; operators with
    # mixed type operands convert the integer operand to floating point.
    assert 4 * 3.75 - 1 == 14.0
