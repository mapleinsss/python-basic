# 使用 {} 创建字典
# 元组可以作为列表的 key，但是列表不行，因为 dict 要求 key 必须是不可变类型
# 使用 dict() 函数来创建
# 使用关键字来创建

## 创建一个字典
scores = {'语文': 100, '数学': 80, '英语': 0}
print(scores)

## 创建一个空字典
empty_dict = {}
print(empty_dict)

## 使用元组作为 key
a_dict = {(20, 30): 'good', 30: 'bad'}
print(a_dict)

## 使用 dict() 函数来创建
vegetables = [('celery', 1.58), ('brocoli', 1.28), ('lettuce', 2.31)]
b_dict = dict(vegetables)
print(b_dict)  # {'celery': 1.58, 'brocoli': 1.28, 'lettuce': 2.31}

## 使用关键字来创建
c_dict = dict(a=1, b=2)
print(c_dict) # {'a': 1, 'b': 2}
