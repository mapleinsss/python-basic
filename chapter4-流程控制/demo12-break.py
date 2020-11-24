for i in range(10):
    print(i)
    # 当 i 的值为 2 时，结束循环
    if i == 2:
        break

exit_flag = False
for i in range(5):
    for j in range(3):
        print('i的值为 %d,j的值为 %d' % (i, j))
        if j == 1:
            exit_flag = True
            break
    if exit_flag:
        break

