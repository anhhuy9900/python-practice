from fpdf import FPDF
import random
import string
import sqlite3


class User:
    """Represents a user that can buy a cinema Seat"""
    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        """Buys the ticket if the card is valid"""
        if seat.is_free():
            if card.validate(price=seat.get_price()):
                seat.occupy()
                ticket = Ticket(user=self, price=seat.get_price(), seat_number=seat.seat_id)
                ticket.to_pdf()
                return "Purchase successful!"
            else:
                return "There was a problem with your card!"
        else:
            return "Seat is taken!"


class Seat:
    """Represents a cinema seat that can be taken from a User"""
    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id
        self.connection = sqlite3.connect(self.database)

    def get_price(self):
        """Get the price of a certain seat"""

        cursor = sqlite3.connect(self.database).cursor()
        cursor.execute("""
                SELECT "price" FROM "Seat" WHERE "seat_id"=?
                """, [self.seat_id])
        result = cursor.fetchone()
        return result[0] if result else None

    def is_free(self):
        """Check in the database if a Seat is taken or not"""
        cursor = sqlite3.connect(self.database).cursor()
        cursor.execute("""
                        SELECT "price" FROM "Seat" WHERE "seat_id"=?
                        """, [self.seat_id])
        result = cursor.fetchone()
        if result:
            return True
        return False

    def occupy(self):
        """Change value of taken in the database from 0 to 1 if Seat is free"""
        if self.is_free():
            cursor = sqlite3.connect(self.database).cursor()
            cursor.execute("""
                            UPDATE "Seat" SET "taken"=? WHERE "seat_id"=?
                           """, [1, self.seat_id])
            self.connection.commit()
            self.connection.close()


class Card:
    """ Represents a bank card needed to finalize a Seat purchase"""
    database = "banking.db"

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder
        self.connection = sqlite3.connect(self.database)

    def validate(self, price):
        """Checks if Card is valid and has balance.
        Subtracts price from balance.
        """
        cursor = sqlite3.connect(self.database).cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE "number"=? and "cvc"=?
        """, [self.number, self.cvc])
        result = cursor.fetchall()

        if result:
            balance = result[0][0]
            if balance >= price:
                self.connection.execute("""
                UPDATE "Card" SET "balance" = ? WHERE "number"=? and "cvc"=?
                """, [balance - price, self.number, self.cvc])
                self.connection.commit()
                self.connection.close()
                return True


class Ticket:
    """Represents a cinema Ticket purchased by a User"""

    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        self.seat_number = seat_number

    def to_pdf(self):
        """Creates a PDF ticket"""
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=80, txt="Your Digital Ticket", border=1, ln=1, align="C")

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Name: ", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=self.user.name, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Ticket ID", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=self.id, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Price", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=str(self.price), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Seat Number", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=str(self.seat_number), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.output("sample_1.pdf", 'F')


if __name__ == "__main__":
    name = input("Your full name: ")
    seat_id = input("Preferred seat number: ")
    card_type = input("Your card type: ")
    card_number = input("Your card number: ")
    card_cvc = input("Your card cvc: ")
    card_holder = input("Card holder name: ")

    card = Card(type=card_type, number=card_number, cvc=card_cvc, holder=card_holder)
    seat = Seat(seat_id)
    user = User(name=name)
    print(user.buy(seat=seat, card=card))