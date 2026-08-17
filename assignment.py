# # x = 5
# # y = 10
# # z = 20

# x, y, z = 5, 10, 20

# # x, y = y, x 
# x += 5 # x = x + 5
# x -= 5 # x = x - 5
# x *= 5 # x = x * 5
# x /= 5 # x = x / 5
# x %= 5 # x = x % 5

# print(x, y, z)

values = 1, 2, 3, 4, 5, 6, 7, 8, 9

print(values)
print(type(values))

x, y, z, *t, w = values

print(values)
print(x, y, z, t, w)
