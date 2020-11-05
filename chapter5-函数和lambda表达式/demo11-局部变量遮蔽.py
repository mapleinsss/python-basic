"""
如果函数中定义了与全局变量同名的变量，此时就会发生局部变量遮蔽全局变量
"""

name = 'Charlie'


def test():
    # 可以访问全局变量的值
    print(name)
    # 对全局变量进行赋值：Shadows name 'name' from outer scope
    # name = 'Brown'


test()


def test2():
    # 访问被遮蔽的全局变量
    print(globals()['name'])  # Charlie
    # 新增局部变量 name
    name = 'Brown'
    print(name)  # Brown


test2()
print(name)


# 在函数内声明全局变量，并修改它的值
def test():
    global name
    print(name)
    name = 'hello'


test()
print(name)
