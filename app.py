import logging
from flask import Flask
app = Flask(__name__)

from routes import *

logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)

# if __name__ == '__main__':
#     app.run(debug=True)