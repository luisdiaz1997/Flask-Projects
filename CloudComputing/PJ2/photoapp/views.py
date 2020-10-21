from flask import render_template, request
from photoapp import app, db, storage_client, bucket, \
CLOUD_STORAGE_BUCKET, CLOUD_THUMBNAIL_BUCKET


@app.route("/")
def home():
    pictures_ref = db.collection(u'pictures')
    
    pictures = pictures_ref.limit(10).stream()
    all_pictures = []
    for picture in pictures:
        curr_dict = picture.to_dict()
        curr_dict['name'] = picture.id
        all_pictures.append(curr_dict) 
    
    print(all_pictures)
    return render_template("home.html", thumbnails= CLOUD_THUMBNAIL_BUCKET, pictures=all_pictures)

    

@app.route("/view/<image_file>")
def read(image_file):
    document_ref = db.collection(u'pictures').document(image_file)
    document = document_ref.get()
    if document.exists:
        return "Exists"
    return "Not doesnt exist"