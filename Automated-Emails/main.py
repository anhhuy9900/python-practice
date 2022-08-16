from send_mail import SendMail
import time
import pandas
import datetime


if __name__ == "__main__":
    while True:
        if datetime.datetime.now().hour == 13 and datetime.datetime.now().minute == 28:
            print("Executing")
            df = pandas.read_excel("people.xlsx")
            mailService = SendMail()
            for index, row in df.iterrows():
                print("row: ", row)
                mailService.send_mail(email=row['email'], interest=row['interest'], name=row['name'])

        time.sleep(60)