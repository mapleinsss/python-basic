

scores = {'语文': 100, '数学': 80, '英语': 0}
## 通过 key 访问 value
print(scores['语文'])

## 新增
scores['化学'] = 99
print(scores)

## 删除
del scores['化学']
print(scores)

## 修改
scores['英语'] = 29
print(scores)

## 判断是否包含，基于 key 判断
print('语文' in scores)
print('化学' not in scores)
