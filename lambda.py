def square(num): return num ** 3

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda num: num ** 2, numbers))

for item in map(square, numbers):
    print(item)

print(result)

square = lambda sayi: sayi ** 2
result = square(5)
print(result)

sayilar = [1, 2, 3, 4, 5, 10, 13]

def check_even(num): return num % 2 == 0

result = list(filter(check_even, sayilar))

print(result)

kontrol = lambda sayi: sayi % 2 == 0
result = list(filter(kontrol, sayilar))
print(result)