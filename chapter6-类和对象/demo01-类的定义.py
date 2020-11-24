"""
class 类名：
    执行语句...
    零到多个变量...
    零到多个方法...

类名：一个或多个单词组成，每个单词首字母大写，不要使用分隔符

python 是动态语言，类所包含的变量可以动态增加或删除

类中定义的方法默认是实例方法，实例方法第一个参数会绑定到方法的调用者--
因此实例方法应该定义一个参数 self，约定名

实例化时 例如 p1 = Person() ：
1. 调用 __new__，申请内存空间
2. 调用 __init__ ，方法传入参数，将 self 指向内存空间
3. 变量 s1 也指向创建好的内存空间
"""


# 定义一个空类
class Empty:
    pass


# 定义一个 Person 类
class Person:
    # 类变量
    hair = 'black'

    # 在 init 方法中定义属性
    def __init__(self, name='Charlie', age=8):
        # 增加实例变量
        self.name = name
        self.age = age

    # 定义方法
    def say(self, content):
        print(self.name + ',' + content)


# 会自动调用 init 方法
p1 = Person()
print(p1.name)
print(p1.age)
p1.say('let\'s go')