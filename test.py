import requests

#with open('a.txt', 'rb') as f:
#    r = requests.post('http://localhost:7979/api/upload/zortos', files={'file': f})
#    print(r.text)

w = requests.get('http://localhost:7979/api/download/zortos')
print(w.text)