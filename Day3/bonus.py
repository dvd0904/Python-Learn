import requests
import json
from time import sleep


speeds = ['-3', '-2.5', '-2', '-1.5', '1', '-0.5', '', '1', '1.5', '2', '2.5', '3']
humans =['thuminh', 'leminh', 'banmai']
url = 'https://api.fpt.ai/hmi/tts/v5'
folder = 'D:/Workspace/TKDTTT/konichiwa'

payload = 'mở rèm'
label = 'mo-rem'
headers = {
    'api-key': 'oaD7dDgbLnqptzwgMFFfaocPomiKjzjM',
    'speed': '',
    'voice': 'thuminh',
    'format': 'wav'
}

# oaD7dDgbLnqptzwgMFFfaocPomiKjzjM
json_arr = []
for human in humans:
    headers['voice'] = human
    for ele in speeds:
        headers['speed'] = ele
        response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)
        json_data = json.loads(response.text)
        json_arr.append(json_data)
        sleep(2)


for data in json_arr:
    url = data['async']
    fileName = url.rsplit('/', 1)[1]
    fileNameSaved = "{label}.{fileName}".format(label=label, fileName=fileName)
    print(fileNameSaved)
    ret = requests.get(url, stream=True)
    with open(folder + '/' + fileNameSaved, 'wb') as f:
        f.write(ret.content)
