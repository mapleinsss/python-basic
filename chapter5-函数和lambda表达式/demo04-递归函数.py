## 一至一个数列 f(0)=1,f(1)=4,f(n+2)=2f(n+1)+f(n)
def fn(n):
    if n == 0:
        return 1
    if n == 1:
        return 4
    else:
        # 在函数体中调用它本身，就是函数递归
        return 2 * fn(n - 1) + fn(n - 2)


print(fn(10))
