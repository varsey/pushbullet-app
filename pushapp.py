from pushbullet import Pushbullet
import os
import requests
from datetime import datetime


KEY = os.environ['PUSHBULLET_API_KEY']
URL = 'https://api.pushbullet.com/v2/pushes'
HEAD = {'Access-Token': KEY}

response = requests.get(URL, headers=HEAD)
json_thing = response.json
header_stuff = response.headers

ratelimit_left = header_stuff['X-Ratelimit-Remaining']
ratelimit_limit = header_stuff['X-Ratelimit-Limit']
unix_time_left = int(header_stuff['X-Ratelimit-Reset'])

print( '', ratelimit_left, ' <- ', ratelimit_limit, '\n',  datetime.fromtimestamp(unix_time_left), end='\n\n' )

pb = Pushbullet(str(KEY))
pushes = pb.get_pushes(limit=1)

for push in pushes:
    print(push, '\n')
    #print(push['url'], '\n')
#print(pb.devices)



