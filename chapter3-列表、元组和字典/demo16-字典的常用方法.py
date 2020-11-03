'''
clear：清空列表
get：获取值，获取不到不会报错
update 相当于 mysql replace
items、keys、values：获取三种对象，转列表
pop： 弹出指定key，返回value，并删除；如果 key 不存在则报错
popitem： 随机弹出：底层总是弹出底层存储的最后一个 kv 对，弹出的是一个元组，可以接收
setdefault()：根据 k 获取 v，如果不存在，设置默认 v，然后返回设置的默认 v
fromkeys()：给定多个 key 创建字典，这些 key 对应的值为 None，也可以额外传一个参数作为默认 v
'''

## clear 清空字典
scores = {'语文': 100, '数学': 80, '英语': 0}
scores.clear()
print(scores)

## get 与 [] 获取的区别， [] 获取不到，会发生 KeyError，get 则返回 None
a_scores = {'语文': 100, '数学': 80, '英语': 0}
print(a_scores.get('化学'))  # None
# print(a_scores['化学'])  # KeyError: '化学'

## update 相当于 mysql 的 replace，相同 key 覆盖，没有则新增
b_scores = {'语文': 100, '数学': 80, '英语': 0}
b_scores.update({'化学': 100, '英语': 99})
print(b_scores)

c_scores = {'语文': 100, '数学': 80, '英语': 0}
## 将字典转换为 dict_items 对象
ims = c_scores.items()
print(type(ims))  # <class 'dict_items'>
## 将 dict_items 转换为列表
print(list(ims))  # [('语文', 100), ('数学', 80), ('英语', 0)]

## 将字典转换为 dict_keys 对象
kys = c_scores.keys()
print(type(kys))  # <class 'dict_keys'>
## 将 dict_keys 转换为列表
print(list(kys))  # ['语文', '数学', '英语']

## 将字典转换为 dict_values 对象
vls = c_scores.values()
print(type(vls))  # <class 'dict_values'>
## 将 dict_values 转换为列表
print(list(vls))  # [100, 80, 0]

## pop 删除指定 kv，并返回 value，如果不存在，则抛出 KeyError: '化学'
d_scores = {'语文': 100, '数学': 80, '英语': 0}
print(d_scores.pop('语文'))  # 100

## popitem 随机弹出字典一对 kv
e_scores = {'语文': 100, '数学': 80, '英语': 0}
k, v = e_scores.popitem()
print(k, v)  # 英语 0

## setdefault()
f_scores = {'语文': 100, '数学': 80, '英语': 0}
f_scores.setdefault('化学', 10)
print(f_scores) # {'语文': 100, '数学': 80, '英语': 0, '化学': 10}

## fromkeys()
g_scores = dict.fromkeys(['a','b'])
print(g_scores) # {'a': None, 'b': None}
h_scores = dict.fromkeys(('a','b'))
print(h_scores) # {'a': None, 'b': None}
## 指定默认值
i_scores = dict.fromkeys(['a','b'],'default')
print(i_scores) # {'a': 'default', 'b': 'default'}