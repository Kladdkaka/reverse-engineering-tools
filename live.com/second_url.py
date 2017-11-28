from urllib.parse import urlsplit, parse_qs
import requests

def get_qs():
    return urlsplit(requests.get('https://signup.live.com/signup', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}).history[0].headers['Location']).query

print()
print(get_qs())
print()
print(get_qs())
print()