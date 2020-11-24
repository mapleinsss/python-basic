my_list = [1, 2, 1, 4, 1]

# 判断 5 是否在列表中
print(5 in my_list)  # False
# 判断 5 是否不在列表中
print(5 not in my_list)  # True

# 列表的遍历
for val in my_list:
    if val == 5:
        print('yes 1')
