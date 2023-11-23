import requests
import json


response = requests.get('https://randomuser.me/api/')

if response.status_code == 200:
    content = response.content

    data = json.loads(content.decode())
    # print(data)

for i in data['results']:
    dic={}
    dic['fullname'] = f"{i['name']['first']} {i['name']['last']}"
    dic['email'] = i['email']
    dic['phone'] = i['cell']
    dic['age'] = i['dob']['age']
# print(dic)
