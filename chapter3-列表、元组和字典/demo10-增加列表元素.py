# append 可以增加 单个值、元组、列表
# extend 可以增加 序列的单个值
# insert 指定将元素插入列表哪个位置

## 追加单个元素
a_list = [1, 2, 3]
a_list.append(4)
print(a_list)  # [1, 2, 3, 4]

## 追加元组，当成一项添加进列表
b_list = [1, 2, 3]
b_tuple = (4, 5, 6)
b_list.append(b_tuple)
print(b_list)  # [1, 2, 3, (4, 5, 6)]

## 追加列表，当成一项添加进列表
c_list = [1, 2, 3]
c_list_2 = [4, 5, 6]
c_list.append(c_list_2) # [1, 2, 3, [4, 5, 6]]
print(c_list)

## 将序列的单个元素添加入列表
d_list = ['1', 30]
d_list.extend((-2, 3, 4))
print(d_list)  # ['1', 30, -2, 3, 4]

## 追加区间
d_list.extend(range(2, 5))
print(d_list)  # ['1', 30, -2, 3, 4, 2, 3, 4]

## 中间插入
e_list = list(range(1, 6))
e_list.insert(3, 'gan')
print(e_list)  # [1, 2, 3, 'gan', 4, 5]

## 插入元组，注意元组会被拆分成元素
f_list = list(range(1, 6))
f_list.insert(3, tuple('org'))
print(f_list)  # [1, 2, 3, ('o', 'r', 'g'), 4, 5]
