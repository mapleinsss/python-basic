'''
如果函数返回多个值，既可以多个值包装成列表返回，也可以直接返回多个值
'''

def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        if isinstance(e, int) or isinstance(e, float):
            count += 1
            sum += e
    return sum, sum / count


my_list = [1, 2, 3.3, 'a', 4, 5, 6]

# 封装成元组进行输出
print(sum_and_avg(my_list))

# 通过序列化解包获取多个返回值
sum, avg = sum_and_avg(my_list)
print(sum)
print(avg)
