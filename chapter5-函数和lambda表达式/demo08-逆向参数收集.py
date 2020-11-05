"""
逆向参数收集：在程序已有列表、元组、字典等对象的前提下，把他们的元素拆开
                        后传给函数的参数
列表、元组参数前面添加 *
字典前面添加 **
"""


# 演示逆向收集 list
def test1(name, msg):
    print(name)
    print(msg)


my_list = ['唐大维', '你真肥']
test1(*my_list)


# 演示逆向收集 tuple
def test2(name, *nums):
    print('name: ', name)
    print('nums: ', nums)


# 传入 name + 元组
test_tuple = (1, 2, 3, 4, 5)
test2('唐大维', *test_tuple)
# 只传元组，被 name 接收
test2((1, 2, 3, 4, 5))


# 演示逆向收集 dict
def test3(book, price, desc):
    print(book)
    print(price)
    print(desc)


my_dict = {'book': 'Python 大神', 'price': 28, 'desc': '2828卡卡就发'}
test3(**my_dict)
