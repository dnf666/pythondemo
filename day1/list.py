#coding:utf-8
# L = ['Adam', 95.5, 'Lisa', 85, 'Bart', 59]
# print(L[:3])
# print( L)
#
# # 按照索引查找
# print(L[0])
# print( L[1])
# # 倒序查找 -1)表示倒数第一个 -2表示倒数第二个
# print( L[-1])
# print( L[-2])
# # 数组扩展和指定位置添加
# L = ['Adam', 'Lisa', 'Bart']
# L.append("lalala")
# L.insert(2,"Paul")
# print( L)

#删除数组元素 1.用del关键字 2. 用pop()方法
L = ['Adam', 'Lisa', 'Paul', 'Bart']
del L[2]
# L.pop()# 删除最后一个
# L.pop(2)# 删除索引为2的元素
print( L)