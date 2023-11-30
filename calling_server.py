import requests

# r = requests.get('http://127.0.0.1:5000/help')0
r = requests.post('http://127.0.0.1:5000/testing', json={"mydata": '4'})
r.status_code
r.text


r = requests.post('https://mill-she-mailto-wishlist.trycloudflare.com/testing', json={"mydata": "4"})
r.text



