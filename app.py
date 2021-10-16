from threading import *
from time import time, sleep


def one(num):
    sleep(num)


def two(num):
    sleep(num)


t1=Thread(target=one, args=(1,))
t2=Thread(target=two, args=(1,))


x1=time()

t1.start()
t2.start()





x2=time()


x3=x2-x1

print(x3)