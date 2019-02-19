import json

with open('./hoge.json', 'r') as f:
    data = json.load(f)

cnt = 10
for x in data['a']:
    x['start'] = cnt
    x['end'] = cnt + 3
    cnt += 3
    print(x)
