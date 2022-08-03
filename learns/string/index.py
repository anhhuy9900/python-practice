my_str = 'How I can do that'
print('my_str: ', my_str)

# type of string
print('type of string: ', type(my_str))

# len of string
print('len of string: ', len(my_str))

str_long = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n'
            'Pellentesque eget tincidunt felis. Ut ac vestibulum est.')
print('str_long: ', str_long)

# str_replace
my_str_replace = 'Nguyen Hoang Anh Huy'
my_str_replace = my_str_replace.replace('Nguyen', 'Tran')
print('my_str_replace: ', my_str_replace)

# str.format()
print('My name is {}'. format('huy'))

# str.join()
str1_join = 'Nguyen '
str2_join = 'Hoang '
str3_join = 'Huy'
print('str_join: ', ''.join([str1_join, str2_join, str3_join]))

mixed_str = 'nGUyen hOANG Anh HUY'
print('Str to lower: ', mixed_str.lower())
print('Str to upper: ', mixed_str.upper())
print('Str to title: ', mixed_str.title())

# str strip
ugly_formatted = ' \n \t Some story to tell '
print('Str ugly: ', ugly_formatted)
print('Str strip: ', ugly_formatted.strip())

# str.split()
sentence = 'three different words'
print('str.split: ', sentence.split(' '))

# Calling multiple methods in a row
ugly_mixed_case = '   ThIS LooKs BAd '
pretty = ugly_mixed_case.strip().lower().replace('bad', 'good')
print('multiple methods: ', pretty)