import base64
from flask import Flask, send_file, request, jsonify, make_response, send_file
from flask_cors import CORS

from audio import Audio_API

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__, static_folder='../frontend/dist', static_url_path='/')
CORS(app)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/about')
def about():
    return app.send_static_file('index.html')

@app.route('/analyze_image', methods=["GET", "POST"])
def process_image():
    if request.method=="POST":
        print(request.form)
        print(request.files)
        image = request.files["image"]

        print(image.filename)
        print(image.content_type)
        response_body = {
                "message": "This a vague description of what is on "+image.filename
            }
        response = jsonify(response_body)
        return response

@app.route('/analyze_audio', methods=["GET", "POST"])
def process_audio():
    audio_obj= Audio_API()
    response = audio_obj.analyze_audio(request)
    return response  

@app.route('/analyze_text', methods=["GET", "POST"])#translate Sally
def process_text():
    if request.method=="POST":
        print(request.form)
        print(request.files)

        response_body = {
                "message": "Hola mi nombre es Luis"
            }
        response = jsonify(response_body)
        return response

@app.route('/text_to_audio',  methods=["GET", "POST"]) #Sally
def text_to_audio():
    if request.method=="POST":
        #If request doesnt have id, then add it to db
        # If it does, send text to api     
        response_body = {
                "message": "Hola mi nombre es Luis"
            }
        file_path = os.path.join(dir_path, 'test.mp3')
        return send_file(file_path)

@app.route('/get_quotes', methods=["GET", "POST"]) #Bhavani
def get_quotes():
    if request.method=="GET":

        response_body = [{
            "id": "2",
            "text": "This world is beautiful",
        },{
            "id": "3",
            "text": "This world is ugly",
        }]

        response = jsonify(response_body)
        return response


if __name__=='__main__':
    app.run(port=5000, debug=True)