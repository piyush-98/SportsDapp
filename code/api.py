import json
import requests
def match_info(mid):
        url="http://mapps.cricbuzz.com/cbzios/match/{}".format(mid)
        res=(requests.get(url))
        data=(json.loads(res.text))
        return(data)
d=match_info("22760")
print(d["team2"]["name"])