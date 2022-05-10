import requests

r = requests.get('https://github.com/timeline.json')
print(r)

r = requests.post('https://httpbin.org/post')
