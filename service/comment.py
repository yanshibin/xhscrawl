import json

import curlify

import utils.xs as util
import utils.mode as mode
import requests

_commentApi = '/api/sns/web/v1/comment/post'
_cookie = "gid.sig=ooYpcOb3cch47JjSWAwFwlhzphfKxAPrMH4b3iOsWuo; gid.sign.sig=Ekn1RiJSw_am2RslNpYMMNojc7beWBp7MzXEvYIqIE4; smidV2=20220902154419cfdc03052f6ca93073821f716ec5153c006de92412963ee50; gid.ss=gSMQ9UOnDuZwH2oRGJG6BW6e4grs67TaYpnrW+8Wmd2l346RCyr+KJPPGa674999; a1=184d1885b79kueq8zufxxah0brzchxbn06l7mjxbt00000242961; webId=a1b67cc8bf1b7e409f32e7cc5175f36a; gid=yY4fyYY2dS8dyY4fyYY2DKVCWjT7dAYu7iCC1D90x8DFuW88SxCDI6888J4JjKy8YKSydd2y; gid.sign=3I/6BUxjRQtksJf1PKLWTqAU0yA=; timestamp2=167325189778920b7a70898e961e5c41797c5855e121b9616a71daa60689e8f; timestamp2.sig=xs56JeTSkpYMjP9wAuZiWJ9AvOlaACxb3Fxuec0aHiw; xhsTrackerId=4fb80133-9401-4b1b-b5bd-5888c4d842c9; xhsTrackerId.sig=wRvoxQcH01_D6sGBV8gnJr0UKPA6gciNdLAHzT6xZnc; web_session=040069b525b1e7f73f25051190364ba70d3447; sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%221892a922d5c1844-018978860d2fd2-1b525634-1296000-1892a922d5d1e84%22%7D; galaxy_creator_session_id=jdBnU0ReSoonuI50cY9gUJazaFjLBYERyS2o; galaxy.creator.beaker.session.id=1690896681180075278854; webBuild=2.18.4; xsecappid=xhs-pc-web; websectiga=9730ffafd96f2d09dc024760e253af6ab1feb0002827740b95a255ddf6847fc8; sec_poison_id=0880d778-c586-4ca2-83be-78a96c3d6a61"
_noteId = "64bd0bf5000000000800d6a1"
_commentText = "1"
_data = {"note_id": _noteId, "content": _commentText, "at_users": []}

if __name__ == '__main__':
    crypt = util.GetXsForPost(_cookie, _commentApi, _data)
    headers = mode.GetHeaders(cookie=_cookie, crypt=crypt)
    dumpData = json.dumps(_data, separators=(",", ":"), ensure_ascii=False)

    session = requests.session()
    resp = session.post( mode.EdithHost + _commentApi, data=json.dumps(_data, separators=(",", ":")) , headers=headers,verify=False)

    # print(curlify.to_curl(resp.request))
    print(resp.text)
    print(resp.status_code)
