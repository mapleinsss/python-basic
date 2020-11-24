for i in range(3):
    print(i)
    if i == 1:
        continue
    # 在 i 的值为 1 时，该语句不输出
    print('continue 后的输出语句')