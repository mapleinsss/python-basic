"""
python 支持定义类方法和静态方法
区别：python 会自动绑定类方法的第一个参数
    类方法：第一个参数，约定为 cls 会自动绑定到类本身
    静态方法不会自动绑定

@classmethod 修饰的方法是类方法
@staticmethod 修饰是静态方法

实例也可以调用上述两种方法

一般不需要使用类方法或静态方法，完全可以使用函数来代替类方法或静态方法
特殊场景下（工厂模式） 使用
"""


class Bird:
    @classmethod
    def fly(cls):
        print('类方法：', cls)

    @staticmethod
    def info(p):
        print('静态方法：', p)


# 调用类方法，Bird 会自动绑定第一个参数
Bird.fly()
# 调用静态方法，不会自动绑定，需要手传
Bird.info('我是静态的呢')
