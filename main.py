import web
from models import Register
web.config.debug=False

urls=[
    '/','index',
    '/register','register',
    '/PostData','Post',
    '/Login','Login',
    '/login','PostLogin',
    '/Logout','Logout'


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

class Post:
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

if __name__=="__main__":
    app.run()