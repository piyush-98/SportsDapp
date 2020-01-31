import json
import requests
def match_info(mid):
        url="http://mapps.cricbuzz.com/cbzios/match/{}".format(mid)
        res=(requests.get(url))
        data=(json.loads(res.text))
        return(data)
data=(match_info("23859"))
for i in data['players']:
    print(i['speciality'])