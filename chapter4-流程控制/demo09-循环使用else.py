# 使用 else
count_i = 0
while count_i < 5:
    print('count_i 小于5：', count_i)
    count_i += 1
else:
    print('count_i 大于或等于5：', count_i)

#
a_list = [1, 2, 3, 4, 5]
for ele in a_list:
    print('元素：', ele)
else:
    # 编译器报错，但是依然会打出最后一个值
    print('else 块', ele)
