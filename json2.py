# Orjinal kodlar
# import json

# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''

# info = json.loads(data)
# print('User count:', len(info))

# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])
# ------------------------------------------------------------------------------------------

import json
import ssl
from urllib.request import urlopen

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print('Retrieving', url)
data = urlopen(url, context=ctx).read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
itemCount = 0
totalSum = 0
for item in info['comments']:
    # print('Name', item['name'])
    # print('Count', item['count'])
    totalSum += int(item['count'])
    itemCount += 1
    # print('Attribute', item['x'])
print('Count:', itemCount)
print('Sum:', totalSum)
