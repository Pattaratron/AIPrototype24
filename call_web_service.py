import requests
import json
    
# url = 'http://20.249.212.109:5006/simpleAPI'
# myobj = {'message_key': 'message_val',
#          'msg':'hi im pattaratron'}

# x = requests.post(url, data = json.dumps(myobj))
    
url = 'http://20.249.212.109:5006/simpleAPI'
myobj = {'name': 'Pattaratron', 'msg': 'Hi, I am Pattaratron!'}

x = requests.post(url, json=myobj)

print(x.json())  # แสดงผล response ที่ได้รับจาก API