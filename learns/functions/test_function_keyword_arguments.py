def test_function(first_arg, *args, **keyword):
    print('first_arg: ', first_arg)
    print('args: ', args)
    print('keyword: ', keyword)


test_function(
    'first param',
    'second param',
    'third param',
    fourth_param_name='fourth named param',
    fifth_param_name='fifth named param',
)
