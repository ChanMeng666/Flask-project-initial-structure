from flask import Flask
from eoms.secret import SECRET_KEY
app = Flask(__name__)

app.secret_key = SECRET_KEY

# Routes
from eoms.route import form_ex