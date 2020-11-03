"""
count():   统计元素出现的次数
index():   判断某个元素在列表出现的位置，如果未找到，会抛出 ValueError: 9 is not in list
pop():     实现元素出栈，如果对空列表执行，会抛出 IndexError: pop from empty list
reverse(): 列表中的元素反向存储
sort():    排序
"""

## count
a_list = [2, 2, 2, 2, [3, 9]]
## 统计 2 出现的次数
print(a_list.count(2))  # 4
## 统计列表中 列表[3,9] 出现的次数
print(a_list.count([3, 9]))  # 1

## index
b_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]
## 如果没有出现则会抛出 ValueError
# print(b_list.index(9)) # ValueError: 9 is not in list
## 从索引2开始，元素 5 出现的位置
print(b_list.index(5, 2))  # 4
## 在索引 2~4 定位 3 出现的位置
print(b_list.index(3, 2, 4))  # 2

## 栈操作 后进先出 pop() + append()
stack = []
## 向栈中入栈 3 给元素
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)  # [1, 2, 3]
# 出栈
print(stack.pop())  # 返回出栈的值
print(stack)  # [3, 4]
# 执行多次出栈
stack.pop()
stack.pop()
# stack.pop() # IndexError: pop from empty list
print(stack)

## reverse()
c_list = list(range(1, 10))
c_list.reverse()
print(c_list) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

## sort() 执行排序
d_list = [3,2,1,341,323,12,31,21,2]
d_list.sort()
print(d_list) # [1, 2, 2, 3, 12, 21, 31, 323, 341]
## 通过 key 指定长度进行排序
e_list = ['hello','world','hi','hey']
e_list.sort(key=len)
print(e_list) # ['hi', 'hey', 'hello', 'world']
## 反向排序
d_list.sort(reverse=True)
print(d_list) # [341, 323, 31, 21, 12, 3, 2, 2, 1]