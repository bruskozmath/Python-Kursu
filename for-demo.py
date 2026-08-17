sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayilar 3'ün katıdır?
for sayi in sayilar:
    if(sayi % 3 == 0):
        print(sayi)
print('*'*100)

# 2- Sayilar listesinde sayıların toplamı kaçtır?
toplam = 0
for sayi in sayilar:
    eskiToplam = toplam
    toplam += sayi
    print(f'Toplam sonucu {eskiToplam} olmuştu, {sayi} eklenince {toplam} oldu.')
print('*'*100)

# 3- Sayilar listesindeki tek sayıların karesini alınız.
for sayi in sayilar:
    if(sayi % 2 == 1):
        print(f'{sayi} tek sayıdır, karesi {sayi**2}')
    else:
        print(f'{sayi} tek değil.')
print('*'*100)

#************************************************************************************************************

sehirler = ['Kocaeli','İstanbul','Ankara','İzmir','Rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?
for sehir in sehirler:
    if(len(sehir) <= 5):
        print(sehir)
print('*'*100)

#************************************************************************************************************

urunler = [
    {'name': 'Samsung S6', 'price': '3000'},
    {'name': 'Samsung S7', 'price': '4000'},
    {'name': 'Samsung S8', 'price': '5000'},
    {'name': 'Samsung S9', 'price': '6000'},
    {'name': 'Samsung S10', 'price': '7000'}
]

# 5- Ürünlerin fiyatları toplamı nedir?
fiyatToplam = 0
for telefon in urunler:
    fiyatToplam += int(telefon['price'])
print(f'Telefonların toplam fiyatı: {fiyatToplam}')
print('*'*100)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.
print("Fiyatı 5000'den ucuz olan telefonlar:")
for telefon in urunler:
    fiyat = int(telefon['price'])
    if(fiyat <= 5000):
        print(telefon['name'])