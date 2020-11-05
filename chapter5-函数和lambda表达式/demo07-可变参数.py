"""
可变参数
"""


# 可变参数示例
def mutable_params(one_param, *params):
    # 可变参数被定义为元组
    print(params)
    for param in params:
        print(param)
    print(one_param)


mutable_params('1', 1, 2, 3, 4)


# 可变参数在前，后面的参数需要用关键字指定
def mutable_params2(*params, one_param):
    for ele in params:
        print(ele)
    print(one_param)


mutable_params2(1, 2, 3, 4, 5, one_param=6)


# 普通参数+可变参数(收集为元组)+关键字参数(收集为字典)
def mutable_params3(x, y=3, *params_one, **params_two):
    print(x)
    print(y)
    for ele in params_one:
        print(ele)
    for ele in params_two:
        print(ele)
    print(params_one)
    print(params_two)


mutable_params3(1, 2, "world", "hello", k=12, v=13)
