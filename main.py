import web
from models import Register


urls=[
    '/','index',
    '/register','register',
    '/PostData','Post',
]
render = web.template.render("views/Templates",base="MainLayout")
app = web.application(urls,globals())
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

if __name__=="__main__":
    app.run()