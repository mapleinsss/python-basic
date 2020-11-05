"""
对传入的参数使用 = 赋值是无效的，出了函数，传入的参数依然是原来的值
如果要通过函数修改某些数据，需要将数据包装成列表、字典来修改它们
"""


# 值传递（类似副本），参数传入后，不会改变传入的值
def swap(a, b):
    a, b = b, a
    print('函数内：', a, b)


p1 = 1
p2 = 2
swap(p1, p2)
print('函数外：', p1, p2)  # 1 2


# 对于对象内的值，会发生改变，对象指针不变
def swap2(dict_one):
    dict_one['a'], dict_one['b'] = dict_one['b'], dict_one['a']
    print(dict_one)
    print(id(dict_one))


di = {'a': 1, 'b': 2}
swap2(di)
# {'a': 2, 'b': 1}
print(di)
# 地址一致，对象里的值发生改变
print(id(di))
