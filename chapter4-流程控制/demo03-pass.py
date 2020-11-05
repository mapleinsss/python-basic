'''
pass 占位符，用来当空语句
'''

s = input('请输入一个整数：')
s = int(s)

if s > 5:
    print('大于5')
elif s < 5:
    # 占位符
    pass
else:
    print('等于5')
