import web

urls=[
    '/(.*)','index'
]
render = web.template.render("views/Templates",base="MainLayout")
app = web.application(urls,globals())
class index:
    def GET(self,name):
        return render.Home(name)

if __name__=="__main__":
    app.run()