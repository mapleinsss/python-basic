## while 循环元组
a_tuple = ('a', 'b', 'c')
i = 0
while i < len(a_tuple):
    print(a_tuple[i])
    i += 1

src_list = [12, 45, 34, 13, 100, 24, 56, 74, 109]
a_list = []
b_list = []
c_list = []
while len(src_list) > 0:
    ele = src_list.pop()
    if ele % 3 == 0:
        a_list.append(ele)
    elif ele % 3 == 1:
        b_list.append(ele)
    else:
        c_list.append(ele)
print(a_list)
print(b_list)
print(c_list)
