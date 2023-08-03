# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 11:48
# @Author  : 蔍鸣霸霸
# @FileName: red_book_comment.py
# @Software: PyCharm
# @Blog    ：只因你太美
import time

import execjs
import requests

headers = {
    'authority': 'edith.xiaohongshu.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'gid.sig=ooYpcOb3cch47JjSWAwFwlhzphfKxAPrMH4b3iOsWuo; gid.sign.sig=Ekn1RiJSw_am2RslNpYMMNojc7beWBp7MzXEvYIqIE4; smidV2=20220902154419cfdc03052f6ca93073821f716ec5153c006de92412963ee50; gid.ss=gSMQ9UOnDuZwH2oRGJG6BW6e4grs67TaYpnrW+8Wmd2l346RCyr+KJPPGa674999; a1=184d1885b79kueq8zufxxah0brzchxbn06l7mjxbt00000242961; webId=a1b67cc8bf1b7e409f32e7cc5175f36a; gid=yY4fyYY2dS8dyY4fyYY2DKVCWjT7dAYu7iCC1D90x8DFuW88SxCDI6888J4JjKy8YKSydd2y; gid.sign=3I/6BUxjRQtksJf1PKLWTqAU0yA=; timestamp2=167325189778920b7a70898e961e5c41797c5855e121b9616a71daa60689e8f; timestamp2.sig=xs56JeTSkpYMjP9wAuZiWJ9AvOlaACxb3Fxuec0aHiw; xhsTrackerId=4fb80133-9401-4b1b-b5bd-5888c4d842c9; xhsTrackerId.sig=wRvoxQcH01_D6sGBV8gnJr0UKPA6gciNdLAHzT6xZnc; web_session=040069b525b1e7f73f25051190364ba70d3447; sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%221892a922d5c1844-018978860d2fd2-1b525634-1296000-1892a922d5d1e84%22%7D; galaxy_creator_session_id=jdBnU0ReSoonuI50cY9gUJazaFjLBYERyS2o; galaxy.creator.beaker.session.id=1690896681180075278854; xsecappid=xhs-pc-web; webBuild=2.18.4; websectiga=cf46039d1971c7b9a650d87269f31ac8fe3bf71d61ebf9d9a0a87efb414b816c; sec_poison_id=8b2bc291-33e5-4b19-9a91-4ae7723e2d94',
    'origin': 'https://www.xiaohongshu.com',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-b3-traceid': '2ebb89801a52c739',
    'x-s': 'XYW_eyJzaWduU3ZuIjoiNTEiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6IjE4MDYxM2YwNWZjZTljMWE5MWUyMGY0NjkyNzg4NDE3NTE1NDM5MGVjOWFiYTA4YTI1MjNlOTY0ODc3Y2QzYjgxMDM0MzQzZjQzNGE5NDg5NjQ4MjIwMjViODhlOTJkZWM5ZTNiZmRhMWZhYTFlYjkwZDc0YWEzMWI1NGM3MmNkMGQ3NGFhMzFiNTRjNzJjZGFjNDg5YjlkYThjZTVlNDhmNGFmYjlhY2ZjM2VhMjZmZTBiMjY2YTZiNGNjM2NiNTU3OGY5ODYyNTFiYmUwNzAyMGM3NmQ5ODQzY2NjMTZkY2ZhY2FhZTg2N2YyZmFkNWZiNDY4NzI2YzEwMTI1MTE2MTA2MTNkOWJiNWNkNzgyYzFmMWJlMWI1YWE0NzNiNjAzMTdhMjcxZWQ5NDAwZjQzNThlYTVkODlkZDgzNmQ1MmExMzRhNmZkNGU1YmJjMDQ5NDlmMWJmMTliYjlmMzU0ZDY5ODcwYjJlYTE0YzQwYTdhNzQ0NzkzOGFkZWU5NyJ9',
    'x-s-common': '2UQAPsHCPUIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1+jhIHjIj2eHjwjQ+GnPW/MPjNsQhPUHCHdYiqUMIGUM78nHjNsQh+sHCH0H1P/W1+sHVHdWMH0ijP/WF8erhwepj+AS34nplwokM8dYhGnWIGdQCG9YhGfhI+fI7JnkhGdcIPeZIPeHFP0D9PaHVHdW9H0il+0DlPecEPAPMP/rENsQh+UHCHSY8pMRS2LkCGp4D4pLAndpQyfRk/SzbyLleadkYp9zMpDYV4Mk/a/8QJf4hanS7ypSGcd4/pMbk/9St+BbH/gz0zFMF8eQnyLSk49S0Pfl1GflyJB+1/dmjP0zk/9SQ2rSk49S0zFGMGDqEybkea/8QyDLF/Lz82rFUng4wpMkxnSzVyDMgz/p+pMpE/L48PrExy7Sw2fqF/DzbPFELz/bwzrFM/L4nyDRgzfS8prrFnpzQPLMx/flOpbDI/Fz0PMDULgk8yf4h/Lz+PrMCLgkyySbC/D4b+LEr8ApwySrF/nkQ4FMxpfSOzBYV/MztyMkg//pyprEknfMayrMgnfY8pr8Vnnk34MkrGAm8pFpC/p4QPLEo//++JLE3/L4zPFEozfY+2D8k/SzayDECafkyzF8x/Dzd+pSxJBT8pBYxnSznJrEryBMwzF8TnnkVybDUnfk+PS8i/nkyJpkLcfS+ySDUnpzyyLEo/fk+PDEk/SzpPFRon/pOzbSE/SzBypSTpg4w2DbE/L4+PFETL/pOzbbCn/QwyDMLnfT8PSkin/QBybkL8AQwPSSEnfMByFEgnfSwzbDF/dkQPSSCzg4+prDl/pzbPDMLc/Q+prE3/M4tyLEg/fTw2f4EngkBJLMgafl+pFDlnp4bPrEC/fSwyDbC/pzDyrMxG7YypMrM/Dzm4MkxLgkwpBYVnpznyFRrJBTyzB4C/fMzPLMTzgY+2SQi/fMyyFEop/b8JLkx/Lzz+LErJBM+pFkT/pzVypSxJBM+2SLInDz8+LRrG748yDkVnpzbPbSCLg48pBzi/dkzPrECy7kOzF83nS4p+LEEa0DjNsQhwsHCHDDAwoQH8B4AyfRI8FS98g+Dpd4daLP3JFSb/BMsn0pSPM87nrldzSzQ2bPAGdb7zgQB8nph8emSy9E0cgk+zSS1qgzianYt8p+1/LzN4gzaa/+NqMS6qS4HLozoqfQnPbZEp98QyaRSp9P98pSl4oSzcgmca/P78nTTL0bz/sVManD9q9z1J7+xJMcM2gbFnobl4MSUcdb6agW3tF4ryaRApdz3agWIq7YM47HFqgzkanTU4FSkN7+3G9PAaL+P8DDA/9LI4gzVP0mrnd+P+nprLFkSyS87PrSk8nphpd4PtMmFJ7Ql4BY7Jn4Sy9Mg+rSht9SQyoQa2S878FTc4bSQPMbcJFzN8/8l4BYQ2sRA+S8FJFSk/nRQyLL6q9h98p+DqpzU8d8AydpFa7Qy89pfG7HE898N8pS0LBpQ2rkSzb8FJDSb+fpfpdzpGfliapbD/BEQ2epAP7bFLfE0+9pn8Dq3anT04FSkaocFPBQ+ag8iqgz/wB4QynSfqb87cLSeab8tJA+SL7mS8nTc4b8Q2e+SPBkHOaHVHdWEH0iT+/Dhwer7+/rhNsQhP/Zjw0rIKc==',
    'x-t': '1691049335119'
}


def get_xs(source_note_id, cursor=None):
    if cursor is None:
        cursor = ''
    with open('xhs_xs.js', 'r', encoding='utf-8') as f:
        js = f.read()
    crt = execjs.compile(js)
    xs_xt = crt.call('get_xs', f'/api/sns/web/v2/comment/page?note_id={source_note_id}&cursor={cursor}&top_comment_id=')
    xs_xt['X-t'] = str(xs_xt['X-t'])
    headers.update(xs_xt)


def get_comment(source_note_id):
    get_xs(source_note_id)
    response = requests.get(
        f'https://edith.xiaohongshu.com/api/sns/web/v2/comment/page?note_id={source_note_id}&cursor=&top_comment_id=',
        headers=headers).json()
    print(response)


# /api/sns/web/v2/comment/page?note_id=640070c90000000013001b92&cursor=64084ec5000000000b0300e6
# /api/sns/web/v2/comment/page?note_id=640070c90000000013001b92&cursor=64084ec5000000000b0300e6
if __name__ == '__main__':
    get_comment('640070c90000000013001b92')