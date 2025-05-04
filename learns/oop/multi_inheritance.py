import datetime


class Time:
    def get_time(self):
        return datetime.datetime.now().strftime('%X')


class Date:
    def get_date(self):
        return datetime.datetime.now().strftime('%x')


class DateTime(Date, Time):

    def get_datetime(self):
        return 'DateTime is: {} {}'.format(self.get_date(), self.get_time())


date_time = DateTime()
print(date_time.get_datetime())
