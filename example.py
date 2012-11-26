import sys
import os
import logging
import uuid
import urlparse
import urllib
import time

import tornado.options
import tornado.ioloop
import tornado.web
import tornado.httpclient as httpclient

from amazon_ses import EmailMessage
from tornado_ses import EmailHandler

class TestHandler(tornado.web.RequestHandler, EmailHandler):
    def get(self):
        # send email notifaction
        user_msg = EmailMessage()
        user_msg.subject = u"Test"
        user_msg.bodyHtml = "This is the test content."
        self.send("your@address.net", "user@address.net", user_msg)

settings = {
    "AmazonAccessKeyID": "00000000000000000000",
    "AmazonSecretAccessKey": "0000000000000000000000000000000000000000",
    "debug": True,
}

application = tornado.web.Application([
    (r"/", TestHandler),
], **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(int(sys.argv[1]))
    tornado.ioloop.IOLoop.instance().start()
