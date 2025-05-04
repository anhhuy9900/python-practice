from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template("index.html")


class CaloriesPage(MethodView):
    def get(self):
        calories_form = CaloriesForm()
        return render_template("calories_form_page.html", caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)
        temperature = Temperature(country=calories_form.country.data, city=calories_form.city.data).get()
        calorie = Calorie(
            weight=float(calories_form.weight.data),
            height=float(calories_form.height.data),
            age=int(calories_form.age.data),
            temperature=temperature
        )
        calorie_number = calorie.calculate()

        return render_template("calories_form_page.html",
                               result=True,
                               caloriesform=calories_form,
                               calories=calorie_number)


class CaloriesForm(Form):
    weight = StringField("Weight: ", default=70)
    height = StringField("Height: ", default=175)
    age = StringField("Age: ", default=32)
    country = StringField("Country: ", default='USA')
    city = StringField("City: ", default="San Francisco")
    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form',
                 view_func=CaloriesPage.as_view('calories_form_page'))

app.run(debug=True)