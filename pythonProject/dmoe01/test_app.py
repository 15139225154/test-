import json

import requests


res = requests.get("https://www.baidu.com/", verify=False)
print(res.text)