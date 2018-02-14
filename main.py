import web
import humanize
import datetime
from models import Register
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
if __name__=="__main__":
    app.run()