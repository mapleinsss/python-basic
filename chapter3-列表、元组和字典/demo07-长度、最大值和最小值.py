# len()、max()、min() 全局函数

a_tuple = (1, 2, 3, 4, 5)
print(max(a_tuple)) # 5
print(min(a_tuple)) # 1
print(len(a_tuple)) # 5

# 字符串比大小，依次比较 ASCII 值，第一次比较出来，就取最大
b_tuple = ('a', 'b', 'c', 'd', 'e')
print(max(b_tuple))
print(min(b_tuple))
print(len(b_tuple))