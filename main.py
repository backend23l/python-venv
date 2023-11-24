import json 
import requests

def get_user(gen):
    response = requests.get('https://randomuser.me/api/')
    if response.status_code==200:
        content = response.content
        data = json.loads(content.decode())
        randomuser = data["results"][0]
        user = None
        if randomuser['gender']==gen:
            user = {
                "gender":randomuser["gender"],
                "first":randomuser['name']['first'],
                "last":randomuser['name']['last'],
                "email":randomuser['email'],
                "phone":randomuser['phone'],
                "age":randomuser['dob']['age'],
            }
    return user

def get_n_users(n:int,gen:str):
    users = []
    i = 0
    while i < n:
        user = get_user(gen)
        if user != None:
            users.append(user)
            i -= 1
        i += 1

    return {"users":users,"info":{"Count":n}}

def write_users(use:dict):

    with open("male_female.json",'w') as f:
        data_json = json.dumps(use,indent=4)
        f.write(data_json)

users = get_n_users(9,"male")
write_users(users)