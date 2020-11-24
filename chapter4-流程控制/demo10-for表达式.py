a_range = range(10)
# 对 a_range 执行 for 表达式
a_list = [x * x for x in a_range]
print(a_list)

c_generator = (x * x for x in range(10))
print(type(c_generator))  # <class 'generator'>
for i in c_generator:
    print(i)

d_list = [(x, y) for x in range(2) for y in range(3)]
print(d_list)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

dd_list = []
for x in range(2):
    for y in range(3):
        dd_list.append((x, y))
print(dd_list) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]