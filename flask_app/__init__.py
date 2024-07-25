# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "bouyskekks"

#replace the name once a proper database is created
DB = "dojos_and_ninjas"