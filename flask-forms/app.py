from datetime import date
from os import getenv
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from wtforms.fields.core import SelectField


app = Flask(__name__)

app.config['SECRET_KEY'] = "asdakdgasjhfgsajfhgakjfhgdsjfhkfdjakfdshgkjadflshbvaerigv4289"

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    date_of_birth = DateField("Date of Birth", format="%Y-%m-%d")
    favorite_number = IntegerField("Your favorite number:")
    favorite_food = SelectField("Favorite Food", choices=[("Pizza", "Pizza"), ("Hamburger", "Hamburger"), ("Ice Cream", "Ice Cream")])
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        date_of_birth = form.date_of_birth.data
        favorite_number = form.favorite_number.data
        favorite_food = form.favorite_food.data


        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply all required fields."
        else:
            message = f'Thank you, {first_name} {last_name}, Your date of birth is {date_of_birth}, Your favorite number is {favorite_number} and Your favorite food is {favorite_food}'

    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')