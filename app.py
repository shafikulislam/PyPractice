# cd /d "D:/Anik/P/PYTHON/SampleProject/"
# py -m http.server 8000

import datetime
import json

from flask import Flask

app = Flask("index")

@app.route("/")
def index():
    return "okay !"


class Person:
    def __init__(self):
        name = ""
        birth_year = 0
        age = 0
        age_group = ""


robo = Person()
robo.name = "Anik"
robo.birth_year = 1993


def get_current_time():
    return datetime.date.today()


def calculate_age(birth_year):
    today = get_current_time()
    year = today.year
    return (year - int(birth_year))


def get_age_group_by_age(age):
    junior = age < 20
    mid = age > 20 & age < 30
    senior = age > 30

    age_group = "Senior"

    if junior:
        age_group = "Junior"
    elif mid:
        age_group = "Middle Aged"

    return age_group


def get_age_group_by_birth_year(birth_year):
    return get_age_group_by_age(calculate_age(birth_year))


def verify_robo_age(user_answer):
    given_age = int(user_answer)
    if given_age == robo.age:
        return True;
    else:
        return False;


robo.age = calculate_age(1993)

user = Person()
user.name = input("Hello ! What's Your Name ?\n")

msg1 = "Hello , {0}! Nice to meet you. I'm {1}\n"
print(msg1.format(user.name, robo.name))

user.birth_year = input("Your Birth Year ?\n")
user.age = calculate_age(user.birth_year)
user.age_group = get_age_group_by_age(user.age)

msg2 = "So, You're {0} right ? I was born in {1}.\n"
print(msg2.format(user.age, robo.birth_year))

user_answer_on_robo_age = input("Tell me, How old am I ?\n")

if verify_robo_age(user_answer_on_robo_age):
    print("Wow ! You're good at Math ! We, can play a Math Game then.\n")
else:
    print("Na a ! That's a wrong guess.\n")
