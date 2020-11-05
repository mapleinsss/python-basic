# 函数的形参为函数
def test(d, fn):
    result = []
    for e in d:
        result.append(fn(e))
    return result


def square(n):
    return n * n


data = [1, 2, 3, 4, 5]
print(test(data, square))
