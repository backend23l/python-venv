import requests
import json

def get_user(gender:str) -> dict:
    respon=requests.get('http://randomuser.me/api/')
    if respon.status_code==200:
        content=respon.content
        data=json.loads(content.decode())
        randomuser=data['results'][0]
        if randomuser['gender']==gender:
            user={
                "fullname": f"{randomuser['name']['first']} {randomuser['name']['last']}",
                "gender": randomuser['gender'],
                "email": randomuser['email'],
                "phone": randomuser['phone'],
                "age": randomuser['dob']['age']
            }
            return user
        else:
            randomuser['gender']=gender
            user={
                "fullname": f"{randomuser['name']['first']} {randomuser['name']['last']}",
                "gender": randomuser['gender'],
                "email": randomuser['email'],
                "phone": randomuser['phone'],
                "age": randomuser['dob']['age']
            }
            return user
def get_n_users(n:int,gender:str) -> list[dict]:
    users=[]
    for i in range(n):
        user=get_user(gender)
        users.append(user)
    return {"users":users,"info":{"count":n},"gender":{f"{gender} count": n}}
def write_users(users: dict):
    with open('users.json','w') as f:
        data_json=json.dumps(users,indent=4)
        f.write(data_json)
users=get_n_users(20,"male")
write_users(users)
