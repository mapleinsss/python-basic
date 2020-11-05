scores = {'语文': 100, '数学': 80, '英语': 0}

## 通过 items 遍历
for k,v in scores.items():
    print('key:',k)
    print('value:',v)

print('----------')

for k in scores.keys():
    print('key:',k)

print('----------')

for v in scores.values():
    print('value:',v)