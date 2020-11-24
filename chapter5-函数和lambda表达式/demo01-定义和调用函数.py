'''
def 函数名(形参列表):
     函数体
    [return [返回值]]

- 函数名：单词全部小写，单词与单词之间用下划线分隔
- 形参列表：用 , 隔开
'''


## 定义一个比大小函数
def get_max(x, y):
    return x if x > y else y

## 定义一个输出函数
def say_hello(name):
    return name + ',你好呀'


print(get_max(5, 6))
print(say_hello('猪猪'))
