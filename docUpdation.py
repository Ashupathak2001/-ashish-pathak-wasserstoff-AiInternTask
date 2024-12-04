import time
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "your_url"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['pdf_database']
collection = db['pdf_collection']

# Function to update files into database
def store_updated_data(filename, summary, keywords):
    start_time = time.time()
    update_data = {
        "summary": summary,
        "keywords": keywords,
        "processing_time": time.time() - start_time
    }
    collection.update_one({'filename': filename}, {"$set": update_data})
    print("Data updated successfully")
