import random
import requests
from flask import Flask, render_template
import datetime
app=Flask(__name__)

@app.route('/')
def Home():
    today1 = datetime.datetime.now()
    curr = today1.year
    rand =  random.randint(1,10)
    return render_template("index.html", current_year=curr, num= rand)
@app.route('/guess/<name1>')
def guess_sex(name1):
    age_url = f"https://api.agify.io/?name={name1}"
    gender_url = f"https://api.genderize.io/?name={name1}"
    agify_response=requests.get(age_url)
    age_data = agify_response.json()
    user_name=age_data["name"]
    user_age=age_data["age"]

    gendr_response = requests.get(gender_url)
    gender_data = gendr_response.json()
    user_gender = gender_data["gender"]

    return render_template("guess.html", name= user_name, gendr=user_gender, age=user_age )
if __name__=="__main__":
    app.run(debug=True)
