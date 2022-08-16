test_variable = 'initial global value'


def test_function_scopes():
    """Scopes and Namespaces Example"""

    def do_local():
        test_variable = 'local variable'
        return test_variable

    # def do_non_local():
    #     nonlocal test_variable
    #     test_variable = 'nonlocal value'
    #     return test_variable

    def do_global():
        # Address the variable from very global scope and try to change it.
        # pylint: disable=redefined-outer-name,global-statement
        global test_variable
        test_variable = 'global value'
        return test_variable

    do_local()
    print('do_local - test_variable: ', test_variable)

    # do_non_local()
    # print('do_non_local - test_variable: ', test_variable)

    do_global()
    print('do_global - test_variable: ', test_variable)


test_function_scopes()