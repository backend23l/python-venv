from requests import get

base_url = 'https://randomuser.me/'
endpoint = 'api/'

url = base_url + endpoint
payload = {
    'results': 50,
    'gender': 'female',
    'nat': 'ua'
}

response = get(url=url, params=payload)
if response.status_code == 200:
    data = response.json()
    users = data['results']

    print(users)
else:
    print('error')