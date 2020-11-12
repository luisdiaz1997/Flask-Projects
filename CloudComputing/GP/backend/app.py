import base64
from flask import Flask, send_file, request, jsonify, make_response, send_file
from flask_cors import CORS
import translation
from audio import analyze_audio
import texttospeech
import os
from google.cloud import datastore

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__, static_folder='../frontend/dist', static_url_path='/')
CORS(app)

datastore_client = datastore.Client()

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/about')
def about():
    return app.send_static_file('index.html')


@app.route('/upload')
def upload():
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
    response = analyze_audio(request)
    return response

@app.route('/analyze_text', methods=["GET", "POST"])
def process_text():
    if request.method=="POST":
        print(request.form)
        translatedText = translation.translate_text("es", request.form['text'])#"to Spanish (es)"
        response_body = {
                "message": translatedText
            }
        response = jsonify(response_body)
        return response

@app.route('/text_to_audio',  methods=["GET", "POST"])
def text_to_audio():
    if request.method=="POST":
        #If request doesnt have id, then add it to db
        # If it does, send text to api  
        message = texttospeech.run(request.form['text'])  
        response_body = {
                "message": message
            }
        file_path = os.path.join(dir_path, 'output.mp3')
        return send_file(file_path)

@app.route('/get_quotes', methods=["GET", "POST"])
def get_quotes():
    if request.method=="GET":
        query = datastore_client.query(kind="proj3_files")
        quotes_list = query.fetch()
        response_body = []
        for quote in quotes_list:
            print('Quote Id : ' + str(quote.key.id) + '   Transcribed Text: ' + quote['Transcribed Text'])        
            response_body.append({
            "id": quote.key.id,
            "text": quote['Transcribed Text'],
            })
        response = jsonify(response_body)
        return response


if __name__=='__main__':
    app.run(port=5000, debug=True)