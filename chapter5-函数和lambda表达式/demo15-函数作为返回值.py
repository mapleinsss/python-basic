# 使用函数作为返回值
def get_math_func(t):
    def square(n):
        return n * n

    def cube(n):
        return n * n * n

    def factorial(n):
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result

    if t == 'square':
        return square
    if t == 'cube':
        return cube
    else:
        return factorial


math_func = get_math_func('cube')
print(math_func(3))
