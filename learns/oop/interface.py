import abc


class UserInterface(abc.ABC):
    @abc.abstractmethod
    def get_info(self):
        pass


class User(UserInterface):

    def get_info(self):
        print('User info......')


if __name__ == '__main__':
    user = User()
    print('user: ', user)
    user.get_info()
