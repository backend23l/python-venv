import requests
import json
from pprint import pprint


response = requests.get('https://randomuser.me/api/')

if response.status_code == 200:
    content = response.content

    data = json.loads(content.decode())
    
    randomuser = data['results'][0]

    user = {
        "fullname": f"{randomuser['name']['first']} {randomuser['name']['last']}",
        "email": randomuser['email'],
        "phone": randomuser['phone'],
        "age": randomuser['dob']['age'],
    }
    print(user)
    