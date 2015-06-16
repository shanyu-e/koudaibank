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

    def get(self, *args, **kwargs):
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


class UpdateVersion(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        ret_dic = {"error": 0, "lastVersion": "1.0", "down_url": "https://itunes.apple.com/cn/app\
                  /wei-xin/id414478124?mt=8#"}
        ret_json = json.dumps(ret_dic)
        self.write(ret_json)
        return


class Recommend(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        ret_dic = {"error": 0, "fundID": "", "return": [{"text": "", "img": "路径",}, \
                   {"text": "", "img": "路径"}], "lastPage": {"problem":"", "answer": \
                    "以#分隔", "rightanswer": ""}}
        ret_json = json.dumps(ret_dic)
        self.write(ret_json)
        return


class UserLogin(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        # print(self.get_argument("username", ""))
        username = self.get_argument("username", "")
        # pwd = self.get_argument("pwd", "")
        ret_dic = {"error": 0, "uid": "", "username": username, "userinfo": ""}
        ret_json = json.dumps(ret_dic)
        self.write(ret_json)
        return


class RecentRecommand(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        ret_dic = {"error": 0, "recommend": [{"img": "路径", "text": ""}, {"img": "路径", \
                    "text": ""}], "rank": [{"img": "路径", "text":""}, {"img": "路径", "text": ""}]}
        ret_json = json.dumps(ret_dic)
        self.write(ret_json)
        return


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/koudaibank/load", InitLoad),
        (r"/koudaibank/brochure", Brochure),
        (r"/koudaibank/updateversion", UpdateVersion),
        (r"/koudaibank/recommend", Recommend),
        (r"/koudaibank/userLogin", UserLogin),
        (r"/koudaibank/recent_recommand", RecentRecommand),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()