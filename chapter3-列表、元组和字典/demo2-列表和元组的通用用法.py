# 只要不涉及改变元素的操作，列表和元组的用法是通用的

# 通过索引使用元素
my_tuple = (0, "1", 2.2, 3, 4, 5)
## 访问第一个元素
print(my_tuple[0])
## 访问倒数第一个元素
print(my_tuple[-1])

# ----------------------------------------

# 子序列
# 通过 slice 切片数组 [start: end: step]

my_list = [0, "1", 2.2, 3, 4, 5]
# 获取第二个到第四个（不包含）的元素
print(my_list[1: 3])  # ['1', 2.2]
# 获取倒数第三个到第一个（不包含）的元素
print(my_list[-3: -1])  # [3, 4]
# 获取第二个到倒数第二个（不包含）的元素
print(my_list[1: -2])  # ['1', 2.2, 3]
# 获取第一个到第五个（不包含），步长为 2
print(my_list[1: 5: 2])  # ['1', 3]
# 步长为 -1 反转列表
print(my_list[:: -1])  # [5, 4, 3, 2.2, '1', 0]
