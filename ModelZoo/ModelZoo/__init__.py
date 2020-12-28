from flask import Flask
from flask_cors import CORS, cross_origin


app = Flask(__name__, static_folder='../modelzoovue/dist', static_url_path='/')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
