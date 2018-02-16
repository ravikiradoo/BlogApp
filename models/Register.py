import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
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
        id=self.Users.insert({"UserName":data.username,"Email":data.email,"Password":hash,"About":"","Hobbies":"","Birthday":"","ProfilePic":""})
        print(id)

    def update_user(self,data):
        self.Users.update_one({"Email":data.email},{'$set':{"UserName":data.username,"About":data.about,"Hobbies":data.hobbies,"Birthday":data.bday}})

    def upload_pic(self,data):
        self.Users.update_one({"Email":data["email"]},{'$set':{"ProfilePic":data["imagepath"]}})

    def getUser(self):
        all_user=self.Users.find({})
        user_list=[]

        for u in all_user:
            user = {}
            user["id"]=u["_id"]
            user["username"]=u["UserName"]
            user["profile"]=u["ProfilePic"]
            user_list.append(user)

        return user_list

    def getProfile(self,data):
        u=self.Users.find_one({"_id":ObjectId(data)})
        user={}



        user["username"]=u["UserName"]
        user["profile"]=u["ProfilePic"]
        user["about"]=u["About"]
        user["hobbies"]=u["Hobbies"]
        user["bday"]=u["Birthday"]


        return user


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
        self.Comments=self.db.comments

    def AddPost(self,data):
        time=(datetime.datetime.now())
        self.Posts.insert({"Email":data.email,"Post":data.post,"Date":time})

    def insertComment(self,data):
        time=datetime.datetime.now()
        data.Time=time
        self.Comments.insert(data)
        return "pass"

    def DeletePost(self,data):
        print(data.id)
        result=self.Posts.delete_one({"_id":ObjectId(data.id)})
        print(result)
        return result





    def Getpost(self,data):
        all_posts=self.Posts.find({"Email":data})
        post_list=[]
        for post in all_posts:
            post["Date"]= humanize.naturaltime(datetime.datetime.now()-post["Date"])
            comments=[]

            all_comments=self.Comments.find({"postid":str(post["_id"])})

            for c in all_comments:
                print(c)
                c["Time"]=humanize.naturaltime(datetime.datetime.now()-c["Time"])
                comments.append(c)


            post["comments"]=comments
            post_list.append(post)
        return  post_list




