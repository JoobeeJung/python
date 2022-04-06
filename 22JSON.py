# 22JSON.py   json.py
# voice over internet protocol
# VoIP, internet of things = IoT IOT
# JSON : JavaScript Object Notation JSON
# re


import json
myInfo = { "company":"KBStar", "city":"Seoul", "model":["김연아","BTS", "공유" ] }
print("myInfo = ", myInfo)

# json으로 만드는 행위 : 직렬화 (Serialize)
json.dumps(myInfo) # console

with open("./myInfo.json", "w" , encoding="utf8" ) as f:
    json.dump(myInfo, f)

# 역직렬화...
with open("./myInfo.json", "r", encoding="utf8") as f:
    readInfo = json.load(f)
    print("readInfo = " , readInfo)
    print("city = ", readInfo["city"])

