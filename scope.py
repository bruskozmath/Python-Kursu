#Global Scope
x = 'global x'

def function():
    #Local Scope
    x = 'local x'
    print(x)

function()
print(x)

#####################################

name = 'Çınar'

def changeName(new_name):
    name = new_name
    print(name)

changeName('Ada')
print(name)

#####################################

name = 'Global string'

def greeting():
    # name = 'Çınar'

    def hello():
        # name = 'Ada'
        print('Hello ' + name)
    hello()

greeting()

######################################

x = 50
def test():
    global x
    print(f'X: {x}')

    x = 100
    print(f'Changed x to: {x}')

test()
print(x)