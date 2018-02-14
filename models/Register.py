import pymongo
from pymongo import MongoClient
import bcrypt
import datetime
import humanize

class RegisterModel:

    def __init__(self):
        self.client=MongoClient()
        self.db=self.client.Blogapp
        self.Users=self.db.users
    def insert_user(self,data):
        hash = bcrypt.hashpw(data.password.encode('utf8'), bcrypt.gensalt())
        id=self.Users.insert({"UserName":data.username,"Email":data.email,"Password":hash,"About":"","Hobbies":"","Birthday":""})
        print(id)

    def update_user(self,data):
        self.Users.update_one({"Email":data.email},{'$set':{"UserName":data.username,"About":data.about,"Hobbies":data.hobbies,"Birthday":data.bday}})


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
               return user
           else:
               print("User not Mathced")
               return "false"
       else:
           return False

class PostModel:
    def __init__(self):
        self.client=MongoClient()
        self.db=self.client.Blogapp
        self.Posts=self.db.posts

    def AddPost(self,data):
        time=(datetime.datetime.now())
        self.Posts.insert({"Email":data.email,"Post":data.post,"Date":time})


    def Getpost(self,data):
        all_posts=self.Posts.find({"Email":data})
        post_list=[]
        for post in all_posts:
            post["Date"]= humanize.naturaltime(datetime.datetime.now()-post["Date"])
            post_list.append(post)
        return  post_list




