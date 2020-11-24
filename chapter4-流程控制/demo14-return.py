def test():
    for i in range(10):
        for j in range(10):
            print('i 的值为 %d，j 的值为 %d' % (i, j))
            # 当 j 的值为 1 时，整个方法结束
            if j == 1:
                return
            print('return 后的输出语句')

test()
