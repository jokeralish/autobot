from line import *
import requests
import json
import random
import string

def randstr(n):
    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
    return random_str

host = 'https://gwk.line.naver.jp'
LA = "BIZIOS\t1.7.5\tiOS\t10.2"
header = {
    'Accept':"application/json",
    "Accept-Language":"ja-KR",
    "X-LHM":'POST',
    "X-LPV":'1',
    'X-Line-Application':LA,
    'User-Agent':LA
}
line = LINE(idOrAuthToken='PukqfiJHXTi9ALRYUV8RRfXM6ib21eGvcNnnplqQIjQH9Z0cetJ6D9J0bcQvYwuvc/OM/yvfDw1Qp1DcrKqAWrsXO1E1rTcGJcq/+edlhxDTLrKFgskCYIsQMKQcpbOCNmG32YQrCOF8GLjzZmKKLQdB04t89/1O/w1cDnyilFU=')
channel_token = line.issueChannelToken('1603505719').channelAccessToken
print(channel_token)
payload = {"PukqfiJHXTi9ALRYUV8RRfXM6ib21eGvcNnnplqQIjQH9Z0cetJ6D9J0bcQvYwuvc/OM/yvfDw1Qp1DcrKqAWrsXO1E1rTcGJcq/+edlhxDTLrKFgskCYIsQMKQcpbOCNmG32YQrCOF8GLjzZmKKLQdB04t89/1O/w1cDnyilFU=":channel_token, "udidHash":open('udidHash.txt').read()}
endpoint = '/plc/api/core/auth/cmsToken'
res = requests.post(host+endpoint, data=json.dumps(payload), headers=header)
print(res.json()["accessToken"]) # CMSToken
