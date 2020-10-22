from flask import render_template, request, redirect
from photoapp import app, db, storage_client, bucket, bucket_thumbnails, \
CLOUD_STORAGE_BUCKET, CLOUD_THUMBNAIL_BUCKET, text_api
import time
import re

@app.route("/")
def home():
    pictures_ref = db.collection(u'pictures')
    pictures = pictures_ref.limit(20).stream()
    all_pictures = []
    for picture in pictures:
        curr_dict = picture.to_dict()
        if not curr_dict.get("thumbnail", False):
            continue
        curr_dict['name'] = picture.id
        all_pictures.append(curr_dict)
    
    return render_template("home.html", thumbnails= CLOUD_THUMBNAIL_BUCKET, pictures=all_pictures)

def create_photo(request, name=False):
    if (request.files["myfile"].filename != ''):
        if not name:
            name = request.files["myfile"].filename
        photo = request.files['myfile']
      
        blob = bucket.blob(name)
        blob_thumbnails = bucket_thumbnails.blob(name)

        if blob.exists():
            db.collection(u'pictures').document(name).delete()
            time.sleep(1)
            blob.delete()
        
        if blob_thumbnails.exists():
            
            blob_thumbnails.delete()
            
        blob.upload_from_string(photo.read(), content_type=photo.content_type)

@app.route("/upload_photo", methods=["GET", "POST"])
def upload_photo():
    create_photo(request)
    return redirect("/")

@app.route("/view/<name>")
def read(name):
    document_ref = db.collection(u'pictures').document(name)
    document = document_ref.get()
    if document.exists:
        labels=None
        try:
            labels = document.get(u'labels')
            print(labels)
        except(KeyError):
            print("No Labels")
        
        return render_template("view.html", name=name, bucket= CLOUD_STORAGE_BUCKET, labels = labels)
    return "Not doesnt exist"


@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method=="POST":
        file_name = request.form["file"]
        blob = bucket.blob(file_name)
        blob_thumbnails = bucket_thumbnails.blob(file_name)
        blob.delete()
        blob_thumbnails.delete()
        db.collection(u'pictures').document(file_name).delete()
        return redirect("/")



@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method=="POST":
        name=request.form["name"]
        create_photo(request, name=name)
        time.sleep(1)
        labels = request.form["labels"]
        labels = re.split("\s*,\s*", labels)
        picture_ref = db.collection(u'pictures').document(name)
        picture_ref.set({
            u'labels': labels
        }, merge=True)
        return redirect("/view/"+name)