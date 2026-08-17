# list = [1, 2, 3]

# tuple = (1, 'iki', 3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))

list = ['Ali', 'Veli']
tuple = ('Damla', 'Ayşe')

list[0:2] = ['Ahmet', 'Mehmet']
# tuple[0] = 'Deniz'  # This would raise an error since tuples are immutable

tuple = ('Deniz', 'Ayşe')  # This is valid since we are creating a new tuple


print(list)
print(tuple)