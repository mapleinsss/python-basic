"""
命名空间定义的变量就是类变量
不管是全局范围还是函数内访问类变量，都必须使用类名进行访问
当然也可以使用实例对象访问类变量

python 允许通过对象访问变量，如果通过实例对类变量赋值，此时
    不是对类变量赋值，而是定义新的实例变量(第一次访问)
"""


class Address:
    detail = '广州'

    def info(self):
        # 直接访问类变量，报错
        # print(detail)
        # 通过类访问类变量
        print(Address.detail)


print(Address.detail)

addr = Address()
addr.info()
# 修改类变量
Address.detail = '佛山'
print(Address.detail)


# 通过实例来访问类变量，不推荐
class Record:
    item = '鼠标'

    def info(self):
        print(self.item)


r = Record()
print(r.item)

print('------------------------')


# 对类变量赋值
class Inventory:
    item = '鼠标'
    quantity = 288

    def change(self, item, quantity):
        self.item = item
        self.quantity = quantity


iv = Inventory()
iv.change('显示器', 1666)
print(iv.item)
print(iv.quantity)
print(Inventory.item)
print(Inventory.quantity)

print('------------------------')

# 如果对类变量修改，此时实例变量的值也不会修改
Inventory.item = '耳机'
Inventory.quantity = '599'

print(iv.item)
print(iv.quantity)
print(Inventory.item)
print(Inventory.quantity)