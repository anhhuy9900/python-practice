from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField
from flatmates_bill import flat

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)

    def post(self):
        bill_form = BillForm(request.form)
        the_bill = flat.Bill(float(bill_form.amount.data), bill_form.period.data)
        flat_mate_1 = flat.Flatmate(bill_form.name1.data, float(bill_form.days_in_house1.data))
        flat_mate_2 = flat.Flatmate(bill_form.name2.data, float(bill_form.days_in_house2.data))
        return render_template('results.html',
                               results=True,
                               name1=flat_mate_1.name,
                               amount1=flat_mate_1.pays(the_bill, flat_mate_2),
                               name2=flat_mate_2.name,
                               amount2=flat_mate_2.pays(the_bill, flat_mate_1)
                               )


class BillForm(Form):
    amount = StringField("Bill Amount: ", default=100)
    period = StringField("Period: ", default="December 2021")

    name1 = StringField("Name: ", default="John")
    days_in_house1 = StringField("Days in the house: ", default=20)

    name2 = StringField("Name: ", default="Marry")
    days_in_house2 = StringField("Days in the house: ", default=12)

    button = SubmitField("Calculate")


class ResultsPage(MethodView):

    def post(self):
        bill_form = BillForm(request.form)
        the_bill = flat.Bill(float(bill_form.amount.data), bill_form.period.data)
        flat_mate_1 = flat.Flatmate(bill_form.name1.data, float(bill_form.days_in_house1.data))
        flat_mate_2 = flat.Flatmate(bill_form.name2.data, float(bill_form.days_in_house2.data))
        return render_template('results.html',
                               results=True,
                               name1=flat_mate_1.name,
                               amount1=flat_mate_1.pays(the_bill, flat_mate_2),
                               name2=flat_mate_2.name,
                               amount2=flat_mate_2.pays(the_bill, flat_mate_1)
                               )


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill-form',
                 view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results',
                 view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
