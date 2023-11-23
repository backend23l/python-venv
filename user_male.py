import requests
import json
def get_user(gender):
    respons = requests.get("https://randomuser.me/api")
    if respons.status_code==200:
        con = respons.content
        data = json.loads(con.decode())
        randomuser = data['results'][0]
        if randomuser['gender']==gender:
            user = {
                "fullname":f"{randomuser['name']['first']} {randomuser['name']['last']}",
                'email':randomuser['email'],
                'phone':randomuser['phone'],
                "age":randomuser['dob']['age'],
                'gender':randomuser["gender"]
            }
            return user
        else:
            randomuser["gender"] = gender
            user = {
                "fullname":f"{randomuser['name']['first']} {randomuser['name']['last']}",
                'email':randomuser['email'],
                'phone':randomuser['phone'],
                "age":randomuser['dob']['age'],
                'gender':randomuser["gender"]
            }
    return user
def get_n_users(n:int,user)->list[dict]:
    users = []
    for i in range(n):
        users.append(user)
    return {"users":users , "info":{"count":n,"gender":user['gender']}}
def write_user(users:dict):
    with open("users.json","w") as w:
        data = json.dumps(users,indent=4)
        w.write(data)
get_user('female')
users = get_n_users(5,get_user('female'))
write_user(users)