import pymongo
from pymongo import MongoClient

class RegisterModel:

    def __init__(self):
        self.client=MongoClient()
        self.db=self.client.Blogapp
        self.Users=self.db.users
    def insert_user(self,data):
        id=self.Users.insert({"Email":data.email,"Password":data.password})
        print(id)