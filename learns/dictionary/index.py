"""Dictionary"""

fruits_dictionary = {
    'cherry': 'red',
    'apple': 'green',
    'banana': 'yellow',
}
print("fruits_dictionary['cherry']: ", fruits_dictionary['cherry'])

# To check whether a single key is in the dictionary, use the in keyword.
print('apple in fruits_dictionary: ', 'apple' in fruits_dictionary)

# Performing list(d) on a dictionary returns a list of all the keys used in the dictionary,
# in insertion order (if you want it sorted, just use sorted(d) instead).
print('list(fruits_dictionary): ', list(fruits_dictionary))
print('sorted(fruits_dictionary): ', sorted(fruits_dictionary))