import web

urls=[
    '/(.*)','index'
]
app = web.application(urls,globals())
class index:
    def GET(self,name):
        return  "<h1>Hello"+name+"How are you?</h1>"

if __name__=="__main__":
    app.run()