import yagmail
import datetime
from news import NewsFeed


class SendMail:
    def __init__(self):
        self.mail_service = yagmail.SMTP(user="nhahuy19902@gmail.com", password="cetztibakqpcimyi")

    def send_mail(self, email, interest, name):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        news_feed = NewsFeed("Apple", yesterday, today, "en")

        self.mail_service.send(
                    to=email,
                    subject=f"Your {interest} news for today!",
                    contents=f"Hi {name}\n See what's on about {interest} today. \n{news_feed.get()}\n")
        print("Send mail successfully")


if __name__ == "__main__":
    mail = SendMail()
    mail.send_mail("anhhuy9900@yopmail.com", "huy", "huy")