# 定义一个 Person 类
class Person:
    # 类变量
    hair = 'black'

    # 在 init 方法中定义属性
    def __init__(self, name='Charlie', age=8):
        # 增加实例变量
        self.name = name
        self.age = age


# 查询
p1 = Person()
print(p1.name)
print(p1.age)

# 修改
p1.name = 'Brown'
print(p1.name)

# 新增属性
p1.height = 180
print(p1.height)

# 删除属性
del p1.name
print(p1.name)  # AttributeError: 'Person' object has no attribute 'name'
