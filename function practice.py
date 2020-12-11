def greet():
    print("hello")
    print("good morning")


greet()
print("welcome")


def add(x, y):
    c = x + y
    return c


result = add(6, 7)
print(result)


def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


result1, result2 = add_sub(4, 8)
print(result1, result2)


def person(name, age=18):
    print(name)
    print(age)


person('abdulrahim', 20)
person(age=28, name='navin')


def sum(a, *b):
    c = a
    for i in b:
        c = c + i
    print(c)


sum(5, 6, 34, 78)


def sum(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)

sum(5, 6, 34, 78)

def person(name,*data):
    print(name)
    print(data)

person('habeeb', 22, 'ibadan', '07036599967')

def person(name,**data):
    print(name)
    print(data)

person('habeeb', age=22, city='ibadan', number='07036599967')

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('habeeb', age=22, city='ibadan', number='07036599967')

gee = 10
print(id(gee))
def something():
    gee = 20
    x = globals()['gee']
    print(id(x))
    print(x)
    print('in function',gee)
something()
print('outside',gee)

gee = 10
print(id(gee))
def something():
    global gee
    gee = 20
    print('in function',gee)
something()
print('outside',gee)

print("anonymous functions / lambda")
f = lambda a: a*a

print(f(5))

nums = (12,13,14,15,16,17,18,19,20,21,22,23,24)

evens = list(filter(lambda n: n % 2 == 0,nums))
print(evens)

doubles = list(map(lambda n: n*2,evens))
print(doubles)

from functools import reduce
addup = reduce(lambda a,b: a+b,doubles)
print(addup)

from factorial import fact

z = fact(4)
print(z)


