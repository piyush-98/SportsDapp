import json
import requests

def scorecard(mid):
        url="http://mapps.cricbuzz.com/cbzios/match/{}/scorecard.json".format(mid)
        res=(requests.get(url))
        data=(json.loads(res.text))
        return(data)
data=scorecard("22773")
for i in data["Innings"]:
    for j in (i['batsmen']):
        print(j['r'])