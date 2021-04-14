from flask import Flask, request, render_template
import math
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    
    return render_template('froyo_results.html',
        users_froyo_flavor = request.args.get('flavor'),
        users_froyo_toppings = request.args.get('toppings')
    )


@app.route('/favorites')
def favorites():
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>
        What is your favorite animal? <br/>
        <input type="text" name="animal"><br/>
        What is your favorite city? <br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    users_fav_color = request.args.get('color')
    users_fav_animal = request.args.get('animal')
    users_fav_city = request.args.get('city')
    return f"Wow, I didn't know {users_fav_color} {users_fav_animal} lived in {users_fav_city}!"

@app.route('/secret_message')
def secret_message():
    return """
    <form action="/message_results" method="POST">
        What is your message? <br/>
        <input type="text" name="message"> <br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    users_message = request.form.get('message')
    return sort_letters(users_message)
    

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():

    context = {
        'operand1' : int(request.args.get('operand1')),
        'operand2' : int(request.args.get('operand2')),
        'operation' : request.args.get('operation')
    }

    return render_template('calculator_results.html', **context)


HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = ''

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = ''

    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randint(1,99)

    context = {
        'horoscope_sign': request.args.get('horoscope_sign'),
        'personality': request.args.get('users_personality'), 
        'lucky_number': request.args.get('lucky_number')
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
