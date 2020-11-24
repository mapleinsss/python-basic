"""
python 定义了 getter/setter 方法，可以用 property() 函数将他们定义为属性（相当于实例变量）

property(fget=None,fset=None,fdel=None,doc=None)

0参数：不能读写、删除
1参数：只读
2参数：读写
3参数：读写、删除
4参数：读写删，文档说明
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def setsize(self, size):
        self.width, self.height = size

    def getsize(self):
        return self.width, self.height

    def delsize(self):
        self.width, self.height = 0, 0

    # 使用 property 定义属性
    size = property(getsize, setsize, delsize, '用于描述矩形大小的属性')


# 访问 size 属性的说明文档
print(Rectangle.size.__doc__)
# 通过内置的 help() 函数查看 size 的说明文档
help(Rectangle.size)

rect = Rectangle(4, 3)
# 访问 size 属性
print(rect.size)
# 设置 size 属性
rect.size = 5, 10
# 访问两个变量
print(rect.width)
print(rect.height)
# 删除 size 属性
del rect.size
# 访问实例变量
print(rect.width)
print(rect.height)
