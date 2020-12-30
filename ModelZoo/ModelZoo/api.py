from . import app
from flask import request, jsonify
from PIL import Image, ImageOps
import base64
from io import BytesIO
from . import model

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/about')
def about():
    return app.send_static_file('index.html')

@app.route('/process_number', methods = ['POST', 'GET'])
def process_number():
    if request.method=="POST":
        image= request.form["image"].split(',')[1]
        img = Image.open(BytesIO(base64.b64decode(image)))

        predictions = model.predict(img)
        return jsonify(predictions=predictions)