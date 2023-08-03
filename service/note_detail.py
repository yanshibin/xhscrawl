import json
import asyncio
import curlify
import httpx
import requests

from xhs import GetXs

if __name__ == '__main__':
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "cookie": '',
        "origin": "https://www.xiaohongshu.com",
        "pragma": "no-cache",
        "referer": "https://www.xiaohongshu.com/",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "x-b3-traceid": "a31fffc0ee4f5d8f",
        "x-s-common": "",
    }
    cookie = 'gid.sig=ooYpcOb3cch47JjSWAwFwlhzphfKxAPrMH4b3iOsWuo; gid.sign.sig=Ekn1RiJSw_am2RslNpYMMNojc7beWBp7MzXEvYIqIE4; smidV2=20220902154419cfdc03052f6ca93073821f716ec5153c006de92412963ee50; gid.ss=gSMQ9UOnDuZwH2oRGJG6BW6e4grs67TaYpnrW+8Wmd2l346RCyr+KJPPGa674999; a1=184d1885b79kueq8zufxxah0brzchxbn06l7mjxbt00000242961; webId=a1b67cc8bf1b7e409f32e7cc5175f36a; gid=yY4fyYY2dS8dyY4fyYY2DKVCWjT7dAYu7iCC1D90x8DFuW88SxCDI6888J4JjKy8YKSydd2y; gid.sign=3I/6BUxjRQtksJf1PKLWTqAU0yA=; timestamp2=167325189778920b7a70898e961e5c41797c5855e121b9616a71daa60689e8f; timestamp2.sig=xs56JeTSkpYMjP9wAuZiWJ9AvOlaACxb3Fxuec0aHiw; xhsTrackerId=4fb80133-9401-4b1b-b5bd-5888c4d842c9; xhsTrackerId.sig=wRvoxQcH01_D6sGBV8gnJr0UKPA6gciNdLAHzT6xZnc; web_session=040069b525b1e7f73f25051190364ba70d3447; sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%221892a922d5c1844-018978860d2fd2-1b525634-1296000-1892a922d5d1e84%22%7D; galaxy_creator_session_id=jdBnU0ReSoonuI50cY9gUJazaFjLBYERyS2o; galaxy.creator.beaker.session.id=1690896681180075278854; webBuild=2.18.4; xsecappid=xhs-pc-web; websectiga=59d3ef1e60c4aa37a7df3c23467bd46d7f1da0b1918cf335ee7f2e9e52ac04cf; sec_poison_id=40d94a01-02e6-4c44-8060-f8b3cbbd453a'

    headers['cookie'] = cookie
    api = '/api/sns/web/v1/feed'
    data = {"source_note_id": "64c87081000000000103f616"}
    xs_xt = GetXs(cookie,api,data)
    headers['X-s'] = xs_xt['X-s']
    headers['X-t'] = str(xs_xt['X-t'])
    feed = 'https://edith.xiaohongshu.com/api/sns/web/v1/feed'
    response = requests.post(url=feed, data=json.dumps(data, separators=(",", ":")), headers=headers)
    if response.status_code == 200:
        print("Request successful:")
        print(response.json())
    else:
        print("POST request failed. Status code:", response.status_code)
        print(response.text)
