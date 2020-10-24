# lang=['C','C++','C#','Java','Python']
# print(lang)
#
# print(len(lang))#打印数组的长度
#
# print(lang[3])#打印数组的第四个数据
#
# lang.append('Golang')#给数组里添加一个新元素
#
# print(lang)
#
# lang.remove('C++')#把数组里的C++删除
#
# print(lang)
#
# print(lang.count('C'))#数一下里面有几个“C”


# MyName=['cm','cmx','cjx']
# NowName=('cm','cmx','cjx')
# print(type(MyName))
# print(type(NowName))
# print(len(MyName))
# print(len(NowName))
# print(dir(MyName))
# print('--------------------------------------------')
# print(dir(NowName))


# age=int(input('请输入你的年龄'))
#
# if age>18:
#     print('你可以上网')
# elif age<18:
#     print('你不可以上网')
# else:
#     print('你18岁，可以上网！')


# for i in range(201):
#     if i>=20:
#         print(i)
# i=1
# while i<10:
#     print('hello world')
#     i += 1

# #定义一个方法求和
# def sum(num1,num2):
#     print(num1+num2)
#
# sum(488,454)
# 定义一个直接返回和的方法
# def sum2(a,b):
#     return (a+b)
#
# b=sum2(45,444)
# print(b)
#
#
# def JinZhi(R):
#     Z=R*1024
#     print(Z)
#
#
# JinZhi(10)
# class Animal():
#
#     def eat(self, name):
#         print(name + "可以吃")
#
#     def run(self, name):
#         print(name + "可以跑")
#
#
# ani = Animal()
# ani.eat('狗')
# ani.run('猫')

# class people:
#     def dance(self,name):
#         print(name+"可以跳舞")
#
#     @staticmethod
#     def sing():
#         print("可以唱歌")
#
# cm=people()
# cm.dance('chen ming')
# cm.sing()

# 初始化变量__init__学习
class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(self.name, "可以走路,他今年", self.age)


stu = Students(name='chenmingxing', age='18岁')
stu.run()
