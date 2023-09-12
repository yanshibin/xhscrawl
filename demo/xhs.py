import json
import pprint

import re
import execjs
from py_mini_racer import py_mini_racer

def GetXs( cookie, api, data):
    with open('xhs.js', 'r', encoding='utf-8') as f:
        jstext = f.read()

    ctx = execjs.compile(jstext)

    match = re.search(r'a1=([^;]+)', cookie)
    a1 = ""
    if match:
        a1 = match.group(1)
    else:
        print("关键参数a1获取失败，请检查你的cookie")
        return ""

    result = ctx.call("get_xs", api, data, a1)
    return result

# 向笔记发送评论
if __name__ == '__main__':
    cookie = 'put your cookie here'
    api = "/api/sns/web/v1/comment/post"  # comment api
    data = {"note_id": "put your note id here", "content": "put your comment here", "at_users": []}
    xs = GetXs(cookie, api, data)
    print(json.dumps(xs, indent=4))
