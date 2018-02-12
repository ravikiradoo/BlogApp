import pymongo
from pymongo import MongoClient
import bcrypt

class RegisterModel:

    def __init__(self):
        self.client=MongoClient()
        self.db=self.client.Blogapp
        self.Users=self.db.users
    def insert_user(self,data):
        hash = bcrypt.hashpw(data.password.encode('utf8'), bcrypt.gensalt())
        id=self.Users.insert({"Email":data.email,"Password":hash})
        print(id)


class LoginModel:


    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.Blogapp
        self.Users = self.db.users

    def login_user(self, data):


       user=self.Users.find_one({"Email":data.email})

       if user:
           if bcrypt.checkpw(data.password.encode('utf8'), user['Password'].encode('utf8')):
               print("User Mathced")
               return "User Matched"
           else:
               print("User not Mathced")
               return "User could not found"
