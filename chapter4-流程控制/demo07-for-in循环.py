'''
for-in 专门用于遍历范围、列表、元素和字典等可迭代对象所包含的元素
for 变量 in 字符串|范围|集合等：
    stmts
'''

## 循环范围
s_max = input('请输入您想计算的阶乘：')
mx = int(s_max)
result = 1
for num in range(1, mx + 1):
    result *= num
print(result)

## 循环元组
a_tuple = ('halo', 'hey', 'hello')
for ele in a_tuple:
    print('当前元素为：', ele)

## 循环列表
src_list = [12, 45, 34.3, 13, 'ee', 24, 56, 74, 109]
for ele in src_list:
    if isinstance(ele, int) or isinstance(ele, float):
        print(ele)

print('-----------')

## 通过索引遍历
b_list = [12, 45, 34.3, 13, 'ee', 24, 56, 74, 109]
for i in range(0, len(b_list)):
    print(b_list[i])