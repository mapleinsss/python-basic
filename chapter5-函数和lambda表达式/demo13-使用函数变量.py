"""
python 函数是 一等公民
    函数本身也是一种对象，既可以用于赋值，
                                        也可以作为其他函数的参数
                                        还可以作为其他函数的返回值
"""


# 使用函数变量
# 定义一个计算乘方的函数
def pow(base, exponent):
    result = 1
    for i in range(1, exponent + 1):
        result *= base
    return result

# pow 函数赋值给 my_fun 函数
my_fun = pow
print(my_fun(3, 3))

