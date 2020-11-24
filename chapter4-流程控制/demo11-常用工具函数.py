a = ['a', 'b', 'c']
b = [1, 2, 3]

# 查看 zip() 函数的类型
print(type(zip(a, b)))  # <class 'zip'>

# 迭代 zip 类型
for v in zip(a, b):
    print(v)
    print(type(v))

a = range(10)
print(reversed(a))
print(type(reversed(a))) # <class 'range_iterator'>
a_list = [x for x in reversed(a)]
print(a_list)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(type(a))  # <class 'range'>

a = [20, 30, -1.2, 3.5, 88]
print(sorted(a)) # [-1.2, 3.5, 20, 30, 88]
print(type(sorted(a))) # <class 'list'>
