# key - value

# 41 - Kocaeli
# 34 - Istanbul

# sehirler = ['Kocaeli', 'Istanbul']
# plakalar = [41, 34]

# print(plakalar[sehirler.index('Kocaeli')])

# plakalar = {'Kocaeli' : 41, 'Istanbul' : 34}
# print(plakalar['Kocaeli'])

# plakalar['Ankara'] = 6
# print(plakalar)
# plakalar['Kocaeli'] = 'new value'
# print(plakalar)

users = {
    'sadikturan' : {
        
        'age' : 36,
        'email' : 'sadikturan@gmail.com',
        'address' : 'İstanbul',
        'phone' : '1234567890'
    },
    'cinarturan' : {
        'age' : 2,
        'roles' : ['admin', 'user'],
        'email' : 'cinarturan@gmail.com',
        'address' : 'Kocaeli',
        'phone' : '0987654321'
    }
}

print(users['sadikturan'])
print(users['cinarturan'])
