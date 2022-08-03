def test_tuples():
    """Tuples"""
    fruits_tuple = ("apple", "banana", "cherry")
    print('fruits_tuple[0]: ', fruits_tuple[0])

    # It is also possible to omit brackets when initializing tuples.
    another_tuple = 12345, 54321, 'hello!'
    print('another_tuple: ', another_tuple)

    # Tuples may be nested:
    nested_tuple = another_tuple, (1, 2, 3, 4)
    print('nested_tuple: ', nested_tuple)

    # The following example is called tuple packing:
    package_tuple = 'nguyen', 'hoang', 'anh', 'huy'
    print('package_tuple: ', package_tuple)

    print('len of tuple: ', len(fruits_tuple))

test_tuples()