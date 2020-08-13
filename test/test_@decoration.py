"""
    带参装饰器
    带有不定参数的装饰器
    多个装饰器
"""

import time

def deco1(function):
    print("test test")  # reminder: always show firstly
    def wrapper(*args, **kwargs):
        print("this is deco1")
        startTime = time.time()
        function(*args, **kwargs)
        endTime = time.time()
        mSecs = (endTime - startTime)
        print("time is %d s" % mSecs)
        print("this the end of deco1")
        print("---------------------")
    return wrapper

def deco2(function):
    def wrapper(*args, **kwargs):
        print("this is deco2")
        function(*args, **kwargs)
        print("this the end of deco2")
        print("---------------------")
    return wrapper


@deco1
@deco2
def printInfo(a, b):
    print("hello, here is a function for add:")
    time.sleep(1)
    print('a+b: %d' % (a+b))

@deco1
@deco2
def printInfo2(a, b, c):
    print("hello, here is a function for add:")
    time.sleep(2)
    print('a+b+c: %d' % (a+b+c))


# args 传无参数名字的 变量值，kwargs传指定参数名的值（即：键值对）
# 或者这样理解：args表示任意多个无名参数，返回一个tuple；kwargs表示关键字参数，返回一个dict。
# func(list1, 1, 2, 3, id='1', name='mingcan')
def func(*args, **kwargs):
    for arg in args:
        print(arg)
        print("aaa")
    for key in kwargs:
        print('the key: %s is %s' % (key, kwargs[key]))


if __name__ == '__main__':
    printInfo(1, 2)
    print("##############")
    printInfo2(1, 2, 3)


'''
    list1 = [1,2,3,4,5]
    dict1 = {'a':1, 'b':2}
    func(list1, 1, 2, 3, id='1', name='mingcan')

    # 自带的dict创建字典
    dict2 = dict(e=3, a=2, b=4)
    print(dict2)
'''