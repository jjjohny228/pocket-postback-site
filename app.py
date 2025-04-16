import logging
from flask import Flask
app = Flask(__name__)

from routes import *

logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)

# app.run(debug=True)