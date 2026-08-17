def changeName(n):
    n = 'Ada'

name = 'Yiğit'
changeName(name)
print(name)

def change(n):
    n[0] = 'İstanbul'

sehirler = ['Ankara', 'İzmir']
n = sehirler[:]

n[0] = 'İstanbul' 

print(sehirler)
print(n)

def add(*params):
    sum = 0
    for n in params:
        sum += n
    return sum

print(add(2,3))
print(add(2,3,4))
print(add(2,3,4,5,6,7,8,9,10))

def displayUser(**args):
    for key, value in args.items():
        print(f"{key} : {value}")

displayUser(name='Yiğit', age=2, city='İstanbul')
displayUser(name='Ada', age=12, city='İstanbul', phone='1234567890')
displayUser(name='Yiğit', age=14, city='İstanbul', phone='1234567890', email = 'yigit@gmail.com')


def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, key1='value1', key2='value2')