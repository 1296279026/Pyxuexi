# import requests
# import DiEr
#
# text = requests.get('http://wallhaven.cc')
# print(text.content)
# 打印文档
# print(help(open))

#################################################################
# 读文件
# 同一文件夹下直接的打开文件名就行
# file=open('ehe.txt',encoding='UTF-8')
# text=file.read()
# print(text)
# #关闭文件夹
# file.close()
#################################################################
# 新版用下面这个不用关闭
# 读文件
# with open('P:\\ceshi.txt',encoding='UTF-8')as f:
#     print(f.read())
#################################################################
# 写文件
# with open('P:\\ceshi2.txt','w',encoding='UTF-8')as f:
#     f.write('这是测试测试')
# 写到同一个文件里面不覆盖
# with open('P:\\ceshi2.txt','a',encoding='UTF-8')as f:
#     f.write('这是测试测试\n')
#################################################################
# #复杂写法
# newList=[]
# for i in range(11):
#     newList.append(i*2)
# print(newList)
# #简约写法
# print([i*2 for i  in range(11)])
# 复杂写法
# list=['小明','小红','张三','李四']
# emptyList=[]
# for name in list:
#     if name.startswith('小'):
#         emptyList.append(name)
# print(emptyList)
# #简约写法
# print([name for name in list if name.startswith('小')])
# if __name__ == '__main__':
# run()
#所有的参数*args
# def add(*args,**kwargs):
#     print(sum(args))
#
#
# add(4, 7)
#字典
# def someone(**kwargs):
#     for k,v in kwargs.items():
#         print(k,':',v)
# someone(height=100,name='小花')

