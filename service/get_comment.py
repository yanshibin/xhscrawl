import json

import curlify

import utils.xs as util
import utils.mode as mode
import requests


myheaders = {
        'authority': 'edith.xiaohongshu.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'gid.sig=ooYpcOb3cch47JjSWAwFwlhzphfKxAPrMH4b3iOsWuo; gid.sign.sig=Ekn1RiJSw_am2RslNpYMMNojc7beWBp7MzXEvYIqIE4; smidV2=20220902154419cfdc03052f6ca93073821f716ec5153c006de92412963ee50; gid.ss=gSMQ9UOnDuZwH2oRGJG6BW6e4grs67TaYpnrW+8Wmd2l346RCyr+KJPPGa674999; a1=184d1885b79kueq8zufxxah0brzchxbn06l7mjxbt00000242961; webId=a1b67cc8bf1b7e409f32e7cc5175f36a; gid=yY4fyYY2dS8dyY4fyYY2DKVCWjT7dAYu7iCC1D90x8DFuW88SxCDI6888J4JjKy8YKSydd2y; gid.sign=3I/6BUxjRQtksJf1PKLWTqAU0yA=; timestamp2=167325189778920b7a70898e961e5c41797c5855e121b9616a71daa60689e8f; timestamp2.sig=xs56JeTSkpYMjP9wAuZiWJ9AvOlaACxb3Fxuec0aHiw; xhsTrackerId=4fb80133-9401-4b1b-b5bd-5888c4d842c9; xhsTrackerId.sig=wRvoxQcH01_D6sGBV8gnJr0UKPA6gciNdLAHzT6xZnc; web_session=040069b525b1e7f73f25051190364ba70d3447; sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%221892a922d5c1844-018978860d2fd2-1b525634-1296000-1892a922d5d1e84%22%7D; galaxy_creator_session_id=jdBnU0ReSoonuI50cY9gUJazaFjLBYERyS2o; galaxy.creator.beaker.session.id=1690896681180075278854; webBuild=2.18.4; xsecappid=xhs-pc-web; websectiga=6169c1e84f393779a5f7de7303038f3b47a78e47be716e7bec57ccce17d45f99; sec_poison_id=c60b832f-d035-4f02-b1f7-bfbe096f86e4',
        'origin': 'https://www.xiaohongshu.com',
        'referer': 'https://www.xiaohongshu.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-b3-traceid': '41dfdddfad87e5a4',
        'x-s': 'XYW_eyJzaWduU3ZuIjoiNTEiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6IjNiMjczZDA4MjExYzYyMWI0NGQ3MTdjYjUwNTAxMzk4YTAxM2M1ZGJhNjhiZjU2OWQ5MWI0YjA1YmRjMGFmYWRiMzBiOTlkN2U5MjI4MWViYzA0ZjUyMGZkMzg5ZmM1ZmM5ZTNiZmRhMWZhYTFlYjkwZDc0YWEzMWI1NGM3MmNkMGQ3NGFhMzFiNTRjNzJjZGFjNDg5YjlkYThjZTVlNDhmNGFmYjlhY2ZjM2VhMjZmZTBiMjY2YTZiNGNjM2NiNTU3OGY5ODYyNTFiYmUwNzAyMGM3NmQ5ODQzY2NjMTZkY2ZhY2FhZTg2N2YyZmFkNWZiNDY4NzI2YzEwMTI1MTE2MTA2MTNkOWJiNWNkNzgyYzFmMWJlMWI1YWE0NzNiNjAzMTdhMjcxZWQ5NDAwZjQzNThlYTVkODlkZDgzNmQ1MmExMzRhNmZkNGU1YmJjMGJmMjcwZGE5ODBiMTRhMjU5Nzg1OTg0YjdiOWU2Mzg1MzY4ODFkMWQ4NzIyOTQwOCJ9',
        'x-s-common': '2UQAPsHCPUIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1+jhIHjIj2eHjwjQ+GnPW/MPjNsQhPUHCHdYiqUMIGUM78nHjNsQh+sHCH0H1P/W1+sHVHdWMH0ijP/WF8erhwepj+AS34nplwokM8dYhGnWIGdQCG9YhGfhI+fI7JnkhGdcIPeZIPeHFP0D9PaHVHdW9H0il+0DIw/D7PeLEw/WhNsQh+UHCHSY8pMRS2LkCGp4D4pLAndpQyfRk/SzbyLleadkYp9zMpDYV4Mk/a/8QJf4hanS7ypSGcd4/pMbk/9St+BbH/gz0zFMF8eQnyLSk49S0Pfl1GflyJB+1/dmjP0zk/9SQ2rSk49S0zFGMGDqEybkea/8QyDEk/nk02Skrc/z+yDphngk82LMga/mwzMrA/pzDySSxpg4wprbh/gk3+bSLcgY+PDFlnD4tyrExyBSyySLU/M4z+LMga/m8yDrlnnMayDMozfM8pMQk/gksyLRLJBTwPSLM/nkQ+rMgpfS82DrInfkp2LMonfT+2fqMnfM+PpkT//pyprEknfMayrMgnfY8pr8Vnnk34MkrGAm8pFpC/p4QPLEo//++JLE3/L4zPFEozfY+2D8k/SzayDECafkyzF8x/Dzd+pSxJBT8pBYxnSznJrEryBMwzF8TnnkVybDUnfk+PS8i/nkyJpkLcfS+ySDUnpzyyLEo/fk+PDEk/SzpPFRon/pOzbSE/SzBypSTpg4w2DbE/L4+PFETL/pOzbbCn/QwyDMLnfT8PSkin/QBybkL8AQwPSSEnfMByFEgnfSwzbDF/dkQPSSCzg4+prDl/pzbPDMLc/Q+prE3/M4tyLEg/fTw2f4EngkBJLMgafl+pFDlnp4bPrEC/fSwyDbC/pzDyrMxG7YypMrM/Dzm4MkxLgkwpBYVnpznyFRrJBTyzB4C/fMzPLMTzgY+2SQi/fMyyFEop/b8JLkx/L4tJLMxG74yzFLM/FzsyLMLLfY+ySLM/dkdPLRL8Am8yfzk/M4pPDMC8Ab+2SDF/FzByFMgL/zw2DSE/Mzz4FRea0DjNsQhwsHCHDDAwoQH8B4AyfRI8FS98g+Dpd4daLP3JFSb/BMsn0pSPM87nrldzSzQ2bPAGdb7zgQB8nph8emSy9E0cgk+zSS1qgzianYt8Lz1/LzN4gzaa/+NqMS6qS4HLozoqfQnPbZEp98QyaRSp9P98pSl4oSzcgmca/P78nTTL0bz/sVManD9q9z1J7+xJMcM2gbFnobl4MSUcdb6agW3tF4ryaRApdz3agWIq7YM47HFqgzkanTU4FSkN7+3G9PAaL+P8DDA/9LI4gzVP0mrnd+P+nprLFkSyS87PrSk8nphpd4PtMmFJ7Ql4BY72fpSy9Mg+rSht9SQyoQa2S878FTc4bSQPMbcJFzN8/8l4BYQ2sRA+S8FJFSk/nRQyLL6q9h98p+DqpzU8d8AydpFa7Qy89pfG7HE898N8pS0LBpQ2rTS8dpFaDSb89pfqgzBqSSryrh7/BEQ2epAP7bFLfE0+9pn8Dq3anT04FSkaocFPBQ+ag8iqgz/wB4QynSfqb87cLSeab8tJA+SL7mS8nTc4b8Q2e+SPBkHOaHVHdWEH0iUP/PEw/q9+/HFNsQhP/Zjw0c7woF=',
        'x-t': '1690997059988'
    }

_note_id = '64bd0bf5000000000800d6a1'
_cursor = ''
_top_comment_id = ''
params = {
    'note_id': _note_id,
    'cursor': _cursor,
    'top_comment_id': _top_comment_id,
}
_getCommenturi = f"/api/sns/web/v2/comment/page?note_id={_note_id}&cursor={_cursor}&top_comment_id={_top_comment_id}"
_getCommentApi = "/api/sns/web/v2/comment/page"
_cookie = "gid.sig=ooYpcOb3cch47JjSWAwFwlhzphfKxAPrMH4b3iOsWuo; gid.sign.sig=Ekn1RiJSw_am2RslNpYMMNojc7beWBp7MzXEvYIqIE4; smidV2=20220902154419cfdc03052f6ca93073821f716ec5153c006de92412963ee50; gid.ss=gSMQ9UOnDuZwH2oRGJG6BW6e4grs67TaYpnrW+8Wmd2l346RCyr+KJPPGa674999; a1=184d1885b79kueq8zufxxah0brzchxbn06l7mjxbt00000242961; webId=a1b67cc8bf1b7e409f32e7cc5175f36a; gid=yY4fyYY2dS8dyY4fyYY2DKVCWjT7dAYu7iCC1D90x8DFuW88SxCDI6888J4JjKy8YKSydd2y; gid.sign=3I/6BUxjRQtksJf1PKLWTqAU0yA=; timestamp2=167325189778920b7a70898e961e5c41797c5855e121b9616a71daa60689e8f; timestamp2.sig=xs56JeTSkpYMjP9wAuZiWJ9AvOlaACxb3Fxuec0aHiw; xhsTrackerId=4fb80133-9401-4b1b-b5bd-5888c4d842c9; xhsTrackerId.sig=wRvoxQcH01_D6sGBV8gnJr0UKPA6gciNdLAHzT6xZnc; web_session=040069b525b1e7f73f25051190364ba70d3447; sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%221892a922d5c1844-018978860d2fd2-1b525634-1296000-1892a922d5d1e84%22%7D; galaxy_creator_session_id=jdBnU0ReSoonuI50cY9gUJazaFjLBYERyS2o; galaxy.creator.beaker.session.id=1690896681180075278854; webBuild=2.18.4; xsecappid=xhs-pc-web; websectiga=9730ffafd96f2d09dc024760e253af6ab1feb0002827740b95a255ddf6847fc8; sec_poison_id=0880d778-c586-4ca2-83be-78a96c3d6a61"

if __name__ == '__main__':
    crypt = util.GetXsForGet( _getCommentApi)
    print(crypt['X-s'])
    print(myheaders['x-s'])
    #
    # headers = mode.GetHeaders(cookie=_cookie, crypt=crypt)
    # print(mode.EdithHost +_getCommentApi)
    # myheaders['x-s'] = crypt['X-s']
    # myheaders['x-t'] = str(crypt['X-t'])
    # resp = requests.get('https://edith.xiaohongshu.com/api/sns/web/v2/comment/page',params=params, headers=myheaders)
    # session = requests.session()
    # resp = session.get(mode.EdithHost + _getCommentApi,  headers=headers)

    # print(curlify.to_curl(resp.request))
    print(resp.text)
    print(resp.status_code)
#
# import json
#
# import requests
# if __name__ == '__main__':
#     url = 'https://edith.xiaohongshu.com/api/sns/web/v2/comment/page'
#
#
#     params = {
#         'note_id': '64bd0bf5000000000800d6a1',
#         'cursor': '',
#         'top_comment_id': ''
#     }
#
#     response = requests.get(url, headers=myheaders, params=params)
#     print(response.status_code)
#     print(json.dumps(response.json() ,indent = 4,ensure_ascii=False))
