def test_list_type():
    """List type."""
    squares = [1, 4, 9, 16, 25]

    print('squares is list type: ', isinstance(squares, list))
    print('squares[0] : ', squares[0])
    print('squares[-1]: ', squares[-1])
    print('slicing returns a new list: ', squares[:3])
    print('slicing returns a new list squares[:-3]: ', squares[:-3])

    # Lists also support operations like concatenation:
    print('operations like concatenation: ', squares + [36, 49, 64, 81, 100] == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

    # the append() method
    cubes = [1, 8, 27, 65, 125]
    cubes.append(100)
    print('cubes.append: ', cubes)

    # Assignment to slices is also possible, and this can even change the size
    # of the list or clear it entirely:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    letters[2:5] = ['C', 'D', 'E']  # replace some values
    letters[3:6] = ['huy', 'hoa', 'hieu']
    print('replace some values:', letters)
    # clear the list by replacing all the elements with an empty list
    empty_letters = letters[:] = []
    print('empty_letters:', empty_letters)

    # The built-in function len() also applies to lists
    letters = ['a', 'b', 'c', 'd']
    print('len of letters: ', len(letters))


def test_list_methods():
    """Test list methods."""
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.append(x)
    # Add an item to the end of the list.
    # Equivalent to a[len(a):] = [x].
    fruits.append('grape')
    print('list.append: ', fruits)

    # list.remove(x)
    fruits.remove('grape')
    print('list.remove: ', fruits)

    # list.insert(i, x)
    # Insert an item at a given position. The first argument is the index of the element
    fruits.insert(5, 'huy')
    print('list.insert: ', fruits)

    # list.index(x[, start[, end]])
    print('list.index: ', fruits.index('pear'))

    # list.count(x)
    # Return a shallow copy of the list. Equivalent to a[:].
    print('list.count: ', fruits.count('banana'))

    # list.copy()
    # Return a shallow copy of the list. Equivalent to a[:].
    fruits_copy = fruits.copy()
    print('fruits_copy: ', fruits_copy)
    fruits_2 = ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    fruits_copy.reverse()
    # list.reverse()
    print('list.reverse(): ', fruits_copy)
    print('list.reverse => ::-1 ', fruits_copy[::-1])

    # list.sort(key=None, reverse=False)
    fruits_copy.sort()
    print('list.sort(): ', fruits_copy)

    # list.pop([i])
    # Remove the item at the given position in the list, and return it. If no index is specified,
    fruits_copy.pop(2)
    print('list.pop(): ', fruits_copy)

    # list.clear()
    # Remove all items from the list. Equivalent to del a[:].
    fruits_copy.clear()
    print('list.clear(): ', fruits_copy)


def test_del_statement():
    """The del statement"""

    numbers = [-1, 1, 66.25, 333, 333, 1234.5]

    del numbers[0]
    print('del numbers[0]: ', numbers)

    del numbers[2:5]
    print('del numbers[2:5]: ', numbers)


def test_list_comprehensions():
    """List Comprehensions."""

    arr_number = []
    for number in range(10):
        arr_number.append(number ** 2)
    print('arr_number: ', arr_number)

    # or, equivalently (which is more concise and readable):
    print('equivalently => arr_number: ', [number * 2 for number in range(10)])

    # For example, this listcomp combines the elements of two lists if they are not equal.
    combinations = [x for x in range(10) if x % 2 == 0]
    print('combinations :', combinations)

    combinations_x_y = [(x, y) for x in [1, 2, 3] for y in [2, 3, 1] if x != y]
    print('combinations_x_y :', combinations_x_y)

    # Flatten a list using a listcomp with two 'for'.
    vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print('Flatten a list: ', [el for num in vector for el in num])


def test_nested_list_comprehensions():
    """Nested List Comprehensions"""

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    # As we saw in the previous section, the nested listcomp is evaluated in the context of the
    # for that follows it, so this example is equivalent to:
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])
    print('transposed: ', transposed)


test_nested_list_comprehensions()