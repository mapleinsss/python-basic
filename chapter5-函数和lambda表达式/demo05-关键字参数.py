def girth(width, height):
    print('width:', width)
    print('height:', height)
    return 2 * (width + height)


## 传统调用方式，根据位置传入参数
print(girth(3.5, 4.9))

## 通过关键字传入参数
print(girth(width=3.5, height=4.9))

## 在使用关键字的时候，可以交换位置
print(girth(height=4.9, width=3.5))

## 部分使用关键字，部分使用位置参数
print(girth(3.5, height=4.8))
# Positional argument after keyword argument
#print(girth(width=3.5, 4.8))
