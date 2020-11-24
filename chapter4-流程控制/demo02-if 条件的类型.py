'''
以下都会被当为 False 处理
False、None、0、""、()、[]、{}

在使用 if else 时，一定要先处理包含范围更小的情形
'''

# 由于范围问题，想展示老年人，却变成了青年人
age = 66
if age > 20:
    print('青年人')
elif age > 40:
    print('中年人')
elif age > 60:
    print('老年人')
