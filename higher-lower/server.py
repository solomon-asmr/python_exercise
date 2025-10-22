from flask import Flask
import random
from functools import wraps
app = Flask(__name__)
correct_number = random.randint(0, 9)
def number_guess_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # call the original view correctly
        guessed_number = int(function(*args, **kwargs))
        if guessed_number < correct_number:
            return ('<h1 style="text-align:center; color:blue;">Too low, try again</h1><br>'
                    '<img style="display:block; margin:auto; width:50%;" '
                    'src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
        elif guessed_number > correct_number:
            return ('<h1 style="text-align:center; color:crimson;">Too high, try again</h1><br>'
                    '<img style="display:block; margin:auto; width:50%;" '
                    'src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
        else:
            return ('<h1 style="text-align:center; color:green;">You found me!</h1><br>'
                    '<img style="display:block; margin:auto; width:50%;" '
                    'src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')

    return wrapper

@app.route('/')
def guess_the_number():
    return ('<h1 style="text-align: center;">guess the number between 0 and 9</h1> <br>'
            '<img style="display: block;margin: auto;width: 50%;" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')



@app.route('/<int:n>')
@number_guess_decorator
def searching_for(n):
    return n
if __name__ == "__main__":
    app.run(debug=True)