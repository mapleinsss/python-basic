"""
self
> 在构造方法引用该构造方法正在初始化的对象
> 在普通实例方法中引用调用该方法的对象

构造方法和实例方法第一个 self 参数会自动绑定，所以不需要为第一个参数传递值

self 族弟啊作用就是引用当前方法的调用者，比如
    1. 在构造方法中，通过 self 为该对象添加实例变量
    2. 在实例方法中访问该类的另一个实例方法或变量
"""


class Dog:

    def jump(self):
        print('i\'m Jumping')

    def run(self):
        self.jump()
        print('I\'m Running')


d = Dog()
d.run()
