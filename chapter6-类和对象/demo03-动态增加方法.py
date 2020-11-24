"""
python 为对象增加方法时，不会自动将调用者自动绑定到第一个参数，需要手动赋值

还可以通过 MethodType ，则可以自动绑定调用者为第一个值

"""


class Person:
    pass


def info(self):
    print('info函数：', self)


p = Person()

# 给 p 实例添加方法
p.foo = info

# 调用时，需要手动传递对象
p.foo(p)

# 通过 lambda 添加方法
p.bar = lambda self: print('lambda:', self)

# 调用时，需要手动传递对象
p.bar(p)


# 定义一个函数
def gg(self, msg):
    print('哈哈哈,', msg)


# 引入 MethodType
from types import MethodType

p.intro = MethodType(gg, p)

p.intro('沙雕')
