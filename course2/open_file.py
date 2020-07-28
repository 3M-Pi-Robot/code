# open a file json file

import json

with open("data.json") as data:
    text = data.read()
    # print(text)
    data = json.loads(text)
    print(data[0])
   
