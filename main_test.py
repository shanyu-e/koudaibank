#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import tornado.web
import tornado.httpserver
import tornado
from tornado.options import options, define

__author__ = 'dengjing'


define("port", default=9090, help="run on the given port", type=int)


class InitLoad(tornado.web.RequestHandler):

    def get(self):
        ret_dic = {"error": 0, "img_url": "https://avatars1.githubusercontent.com/u/3265603?v=3&s=460",
                   "text_context": "欢迎", "title": "标题"}
        ret_json = json.dumps(ret_dic)
        self.write(ret_json)
        return


class Brochure(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        ret_dic = {"error": 0, "return": [{"img": "http://ww1.sinaimg.cn/bmiddle/61847454jw1esz2g\
                   y47rbj20j60ctaea.jpg", "text": "图片1"}, {"img": "http://ww1.sinaimg.cn/bmiddle/\
                   61847454jw1esz2gy47rbj20j60ctaea.jpg", "text": "图片2"},]}
        ret_json = json.dumps(ret_dic)
        self.write(ret_json)
        return


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/koudaibank/load", InitLoad),
        (r"/koudaibank/brochure", Brochure),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()