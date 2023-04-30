import urllib.request
import gzip
import json
import time
from PRIVATE.headers import HEADERS

def get_following(pk):
    max_id = 0
    all_users = []
    while max_id is not None:
        host = f'https://www.instagram.com/api/v1/friendships/{pk}/following/?count=200&max_id={max_id}'

        headers = HEADERS

        request = urllib.request.Request(host, headers=headers)
        response = urllib.request.urlopen(request)

        result_string = gzip.decompress(response.read())

        result = json.loads(result_string.decode())
        users = [[u.get("pk"), u.get("username")] for u in result.get("users")]
        all_users.extend(users)

        max_id = result.get("next_max_id")
        print(max_id, len(users))

    return all_users

with open("data/username_ids.json") as f:
    userid = json.load(f)

file = open("data/following.json", "a+") 

for name, pk in userid.items():
    try:
        following = get_following(pk)
        file.write(json.dumps({name: following}))
        print(name, len(following))
        time.sleep(3)
    except Exception:
        print(f"Could not query for {name}")

file.close()