import json
import pprint

import re
import execjs
import requests


def Get( uri: str, host:str ,headers, params=None):
    final_uri = uri
    if isinstance(params, dict):
        final_uri = (f"{uri}?"
                     f"{'&'.join([f'{k}={v}' for k, v in params.items()])}")
    requests.get(url=f"{host}{final_uri}", headers=headers)


def Post( uri: str, host: str , headers, data: dict):

    json_str = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
    requests.post(url=f"{host}{uri}", data=json_str, headers=headers)

# unavailable currently
def GetXsForGet(api):
    with open('../demo/xhs_xs.js', 'r', encoding='utf-8') as f:
        jstext = f.read()

    ctx = execjs.compile(jstext)

    result = ctx.call("get_xs",api)
    return result


def GetXsForPost( cookie, api, data):
    with open('../demo/xhs_xs.js', 'r', encoding='utf-8') as f:
        jstext = f.read()
        #print(jstext)

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

