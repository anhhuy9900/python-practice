def test_sets():
    """Sets"""
    fruits_set = {"apple", "banana", "cherry"}


def test_set_methods():
    """Set methods"""

    fruits_set = {"apple", "banana", "cherry"}
    print('type of fruits_set: ', type(fruits_set))

    # You may check if the item is in set by using "in" statement
    check = 'apple' in fruits_set
    print('apple in fruits_set: ', check)

    # You can use the add() object method to add an item.
    fruits_set.add('mango')
    print('fruits_set.add: ', fruits_set)

    # Use remove() method to remove an item.
    fruits_set.remove('banana')
    print('fruits_set.remove: ', fruits_set)

test_set_methods()