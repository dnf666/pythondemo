#coding:utf-8
print ("123","23324","123")
# print 可以用逗号拼接。逗号在输出中会变为空格
# end关键字用于使输出结果保持在一行
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b