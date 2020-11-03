# 列表和元组只支持加法运算，和为两个所包含元素的总和
# 注意：列表只能和列表相加，元组只能和元组相加

a_tuple = (1, 2, 3)
b_tuple = (4, 5)
## 执行相加
sum_tuple = a_tuple + b_tuple
print(sum_tuple)
## 直接加未定义
print(sum_tuple + (6, 7))
# 相加后，原来的值未发生改变
print(sum_tuple)
## 元组 + 列表报错
# print(sum_tuple + [3])

a_list = [1, 2, 3]
b_list = [4, 5]
# 列表相加
sum_list = a_list + b_list
print(sum_list)
print(sum_list + [6])
# 相加后，原来的值未发生改变
print(sum_list)
