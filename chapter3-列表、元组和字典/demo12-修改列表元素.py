# 修改列表元素：通过索引赋值修改
# 通过 slice 可以修改或者新增元素

a_list = list(range(1, 10))
## 修改第三个元素
a_list[3] = '被修改了呢'
print(a_list)
## 修改最后要给元素
a_list[-1] = '最后的元素也被修改了呢'
print(a_list)

b_list = list(range(1, 10))
## 修改一段值为 hahaha
b_list[1:3] = ['hahaha']
print(b_list)  # [1, 'hahaha', 4, 5, 6, 7, 8, 9]

## 根据步长修改
b_list[2:5:2] = ['q', 'w']
print(b_list) # [1, 'hahaha', 'q', 'c', 'w', 'c', 'd', 'd', 4, 5, 6, 7, 8, 9]


## 插入列表
b_list[2:2] = ['d', 'd']
print(b_list)  # [1, 'hahaha', 'd', 'd', 4, 5, 6, 7, 8, 9]

## 插入字符串
b_list[2:2] = 'accc'
print(b_list)  # [1, 'hahaha', 'a', 'c', 'c', 'c', 'd', 'd', 4, 5, 6, 7, 8, 9]

## 删除
b_list[1:8] = []
print(b_list)  # [1, 4, 5, 6, 7, 8, 9]
