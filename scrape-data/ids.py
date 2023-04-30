import urllib.request
import gzip
import json
import time
from PRIVATE.headers import HEADERS


def get_user_id(username):
    host = f"https://www.instagram.com/web/search/topsearch/?context=blended&query={username}"

    request = urllib.request.Request(host, headers=HEADERS)
    response = urllib.request.urlopen(request)

    result_string = gzip.decompress(response.read())

    result = json.loads(result_string.decode())

    pk = result.get('users')[0].get('user').get('pk')

    return pk


f = open("usernames.json")
cast = json.load(f)
f.close()

usernames = [n  for k,v in cast.items() for n in v.values()]

f = open("data/username_ids.txt", "a+")
for user in usernames:
    try:
        user_pk = get_user_id(user)
        print(f"got user: {user}, {user_pk}")
        f.write(f'"{user}": "{user_pk}",\n')
    except Exception:
        print(f"Could not query user: {user}")

    time.sleep(5)
    
    

f.close()