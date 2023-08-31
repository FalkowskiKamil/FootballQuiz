from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

CLIENT = False
CONNECTION = False

def checking_connection():
    global CONNECTION, CLIENT
    if CONNECTION == True:
        print("Connected")
        return CLIENT
    else:
        print("Not connected")
        uri = "mongodb+srv://testuser:testuser@quizapp.hg72xda.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi("1"))
        # Send a ping to confirm a successful connection
        try:
            client.admin.command("ping")
            print("Pinged your deployment. You successfully connected to MongoDB!")
            CLIENT = client
            CONNECTION = True
            return CLIENT
        except Exception as e:
            print(e)
