import pymongo
from pymongo import MongoClient

class RegisterModel:
    def insert_user(self,data):
        print("Data",data)