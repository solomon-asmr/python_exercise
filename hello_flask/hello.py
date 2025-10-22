from flask import Flask


app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>"+function()+"</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hell_world():
    return 'hello world'

@app.route('/bye')
def good_bye():
    return 'good bye'

@app.route('/<name>/<int:number>')
def greeting(name, number):
    return f"hello there {name}! you are {number} years old"
if __name__ == "__main__":
    app.run(debug=True)