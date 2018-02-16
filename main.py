import web
import humanize
import datetime
from models import Register
import os
web.config.debug=False

urls=[
    '/','index',
    '/register','register',
    '/PostData','Save',
    '/Login','Login',
    '/login','PostLogin',
    '/Logout','Logout',
    '/post', 'Post',
    '/HomeFeed','HomeFeed',
    '/Setting','Setting',
    '/update','Update',
    '/comment','Comment',
    '/deletePost','DeletePost',
    '/Upload','UploadImage',
    '/Profile','Profile'

]

app = web.application(urls,globals())
session=web.session.Session(app,web.session.DiskStore("session"),initializer={"user":None})
session_data=session._initializer

render = web.template.render("views/Templates",base="MainLayout",globals={'session':session_data,'Current_user':session_data['user']})


class index:
    def GET(self):
        return render.Home()
class register:
    def GET(self):
        return render.Register()

class Save:
    def POST(self):
        data=web.input()
        reg_model=Register.RegisterModel()
        reg_model.insert_user(data)
        return "pass"
class Login:
    def GET(self):
        return render.Login()

class PostLogin:
    def POST(self):
        data=web.input()
        log_model=Register.LoginModel()
        message=log_model.login_user(data)
        if message:
            session_data['user']=message
            return message
        else:
            return message
class Logout:
    def GET(self):
        session['user']=None
        session_data['user']=None
        session.kill()
        return "pass"

class Post:
    def POST(self):
        data=web.input()
        data.email=session_data['user']['Email']
        p_model=Register.PostModel()
        p_model.AddPost(data)
        return "pass"

class HomeFeed:
    def GET(self):
        p_model=Register.PostModel()
        print(session_data['user'])
        print("hi")
        if session_data['user']!=None:
            email=session_data['user']['Email']
            data=[]
            p_model=Register.PostModel()
            data=p_model.Getpost(email)


            return render.HomeFeed(data)
        else:
            data=[]
            return render.HomeFeed(data)

class Setting:
    def GET(self):
        data={}
        return render.Setting(data)

class Update:
    def POST(self):
        data=web.input()
        data.email=session_data['user']['Email']
        u_model=Register.RegisterModel()
        u_model.update_user(data)
        return "pass"

class Comment:
    def POST(self):
        data=web.input();
        data.email=session_data['user']['Email']
        data.user=session_data['user']['UserName']
        c_model=Register.PostModel()
        result=c_model.insertComment(data)

        if result:
            return "pass"
        else:
            return "fail"


class DeletePost:
    def POST(self):
        data=web.input()
        model=Register.PostModel()
        result=model.DeletePost(data)
        if result:
            return "pass"
        else:
            return "fail"

class UploadImage:
    def POST(self):
        file=web.input(pic={})
        cwd=os.getcwd()
        dir="static\uploads\\"+(session_data["user"]["Email"]).split("@")[0]
        file_dir=os.path.join(cwd,dir)
        if os.path.exists(file_dir):
            for f in os.listdir(file_dir):
                os.remove(file_dir+"\\"+f)

        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        if "pic" in file:
             filepath=file["pic"].filename

        f=open(file_dir+"\\"+filepath,"wb")
        f.write(file['pic'].file.read())
        f.close()
        model=Register.RegisterModel()
        data={}
        data["email"]=session_data["user"]["Email"]
        data["imagepath"]=dir+"\\"+filepath
        model.upload_pic(data)
        data={}
        data["message"]="Profile Updated Successfully"

        return render.Setting(data)










if __name__=="__main__":
    app.run()