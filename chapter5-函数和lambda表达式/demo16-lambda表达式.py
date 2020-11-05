"""
lambda [parameter_list] : 表达式

> 对于单行函数，lambda 使代码更简洁
> 对于不需要多次复用的函数，使用 lambda 用完后立刻释放，提高了性能
"""


def get_math_func(t):
    result = 1
    if t == 'square':
        return lambda n: n * n
    if t == 'cube':
        return lambda n: n * n * n
    else:
        return lambda n: (1 + n) * n / 2


math_func = get_math_func('square')
print(math_func(3))
