import json
import pprint

import execjs
from py_mini_racer import py_mini_racer

headers = {
    'authority': 'edith.xiaohongshu.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'xhsTrackerId=026c0cb3-a700-4cb3-8028-aa9250a459fb; xhsTrackerId.sig=sBicF6SeFKz1sG106f10CTLGxd1gBA1o3uVabWCNiEY; a1=186a0f1cf00cyprlnpc98qo6zobuu8jz9tm4aeaq030000818168; webId=8db5cbb3877e71dc815023bad3dcc9c8; gid=yYK08iyiWjj4yYK08iySi9d088SvUF1IUSjY6A8AlKulD4q877YVu0888YyYyKY8fdd84j22; gid.sign=z9YuhADLvkH9KOb6jOs4jijOMM4=; customerClientId=296354310261633; x-user-id-creator.xiaohongshu.com=62870393f683e3000128206d; access-token-creator.xiaohongshu.com=customer.ares.AT-1c2f5d30d2bd403b803d772cc6a2618e-33e23d08ee1f42ca8a9c2fd2bbc31efc; x-user-id-pgy.xiaohongshu.com=607e4f9b2b9c54000132a33b; xsecappid=xhs-pc-web; xhsTracker=url=explore&xhsshare=CopyLink; xhsTracker.sig=wmLdXV__wbETiz1qUgqoiY8swj2zGxC5B-xOV9HIhWg; webBuild=2.8.6; web_session=040069768cba5721084696de4c364b9de88f5f; websectiga=59d3ef1e60c4aa37a7df3c23467bd46d7f1da0b1918cf335ee7f2e9e52ac04cf; sec_poison_id=f82145d4-f9f4-4050-a03a-8a10334c8200',
    'origin': 'https://www.xiaohongshu.com',
    'pragma': 'no-cache',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'x-b3-traceid': 'eb421ef157255ea4',
    'x-s': 'XYW_eyJzaWduU3ZuIjoiNTEiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6ImIxMjYzNTcwNzY2MWIzODBhZjk4ZjQyMTY3NDg3NWJkOGIxYWMwNThmYTlmZDhkMDc2Y2E1YjY4OTUzY2M2ZTkzMWNiYTI0N2ExMGYzZTU1ZGRiZjQxOWVjYjMzNTg4Y2M5ZTNiZmRhMWZhYTFlYjkwZDc0YWEzMWI1NGM3MmNkMGQ3NGFhMzFiNTRjNzJjZGFjNDg5YjlkYThjZTVlNDhmNGFmYjlhY2ZjM2VhMjZmZTBiMjY2YTZiNGNjM2NiNWFjNzE3ZWMyYWQ1Y2NjZjAyOWFlYjk3NGIzYzVjN2UzODI0ZGU4ZTMwOWIxYTcxOTk2NzVlZGQ4YzE2NjMyYmE1OThmZDlhNGExYjQ1ZTI1ZTFhNDg4MzRiZjAwOGM3ODAyYTU1NmY3Yzc3MjIwZDE1ZmM4N2YyOTIwOTFhNzZjOGIyOTk5MDU4YTUwZmQ4OGNjM2MzYmU3YjcxZjhlZDA1YmY5YmI5ZTliMDcwZmZlMTI2NzA4NjM0NzkzOWJhYSJ9',
    'x-s-common': '2UQAPsHCPUIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1PUhAHjIj2eHjwjQ+GnPW/MPjNsQhPUHCHdYiqUMIGUM78nHjNsQh+sHCH0H1wsh9HjIj2eLjwjHlwe8YPBGlG9GIPB+EqoQVJdm0w/YlJA8CJ9QM4/Yx20SFJ/zY8nblPePIPeZIwerhP/GhHjIj2eGjw0r9weL9weWhw/cI+eHVHdW7H0ijnbSgg9pEadkYp9zMp/+y4LSxJ9Swprpk/r+t2fbg8opnaBl7nS+Q+DS187YQyg4knpYs4M+gLnSOyLiFGLY+4B+o/gzDPS8kanS7ynPUJBEjJbkVG9EwqBHU+BSOyLShanS7yn+oz0pjzASinD+Q+DSTagY+ySSC/Sz04FECn/Q+pFSC/FzsybkxyAzyySbE/pz8PFEr8A+wpFk3/F4Q2bSg/g4wpBYTnpzVJpkryBT+zBPUn/QbPpSxn/zOpbpCn/Q+PSkLy7k+pFEknpzQPrhUzgY+zMSCnSzpPpkoLfSyySbh/M4nySSx/gkwpBqFn/Q++pkL/fSyJpQi/p4yybSLzfl8yfT7nDz0PbSgzgk+pFDl/D4+PFMT/fT+zMrA/D4ByrMCzfSwpbQx/dktySkozfkwzBqMnnkVyMSLyBkypb8V/DziJLEozfM8yflin/QyyDFUpfY+ySkTnSzsyLMxn/Q8pbkk/D4wyDFU/fSwpF8x/dkbPMkg/gS8pMrln/QwySkxcgSOpF8Vnnk3PFEoagk82S8x/0Qp2DRra/myzMLFnSz+4FRgagY8pB+h/Mz3PDECpflyzMrFngkbPDEx/gS8JLLl/MziJpkrJBYwzFphnnkzPpkLa/bypr8i/Dzd+rMCLfSyyDb7/F4+PFRrcgS8pbLl/fM8PMSCGA++yDS7nDzbPpkT//zwPSSE/MzQ4FRLzfYw2Skx/F4Q2LRLyAp+zbLFnpzp4MkTL/zOzFEx//Q+2SSTp/+8yf+hnfkiJbkrc/b8JpDMnnMQ+pkLJBS+zB+7nfMyJrMLa/Qw2DrF/fk+PrECy7kOpFkinp+twaHVHdWhH0ija/PhqDYD87+xJ7mdag8Sq9zn494QcUT6aLpPJLQy+nLApd4G/B4BprShLA+jqg4bqD8S8gYDPBp3Jf+m2DMBnnEl4BYQyrkSL9E+zrTM4bQQPFTAnnRUpFYc4r4UGSGILeSg8DSkN9pgGA8SngbF2pbmqbmQPA4Sy9MaPpbPtApQy/8A8BE6q9k6pepEqgzGqgb7ngQsqnRQ2sV3zFzkN7+n4BTQ2emA2op7q0zl4BSQy7Q7anD6q9T0GA+QcFlfa/+O8/mM4BIUPrzyqFIM8Lz/afpxpdqIanSS8gYn4FI3Loz6qdbFybmTN9pL2Dq6ag8rzrSiqpzdpd4OadbF4LShzn+yLURSpdpFwLS94fpnpdzyanTVaFS3woQ1c/4AnpplPnQm+npxpdzCJMPMqM+0qS4C8epSLM40LrSh+np/4gzPaLLA8Lzl4rp6nnSi/0SPzFShJ9pL4g4VJfFA8gYDzpmQyM4OanSHJgbAwrzQcFzltF8nJFSkG9SSLocMaL+yyezs/d+rqrTS2obFcLDAcg+x8A4Ap9PROaHVHdWEH0iT+/P7P/DU+eW9NsQhP/Zjw0rlKc==',
    'x-t': '1685688894042',
}

if __name__ == '__main__':
    with open('xhs_xs.js', 'r', encoding='utf-8') as f:
        jstext = f.read()

    ctx = execjs.compile(jstext)

    api = "/api/sns/web/v1/comment/post" #评论api
    data = {"note_id": "6492ace6000000001300bdba", "content": "终于把你逆向了", "at_users": []}
    a1 = "184d1885b79kueq8zufxxah0brzchxbn06l7mjxbt00000242961" #为cookie中的ai字段，需要自己手动替换


    result = ctx.call("get_xs", api, data, a1)

    print(json.dumps(result,indent=4))
