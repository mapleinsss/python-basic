"""
python 中的定义的方法，默认都是实例方法
类很大程度上是一个命名空间

python 类可以调用实例方法，但是不会自动绑定 self 参数，所以需要显示传入
"""


# 定义全局空间的 foo 函数
def foo():
    print('全局 foo 方法')


# 定义全局空间 bar 变量
bar = 20


class Bird:
    # Bird 命名空间中的变量
    bar = 200

    # Bird 命名空间中的方法，虽然报错，但是可以执行
    def foo():
        print('Bird foo 方法')


foo()
print(bar)
Bird.foo()
print(Bird.bar)


# 如果添加了 self
class User:
    def walk(self):
        print(self, 'walking')


# walk() missing 1 required positional argument: 'self'
# User.walk()

# 通过初始化
User().walk()
# 通过传入对象
u = User()
User.walk(u)
