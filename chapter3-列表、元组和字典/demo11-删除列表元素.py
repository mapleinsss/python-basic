# del    可以用于删除列表的元素，也可以用于删除变量
# remove 删除指定元素第一次找到的位置，如果找不到就报错
# pop 根据索引移出，找到到报错
# clear  清空列表所有元素

a_list = list(range(1, 10))
# 删除索引为 2 的元素
del a_list[2]
print(a_list)  # [1, 2, 4, 5, 6, 7, 8, 9]

# 删除第二个到第四个的元素
del a_list[2: 4]
print(a_list)  # [1, 2, 6, 7, 8, 9]

# 删除倒数第三个到第二个元素
del a_list[2:-2:2]
print(a_list)  # [1, 2, 7, 8, 9]

# 删除变量
name = 'tangjingjing'
print(name)
del name
# print(name) # NameError: name 'name' is not defined


b_list = [1, 2, 3]
# 删除第一次找到 3
b_list.remove(3)
print(b_list)
# b_list.remove(4)  # ValueError: list.remove(x): x not in list

c_list = list(range(1, 10))
# clear 清空元素
c_list.clear()
print(c_list)

d_list = list(range(1, 10))
# 移除索引为 1 的元素
d_list.pop(1)
print(d_list)  # [1, 3, 4, 5, 6, 7, 8, 9]
# 索引越界，报错
# d_list.pop(20) # IndexError: pop index out of range
# 不写索引，移除最后一个元素
d_list.pop()
print(d_list)  # [1, 3, 4, 5, 6, 7, 8]
