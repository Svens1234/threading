from time import time, sleep


def one(num):
    sleep(num)


def two(num):
    sleep(num)


x1=time()

one(1)
two(1)


x2=time()


x3=x2-x1

print(x3)
