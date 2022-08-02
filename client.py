import requests

HOST = 'http://127.0.0.1:8080'

resp = requests.delete(f'{HOST}/advs/13')

print(resp.status_code)
print(resp.text)
