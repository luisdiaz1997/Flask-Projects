from flask import render_template, request, redirect
from photoapp import app, db, storage_client, bucket, bucket_thumbnails, \
CLOUD_STORAGE_BUCKET, CLOUD_THUMBNAIL_BUCKET, words, categories
import time
import re


@app.route("/")
def home():
    pictures_ref = db.collection(u'pictures')
    pictures_dict = dict()
    for category in categories:
        pictures = pictures_ref.where(u'category', u'==', category).limit(20).stream()
        all_pictures = pictures_dict.get(category, [])
        for picture in pictures:
            curr_dict = picture.to_dict()
            if not curr_dict.get("thumbnail", False):
                curr_dict["thumbnail_path"] = "https://storage.googleapis.com/"+ CLOUD_STORAGE_BUCKET + "/" + curr_dict["name"]
            else:
                curr_dict["thumbnail_path"] = "https://storage.googleapis.com/"+ CLOUD_THUMBNAIL_BUCKET + "/" + curr_dict["name"]
            
            # if not curr_dict.get("photographer", False):
            #     document = pictures_ref.document(curr_dict["name"])
            #     document.set({
            #         u'photographer': "Luis Chumpitaz",
            #         u'taken':"2020-10-25",
            #         u'location':"San Francisco"
            #     }, merge=True)
                
            all_pictures.append(curr_dict)
        
        pictures_dict[category] = all_pictures

    return render_template("home.html", pictures_dict=pictures_dict, categories=categories)


def create_photo(request, name=False):
    if (request.files["myfile"].filename != ''):
        if not name:
            name = request.files["myfile"].filename
        photo = request.files['myfile']
      
        blob = bucket.blob(name)
        blob_thumbnails = bucket_thumbnails.blob(name)

        if blob.exists():
            db.collection(u'pictures').document(name).delete()
            blob.delete()
        
        if blob_thumbnails.exists():

            blob_thumbnails.delete()
            
        blob.upload_from_string(photo.read(), content_type=photo.content_type)

@app.route("/upload_photo", methods=["GET", "POST"])
def upload_photo():
    create_photo(request)
    name = request.files["myfile"].filename
    if name != '':
        document_ref = db.collection(u'pictures').document(name)
        while (True):
            try:
                document = document_ref.get()
                labels = document.get(u'labels')
                labels_string = ' '.join(labels)
                break
            except:
                continue
        
        category = words.set_category(labels_string)
        document_ref.set({
            u'category': category,
            u'photographer': request.form["photographer"],
            u'taken':request.form["date"],
            u'location':request.form["location"]
        }, merge=True)

    return redirect("/")

@app.route("/view/<name>")
def read(name):
    document_ref = db.collection(u'pictures').document(name)
    document = document_ref.get()
    if document.exists:
        picture = document.to_dict()
        
        return render_template("view.html", name=name, bucket= CLOUD_STORAGE_BUCKET, picture = picture)
    return "Not doesnt exist"


@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method=="POST":
        file_name = request.form["file"]
        blob = bucket.blob(file_name)
        if blob.exists():
            blob.delete()

        blob_thumbnails = bucket_thumbnails.blob(file_name)

        if blob_thumbnails.exists():
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

        category = request.form["category"]
        if category == "auto":
            category = words.set_category(' '.join(labels))

        picture_ref = db.collection(u'pictures').document(name)
        picture_ref.set({
            u'labels': labels,
            u'category': category
        }, merge=True)

        return redirect("/view/"+name)