'''
断言如果为 True 继续执行，否则抛出 AssertionError
其实等于
if 条件为 False:
    抛出 AssertionError 错误
'''
s_age = input('请输入年龄：')
age = int(s_age)

assert 20 < age < 80
print('年龄在20到80之间') # 输入不在区间的数， AssertionError assert 20 < age < 80