from flask import Flask, request, render_template
from random import choice, sample

app = Flask(__name__)
# __name__ mean current file

compliments = ['coolio', 'smashing', 'neato', 'fantabulous']
planets = ['sun', 'moon', 'venus', 'mars', 'jupiter', 'uranus', 'neptune', 'pluto', 'mercury', 'saturn']
signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'sagitarius', 'aquarius', 'scorpio', 'pisces', 'libra', 'capricorn']


@app.route('/compliment')
def get_compliment():
    # give user compliment
    name = request.args.get('name')
    show_compliments = request.args.get('show_compliments')
    compliments_to_show = choice(compliments, 3)

    return render_template(
        'compliments.html',
        name=name,
        show_compliments=show_compliments,
        compliments=compliments_to_show)

    '''if show_compliments:
        return f'Hello there, {name}! You are so {compliment}!'
    else:
        return f'Hello there, {name}! Have a nice day!''''


def get_horoscope():
    # impliment this function in the activy
    # return a rand fortune or horoscope
    horoscope = choice(planets) + " in " + choice(signs)
    return f'{horoscope} brings good fortune to your day!'


@app.route('/')
def index():
    section = 'BEW 1.1 Section A'
    greeting = 'Good Morning class!'
    # Show the homepage and ask the user's name."""
    return render_template('index.html', section=section, greeting=greeting)
    <form action='/compliment'>
        What is your name?
        <input type="text" name="name"></input>
        <button type="submit">Submit</button>
    </form>'''


if __name__ == "__main__":
    app.run(debug=True)
