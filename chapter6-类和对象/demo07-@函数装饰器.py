"""
前面描述的 @staticmethod 和 @classmethod 都是函数装饰器

使用函数装饰器，被 @函数 修饰的函数会被替换成新的东西

@ 符号修饰函数，可以在被修改的函数前后添加处理逻辑，类似 AOP
"""


def funA(fn):
    print('A')
    fn()
    return 'hello A'


@funA
def funB():
    print('B')


print(funB)

"""
A
B
hello A

可以看到函数 b 只是被调用过，自身未执行
"""

print('-------------------------')


# 展示一个更复杂的函数装饰器
def foo(fn):
    # 定义一个嵌套函数
    def bar(*args):
        print("args:", args)
        n = args[0]
        print(n)
        # 查看传给 foo 函数的 fn 函数
        print(fn.__name__)
        fn(n * (n - 1))
        return fn(n * (n - 1))

    return bar


@foo
def test(a):
    print('test 被调用了')


test(10)

print('-------------------------')


# 模拟权限检查
def auth(fn):
    def auth_fn(*args):
        print('正在执行权限检查')
        # 回调被修饰的目标函数
        fn(*args)
        print('记录日志')

    return auth_fn


@auth
def test(a, b):
    print('执行 test 函数，参数 a: %s,参数 b: %s' % (a, b))


test(10, 20)
