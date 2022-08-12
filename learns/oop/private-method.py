class User():

    def __init__(self):
        # private property
        self.__fullname = 'huy'
        self.__email = 'huy@mail.com'

    def get_info(self):
        return f'{self.__fullname} {self.__email} {self.__get_address()}'

    # private method
    def __get_address(self):
        return 'address 12344'


user = User()
print('User info: ', user.get_info())

# AttributeError: 'User' object has no attribute '__fullname'
# print('User fullname: ', user.__fullname)

# Error: AttributeError: 'User' object has no attribute '__get_address'
# print('User address: ', user.__get_address())
# Allow
# print('User address: ', user._User__get_address())