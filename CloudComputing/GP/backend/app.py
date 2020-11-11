import base64
from flask import Flask, send_file, request, jsonify, make_response
from flask_cors import CORS

from audio import Audio_API

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

if __name__=='__main__':
    app.run(port=5000, debug=True)