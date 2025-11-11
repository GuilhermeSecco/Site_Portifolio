from flask import Flask, request, redirect, url_for, session
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.secret_key = 'Shiro'
from views import *

if __name__ == '__main__':
    app.run(debug=True)