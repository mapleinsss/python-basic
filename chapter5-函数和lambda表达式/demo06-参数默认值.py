"""
使用 形参=值 实现默认值
"""


def say_hi(name='小弟弟', msg='赶紧滚'):
    print(name, '你好呀')
    print('给你的消息：', msg)


say_hi()

say_hi('臭弟弟')

say_hi('老弟', '滚啊')
