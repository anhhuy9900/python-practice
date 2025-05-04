"""Function Decorators."""


def calculator_age(fune):
    def cal(age):
        if 10 < age < 20:
            return age + 5
        if age > 20:
            return age + 10
        return fune(age)
    return cal


def get_profile():
    def get_name():
        return 'nguyen hoang anh huy'

    @calculator_age
    def get_age(age):
        return age

    return "User info: name: {}, age: {}".format(get_name(), get_age(40))


print(get_profile())
