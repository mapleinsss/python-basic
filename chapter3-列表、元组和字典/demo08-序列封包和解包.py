# 程序把多个值赋予变量时，python 会自动将多个值封装成元组，即序列封包
# 程序允许序列直接赋值给多个变量，此时序列的各元素依次赋值给每个变量（要求元素个数和变量个数相等），即序列解包

# 序列封包
vals = 10, 20, 30
print(vals)
print(type(vals))  # <class 'tuple'>
print(vals[1])

# 序列解包
a_tuple = tuple(range(1, 10, 2))
print(a_tuple)
a, b, c, d, e = a_tuple
print(a, b, c, d, e)  # 1 3 5 7 9

x, y, z = 10, 20, 30
print(x)  # 10

# 使用 *
first, second, *rest = range(10)
print(rest) # [2, 3, 4, 5, 6, 7, 8, 9]


*begin, last = range(10)
print(begin) # [0, 1, 2, 3, 4, 5, 6, 7, 8]

