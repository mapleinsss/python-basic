# 元组支持的操作，列表基本都支持。对于不需要修改所包含的元素，使用元组代替列表更加安全


## 将元组转换成列表
a_tuple = (1, 2, 3)
a_list = list(a_tuple)
print(type(a_list))  # <class 'list'>

## 使用 range 函数来创建区间(range)对象
a_range = range(1, 5)
print(a_range)  # range(1, 5)
## 将区间转换为列表
print(list(a_range))  # [1, 2, 3, 4]
## 创建区间同时指定步长
print(list(range(4, 20, 2)))  # [4, 6, 8, 10, 12, 14, 16, 18]

## 将列表转换成元组
a_list = [1, 2, 3]
a_tuple = tuple(a_list)
print(type(a_tuple))  # <class 'tuple'>

## 通过区间创建元组
print(tuple(range(1, 5))) # (1, 2, 3, 4)
## 指定步长
print(tuple(range(1, 5, 2))) # (1, 3)
