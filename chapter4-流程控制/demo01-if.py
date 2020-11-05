'''
if 注意缩进，表达为下面三种形式

第一种
if expr:
    stmts

第二种
if expr:
    stmts
else:
    stmts

第三种
if expr:
    stmts
elif expr:
    stmts
... # 多条 elif
else:
    stmts
'''

s_age = input("请输入年龄：")
age = int(s_age)
if age > 20:
    print('老年人')
else:
    print('小崽子')