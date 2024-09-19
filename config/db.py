from pymongo import MongoClient

MONGO_URI = "mongodb+srv://aloknathtiwari2000:1DnSObvpoHQlMTqH@cluster1.8fkbw.mongodb.net/user?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
client = client.get_database("user")
