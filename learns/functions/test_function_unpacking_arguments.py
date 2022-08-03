# In the same fashion, dictionaries can deliver keyword arguments with the **-operator:
def function_that_receives_names_arguments(first_word, second_word):
    return first_word + ', ' + second_word + '!'


arguments = {'first': 'anh', 'second': 'huy'}
print('function_that_receives_names_arguments: ', function_that_receives_names_arguments(*arguments))
