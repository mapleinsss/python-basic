"""
默认情况下，局部函数对外部是隐藏的，只能在函数内有效
其封闭函数也可以返回局部函数
"""


def get_math_func(tp, nn):
    def square(n):
        return n * n

    def cube(n):
        return n * n * n

    def factorial(n):
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result

    if tp == 'square':
        return square(nn)
    if tp == 'cube':
        return cube(nn)
    else:
        return factorial(nn)


print(get_math_func('square', 3))
print(get_math_func('cube', 3))
print(get_math_func('', 3))


# 演示局部函数的变量遮蔽，无法修改父级函数的值
def foo():
    name = 'Charlie'

    def bar():
        # print(name)  # 报错，因为局部变量遮蔽
        name = 'Brown'
        print(name)

    bar()
    print(name)


foo()


# 通过 nonlocal 访问父级函数的局部变量，修改值
def t():
    name = 'Charlie'

    def b():
        nonlocal name
        print(name)
        name = 'Brown'

    b()
    print(name)


t()
