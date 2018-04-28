from main import route, BaseHandler


@route(r'/')
class HelloWorld(BaseHandler):

    def get(self):

        """
        get value by key
        """

        self.db.Test.insert({'test': 'test'})
        self.logger.info(self.db.Test.find_one({'test': 'test'}))

        return self.write_json({
            'errcode': 0,
            'msg': 'success',
        })


@route(r'/index')
class Index(BaseHandler):

    def get(self):

        self.render('index.html')