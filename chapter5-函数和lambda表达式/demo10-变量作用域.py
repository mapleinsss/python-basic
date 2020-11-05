"""
局部变量：函数中定义的变量，包括参数
全局变量：在函数外，全局范围定义的变量

所有的变量和值都存在一个看不见的字典，变量名为 key，值为 value
全局变量还包括 python 自身的一些全局变量

globals()：返回全局范围所有变量组成的字典
locals()：在函数外获取全局范围，在函数内获取函数体里的 变量组成的字典
var(object)：获取指定对象范围内变量组成的字典变量，如果不传递，vars() 和 locals() 用法一样

通过上面三个函数获取的变量，可以被修改，但不建议
通过 globals() 和 locals() 获取全局字典变量，可以被修改
通过 locals() 获取局部变量字典，修改了也不会影响局部变量
"""


# 测试局部
def test():
    age = 20
    # 直接访问局部变量
    print(age)
    # 通过 locals() 输出局部变量字典
    print(locals())
    # 访问局部变量的 age
    print(locals()['age'])
    # 改变局部变量 age 的值，修改失败
    locals()['age'] = 12
    # 再次访问 age 的值
    print(age)


test()

# 测试全局
x = 5
print(globals())
print(locals())
# 直接访问 x 的值
print(globals()['x'])
# 使用 globals 修改全局变量的值，成功
globals()['x'] = 50
print(locals()['x'])
# 使用 locals() 修改全局变量的值，成功
locals()['x'] = 500
print(x)