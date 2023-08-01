import json
import pprint

import re
import execjs
from py_mini_racer import py_mini_racer

# headers = {
#     'authority': 'edith.xiaohongshu.com',
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cache-control': 'no-cache',
#     'cookie': 'gid.sig=ooYpcOb3cch47JjSWAwFwlhzphfKxAPrMH4b3iOsWuo; gid.sign.sig=Ekn1RiJSw_am2RslNpYMMNojc7beWBp7MzXEvYIqIE4; smidV2=20220902154419cfdc03052f6ca93073821f716ec5153c006de92412963ee50; gid.ss=gSMQ9UOnDuZwH2oRGJG6BW6e4grs67TaYpnrW+8Wmd2l346RCyr+KJPPGa674999; a1=184d1885b79kueq8zufxxah0brzchxbn06l7mjxbt00000242961; webId=a1b67cc8bf1b7e409f32e7cc5175f36a; gid=yY4fyYY2dS8dyY4fyYY2DKVCWjT7dAYu7iCC1D90x8DFuW88SxCDI6888J4JjKy8YKSydd2y; gid.sign=3I/6BUxjRQtksJf1PKLWTqAU0yA=; timestamp2=167325189778920b7a70898e961e5c41797c5855e121b9616a71daa60689e8f; timestamp2.sig=xs56JeTSkpYMjP9wAuZiWJ9AvOlaACxb3Fxuec0aHiw; xhsTrackerId=4fb80133-9401-4b1b-b5bd-5888c4d842c9; xhsTrackerId.sig=wRvoxQcH01_D6sGBV8gnJr0UKPA6gciNdLAHzT6xZnc; web_session=040069b525b1e7f73f25051190364ba70d3447; sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%221892a922d5c1844-018978860d2fd2-1b525634-1296000-1892a922d5d1e84%22%7D; xsecappid=xhs-pc-web; webBuild=2.18.4; websectiga=634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a; sec_poison_id=e8e5e088-0923-4a12-983e-b6a71580af07',
#     'origin': 'https://www.xiaohongshu.com',
#     'pragma': 'no-cache',
#     'referer': 'https://www.xiaohongshu.com/',
#     'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
#     'x-b3-traceid': 'eb421ef157255ea4',
#     'x-s': 'XYW_eyJzaWduU3ZuIjoiNTEiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6ImIxMjYzNTcwNzY2MWIzODBhZjk4ZjQyMTY3NDg3NWJkOGIxYWMwNThmYTlmZDhkMDc2Y2E1YjY4OTUzY2M2ZTkzMWNiYTI0N2ExMGYzZTU1ZGRiZjQxOWVjYjMzNTg4Y2M5ZTNiZmRhMWZhYTFlYjkwZDc0YWEzMWI1NGM3MmNkMGQ3NGFhMzFiNTRjNzJjZGFjNDg5YjlkYThjZTVlNDhmNGFmYjlhY2ZjM2VhMjZmZTBiMjY2YTZiNGNjM2NiNWFjNzE3ZWMyYWQ1Y2NjZjAyOWFlYjk3NGIzYzVjN2UzODI0ZGU4ZTMwOWIxYTcxOTk2NzVlZGQ4YzE2NjMyYmE1OThmZDlhNGExYjQ1ZTI1ZTFhNDg4MzRiZjAwOGM3ODAyYTU1NmY3Yzc3MjIwZDE1ZmM4N2YyOTIwOTFhNzZjOGIyOTk5MDU4YTUwZmQ4OGNjM2MzYmU3YjcxZjhlZDA1YmY5YmI5ZTliMDcwZmZlMTI2NzA4NjM0NzkzOWJhYSJ9',
#     'x-s-common': '2UQAPsHCPUIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1PUhAHjIj2eHjwjQ+GnPW/MPjNsQhPUHCHdYiqUMIGUM78nHjNsQh+sHCH0H1wsh9HjIj2eLjwjHlwe8YPBGlG9GIPB+EqoQVJdm0w/YlJA8CJ9QM4/Yx20SFJ/zY8nblPePIPeZIwerhP/GhHjIj2eGjw0r9weL9weWhw/cI+eHVHdW7H0ijnbSgg9pEadkYp9zMp/+y4LSxJ9Swprpk/r+t2fbg8opnaBl7nS+Q+DS187YQyg4knpYs4M+gLnSOyLiFGLY+4B+o/gzDPS8kanS7ynPUJBEjJbkVG9EwqBHU+BSOyLShanS7yn+oz0pjzASinD+Q+DSTagY+ySSC/Sz04FECn/Q+pFSC/FzsybkxyAzyySbE/pz8PFEr8A+wpFk3/F4Q2bSg/g4wpBYTnpzVJpkryBT+zBPUn/QbPpSxn/zOpbpCn/Q+PSkLy7k+pFEknpzQPrhUzgY+zMSCnSzpPpkoLfSyySbh/M4nySSx/gkwpBqFn/Q++pkL/fSyJpQi/p4yybSLzfl8yfT7nDz0PbSgzgk+pFDl/D4+PFMT/fT+zMrA/D4ByrMCzfSwpbQx/dktySkozfkwzBqMnnkVyMSLyBkypb8V/DziJLEozfM8yflin/QyyDFUpfY+ySkTnSzsyLMxn/Q8pbkk/D4wyDFU/fSwpF8x/dkbPMkg/gS8pMrln/QwySkxcgSOpF8Vnnk3PFEoagk82S8x/0Qp2DRra/myzMLFnSz+4FRgagY8pB+h/Mz3PDECpflyzMrFngkbPDEx/gS8JLLl/MziJpkrJBYwzFphnnkzPpkLa/bypr8i/Dzd+rMCLfSyyDb7/F4+PFRrcgS8pbLl/fM8PMSCGA++yDS7nDzbPpkT//zwPSSE/MzQ4FRLzfYw2Skx/F4Q2LRLyAp+zbLFnpzp4MkTL/zOzFEx//Q+2SSTp/+8yf+hnfkiJbkrc/b8JpDMnnMQ+pkLJBS+zB+7nfMyJrMLa/Qw2DrF/fk+PrECy7kOpFkinp+twaHVHdWhH0ija/PhqDYD87+xJ7mdag8Sq9zn494QcUT6aLpPJLQy+nLApd4G/B4BprShLA+jqg4bqD8S8gYDPBp3Jf+m2DMBnnEl4BYQyrkSL9E+zrTM4bQQPFTAnnRUpFYc4r4UGSGILeSg8DSkN9pgGA8SngbF2pbmqbmQPA4Sy9MaPpbPtApQy/8A8BE6q9k6pepEqgzGqgb7ngQsqnRQ2sV3zFzkN7+n4BTQ2emA2op7q0zl4BSQy7Q7anD6q9T0GA+QcFlfa/+O8/mM4BIUPrzyqFIM8Lz/afpxpdqIanSS8gYn4FI3Loz6qdbFybmTN9pL2Dq6ag8rzrSiqpzdpd4OadbF4LShzn+yLURSpdpFwLS94fpnpdzyanTVaFS3woQ1c/4AnpplPnQm+npxpdzCJMPMqM+0qS4C8epSLM40LrSh+np/4gzPaLLA8Lzl4rp6nnSi/0SPzFShJ9pL4g4VJfFA8gYDzpmQyM4OanSHJgbAwrzQcFzltF8nJFSkG9SSLocMaL+yyezs/d+rqrTS2obFcLDAcg+x8A4Ap9PROaHVHdWEH0iT+/P7P/DU+eW9NsQhP/Zjw0rlKc==',
#     'x-t': '1685688894042',
# }

cookie = 'gid.sig=ooYpcOb3cch47JjSWAwFwlhzphfKxAPrMH4b3iOsWuo; gid.sign.sig=Ekn1RiJSw_am2RslNpYMMNojc7beWBp7MzXEvYIqIE4; smidV2=20220902154419cfdc03052f6ca93073821f716ec5153c006de92412963ee50; gid.ss=gSMQ9UOnDuZwH2oRGJG6BW6e4grs67TaYpnrW+8Wmd2l346RCyr+KJPPGa674999; a1=184d1885b79kueq8zufxxah0brzchxbn06l7mjxbt00000242961; webId=a1b67cc8bf1b7e409f32e7cc5175f36a; gid=yY4fyYY2dS8dyY4fyYY2DKVCWjT7dAYu7iCC1D90x8DFuW88SxCDI6888J4JjKy8YKSydd2y; gid.sign=3I/6BUxjRQtksJf1PKLWTqAU0yA=; timestamp2=167325189778920b7a70898e961e5c41797c5855e121b9616a71daa60689e8f; timestamp2.sig=xs56JeTSkpYMjP9wAuZiWJ9AvOlaACxb3Fxuec0aHiw; xhsTrackerId=4fb80133-9401-4b1b-b5bd-5888c4d842c9; xhsTrackerId.sig=wRvoxQcH01_D6sGBV8gnJr0UKPA6gciNdLAHzT6xZnc; web_session=040069b525b1e7f73f25051190364ba70d3447; sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%221892a922d5c1844-018978860d2fd2-1b525634-1296000-1892a922d5d1e84%22%7D; xsecappid=xhs-pc-web; webBuild=2.18.4; websectiga=634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a; sec_poison_id=e8e5e088-0923-4a12-983e-b6a71580af07'

def GetXs( cookie, api, data):
    with open('xhs_xs.js', 'r', encoding='utf-8') as f:
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

if __name__ == '__main__':

    api = "/api/sns/web/v1/comment/post"  # 评论api
    data = {"note_id": "64bd0bf5000000000800d6a1", "content": "2", "at_users": []} #所需的参数字典
    xs = GetXs(cookie, api, data)
    print(json.dumps(xs, indent=4))
