import json

from twisted.internet.task import react
from _utils import print_response

import treq


def main(reactor, *args):
    http_client = treq
    d = http_client.post('http://httpbin.org/post',
                  json.dumps({"msg": "Hello!"}),
                  headers={'Content-Type': ['application/json']})
    d.addCallback(print_response)
    return d

react(main, [])
