'''
说明文档-把一串字符串放在函数声明之后，函数体之前
'''


def get_max(x, y):
    '''
    获取两个数值之间比较大的函数
    返回 x, y 两个参数较大的那个数
    '''
    return x if x > y else y

## 使用 help 查看帮助
help(get_max)
## 调用函数访问说明文档
print(get_max.__doc__)