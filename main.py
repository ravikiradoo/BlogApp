import web

urls=[
    '/(.*)','index'
]
render = web.template.render("resources/")
app = web.application(urls,globals())
class index:
    def GET(self,name):
        return render.main(name)

if __name__=="__main__":
    app.run()