from pymongo import MongoClient

MONGO_URI = "mongodb+srv://jaiganeshh574_db_user:jai1234@cluster0.drmyzog.mongodb.net/mydatabase?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["mydatabase"]
collection = db["users"]

print("✅ Connected to MongoDB Atlas")
#hi sndjgnsdnvjdfnjnvodvnoe nvernvon