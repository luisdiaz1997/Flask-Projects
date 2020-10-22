from flask import Flask
from google.cloud import firestore
from google.cloud import storage

import os

    
CLOUD_STORAGE_BUCKET = os.environ.get("CLOUD_STORAGE_BUCKET")
CLOUD_THUMBNAIL_BUCKET = os.environ.get("CLOUD_THUMBNAIL_BUCKET")
print(CLOUD_STORAGE_BUCKET)
if CLOUD_STORAGE_BUCKET is None:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Project-1f0d49812708.json"
    # os.environ["CLOUD_STORAGE_BUCKET"] = "papus"
CLOUD_STORAGE_BUCKET = "papus" #os.environ.get("CLOUD_STORAGE_BUCKET")
CLOUD_THUMBNAIL_BUCKET = "thumbnails-papus"
    
app = Flask(__name__)

db = firestore.Client()
storage_client = storage.Client()
bucket = storage_client.get_bucket(CLOUD_STORAGE_BUCKET)