import requests 
import json
def get_user():
    respons = requests.get("https://randomuser.me/api")
    if respons.status_code==200:
        content = respons.content
        data = json.loads(content.decode())
        randomuser = data['results'][0]
        user = {
            "fullname": f"{randomuser['name']['first']} {randomuser['name']['last']}",
            "phone": randomuser['phone'],
            "email":randomuser['email'],
            "age": randomuser['dob']['age']
            
        }
    return user
def get_n_user(n:int)->list[dict]:
    users = []
    for i in range(n):
        user = get_user()
        users.append(user)
    return {"users":users,"info":{"count":n}}
def write_user(users:dict):
    with open("user.json","w") as w:
        data_json = json.dumps(users,indent=4)
        w.write(data_json)
users = get_n_user(5)
write_user(users)

