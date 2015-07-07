#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import random
import urllib2
import django
import tornado.web
import tornado.httpserver
import tornado
import sys
from tornado.options import options, define

__author__ = 'dengjing'

define("port", default=9090, help="run on the given port", type=int)
reload(sys)
sys.setdefaultencoding('utf-8')

# from backend.backend import settings
# import os
# from django.core.management import
# setup_environ(settings)
# sys.path.append('/Users/dengjing/mywb/koudaibank/backend/bankend/')
# os.environ['DJANGO_SETTING_MODULE'] = 'backend.settings'
# from p1.models import TmpAuth
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.backend.settings'
from backend.p1.models import TmpAuth

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
                   61847454jw1esz2gy47rbj20j60ctaea.jpg", "text": "图片2"}, ]}
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
        ret_dic = {"error": 0, "fundID": "", "return": [{"text": "", "img": "路径", }, {"text": "", "img": "路径"}],\
                   "lastPage": {"problem": "", "answer": "以#分隔", "rightanswer": ""}}
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
        ret_dic = {"error": 0, "recommend": [{"img": "路径", "text": ""}, {"img": "路径", "text": ""}], \
                   "rank": [{"img": "路径", "text": ""}, {"img": "路径", "text": ""}]}
        ret_json = json.dumps(ret_dic)
        self.write(ret_json)
        return


class AppendRank(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        page = self.get_argument("page", "")
        # print(args)
        # print(kwargs)
        ret_dic = {"error": 0, "rank": [{"img": "路径", "text": ""}, {"img": "路径", "text": ""}], "page": page}
        ret_json = json.dumps(ret_dic)
        self.write(ret_json)
        return


class ScopeRecommand(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        x = self.get_argument("x", "")
        y = self.get_argument("y", "")
        page = self.get_argument("page", "")
        ret_dic = {"error": 0, "return": [{"img": "路径", "fundID": "", "title": "", \
                  "type": ""}, {"img": "路径", "text": "", "title": "", "type": ""}]}
        ret_json = json.dumps(ret_dic)
        self.write(ret_json)
        return


class ScopeRecommandNet(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        x = self.get_argument("x", "")
        y = self.get_argument("y", "")
        ret_dic = {"error": 0, "return": [{"img": "路径", "fundID": "", "title": "", \
                  "distance": ""}, {"img": "路径", "fundID": "", "title": "", "distance": ""}]}
        ret_json = json.dumps(ret_dic)
        self.write(ret_json)
        return


class ScopeRecommandDes(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        _type = self.get_argument("type", 0)
        ret_dic = {"error": 0, "return": [{"img": "路径", "text": "", "title": "", \
                                           "fundID": ""}, {"img": "路径", "text": "", "title": "", "fundID": ""}]}
        ret_json = json.dumps(ret_dic)
        self.write(ret_json)
        return


class BindPhone(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        user_name = self.get_argument("username", "dengjing")
        phone_number = self.get_argument("phone", "")
        # api_account = "jiekou-clcs-02"
        api_account = "qijing123"
        # api_pswd = "Tch112345"
        api_pswd = "Qijing888"
        # api_msg = u"注册验证码是：1111"
        try:
            auth = TmpAuth.objects.get(username=user_name)
        except:
            django.db.close_connection()
            # sys.exit()
            # raise SystemExit
            auth = TmpAuth.objects.get(username=user_name)
        # print auth.username
        auth.tmpcode = random.randint(1000, 9999)
        # print auth.tmpcode
        auth.save()
        api_msg = u"注册验证码是：%d" % auth.tmpcode
        api_needstatus = "true"
        api_query = "http://222.73.117.158/msg/HttpBatchSendSM"
        url = api_query + "?account=" + api_account + "&pswd=" + api_pswd + "&mobile=" + phone_number \
              + "&msg=" + api_msg + "&needstatus" + api_needstatus
        req = urllib2.urlopen(url).read()
        error_code = str(req).split(',')[1]
        ret_dic = {"error": error_code, "user_name": user_name}
        ret_json = json.dumps(ret_dic)
        self.write(ret_json)
        return


class CheckPhone(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        user_name = self.get_argument("username", "dengjing")
        verify_code = self.get_argument("verify", "")
        ret_dic = {"error": -1, "user_name": user_name}
        auth = TmpAuth.objects.get(username=user_name)
        if verify_code == str(auth.tmpcode):
            ret_dic["error"] = 0
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
        (r"/koudaibank/append_rank", AppendRank),
        (r"/koudaibank/scope_recommand", ScopeRecommand),
        (r"/koudaibank/scope_recommand_net", ScopeRecommandNet),
        (r"/koudaibank/scope_recommand_des", ScopeRecommandDes),
        (r"/koudaibank/bind_phone", BindPhone),
        (r"/koudaibank/check_phone", CheckPhone),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()