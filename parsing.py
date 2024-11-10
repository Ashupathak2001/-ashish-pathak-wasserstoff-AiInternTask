import os
import fitz
import time

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://ashupathak1610:HhpeLyBtJZLvs5Js@cluster1.kf54v.mongodb.net/?retryWrites=true&w=majority&ssl=true&appName=Cluster1"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# MongoDB Setup
db = client['pdf_database']
collection = db['pdf_collection']

# Function to parse PDF files
def load_pdfs(folder_path):
    pdf_texts = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            doc = fitz.open(os.path.join(folder_path, filename))
            text = ""
            for page in doc:
                text += page.get_text()
            pdf_texts[filename] = text
            doc.close()
    return pdf_texts

def store_initial_data(filename, size, ingestion_time):
    metadata ={
        'filename': filename,
        'size': size,
        'ingestion_time': ingestion_time
    }
    collection.insert_one(metadata)
    print("Data stored successfully")

def parse_and_store(folder_path):
    pdf_texts = load_pdfs(folder_path)
    for filename, text in pdf_texts.items():
        size = len(text)
        ingestion_time = time.time()
        store_initial_data(filename, size, ingestion_time)
    return pdf_texts