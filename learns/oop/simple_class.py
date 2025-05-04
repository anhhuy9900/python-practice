class User():
    name = None
    age = 0
    email = None

    def __init__(self, name_value=None, age_value=None, email_value=None):
        self.name = name_value
        self.age = age_value
        self.email = email_value

    def set_name(self, value):
        self.name = value

    def set_age(self, value):
        self.age = value

    def set_email(self, value):
        self.email = value

    def show_info(self):
        return 'name={}, age={}, email={}'.format(self.name, self.age, self.email)


user = User('Nguyen Hoang Anh huy', 32, 'huy@email.com')
print('User info: ', user.show_info())
user.set_name('huy')
user.set_age(30)
user.set_email('test@mail.com')
print('New user info: ', user.show_info())
