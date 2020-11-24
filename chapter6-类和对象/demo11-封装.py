class User:
    def __hide(self):
        print('演示封装的 hide 方法')

    def getname(self):
        return self.__name

    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度在3~8个字符')
        self.__name = name

    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError('年龄必须在在18~70岁之间')
        self.__age = age

    def getage(self):
        return self.__age

    age = property(getage, setage)


u = User()
u.setage(19)
u.age = 22
print(u.age)
