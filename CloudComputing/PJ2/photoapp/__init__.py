from flask import Flask
from google.cloud import firestore
from google.cloud import storage
import nltk
import os



nltk.download('wordnet')
    
CLOUD_STORAGE_BUCKET = os.environ.get("CLOUD_STORAGE_BUCKET")
CLOUD_THUMBNAIL_BUCKET = os.environ.get("CLOUD_THUMBNAIL_BUCKET")
CLOUD_STORAGE_BUCKET = "papus" #os.environ.get("CLOUD_STORAGE_BUCKET")
CLOUD_THUMBNAIL_BUCKET = "thumbnails-papus"

if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") is None:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Project-1f0d49812708.json"

    
app = Flask(__name__)

db = firestore.Client()
storage_client = storage.Client()
bucket = storage_client.get_bucket(CLOUD_STORAGE_BUCKET)
bucket_thumbnails = storage_client.get_bucket(CLOUD_THUMBNAIL_BUCKET)
categories = ["animals", "flowers", "people", "other"]
