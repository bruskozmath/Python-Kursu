
# ogrenciler = {
#     '120' : {
#         'ad' : 'Ali',
#         'soyad' : 'Yılmaz',
#         'telefon' : '0532 000 00 01'
#     },
#     '125' : {
#         'ad' : 'Can',
#         'soyad' : 'Korkmaz',
#         'telefon' : '0532 000 00 02'
#     },
#     '128' : {
#         'ad' : 'Volkan',
#         'soyad' : 'Yükselen',
#         'telefon' : '0532 000 00 03'
#     }
# }

    # 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

    # 2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

ogrenciler = {}

number = input('Öğrenci Numaran: ')
name = input('Adın: ')
surname = input('Soyadın: ')
phone = input('Telefon numaran: ')

# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'telefon': phone
# }
ogrenciler.update({
        number: {
            'ad': name,
            'soyad': surname,
            'telefon': phone
        }
})

number = input('Öğrenci Numaran: ')
name = input('Adın: ')
surname = input('Soyadın: ')
phone = input('Telefon numaran: ')

ogrenciler.update({
        number: {
            'ad': name,
            'soyad': surname,
            'telefon': phone
        }
})

number = input('Öğrenci Numaran: ')
name = input('Adın: ')
surname = input('Soyadın: ')
phone = input('Telefon numaran: ')

ogrenciler.update({
        number: {
            'ad': name,
            'soyad': surname,
            'telefon': phone
        }
})

print(ogrenciler)

print('*'*50)
ogrNo = input('Öğrenci Numarası Giriniz: ')
ogrenci = ogrenciler[ogrNo]

print(f'Aradığınız Öğrenci: {ogrenci}') 
