
# 1- Girilen 2 sayıdan hangisi büyüktür?
a = int(input('1. Sayı: '))
b = int(input('2. Sayı: '))

result = (a > b)
print(f'a: {a} b: {b} den büyüktür: {result}')

# 2- )Kullanıcıdan 2 vize ve final (%60-%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

vize1 = float(input('1. vize notu: '))
vize2 = float(input('2. vize notu: '))
final = float(input('Final notu: '))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
print(f'not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama >= 50}')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

sayi = int(input('Sayı Giriniz: '))
tekcift = (sayi % 2 == 0)

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
pozitif = (sayi > 0)

print(f'Girdiğiniz sayı: {sayi}, Çift sayı olma durumu: {tekcift}, Pozitif olma durumu: {pozitif}')

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@sadikturan.com parola: abc123) 

email = 'email@sadikturan.com'
password = 'abc123'

girilenEmail = input('E-Posta Adresi Giriniz: ')
girilenSifre = input('Şifre Giriniz: ')

isEmail = (email == girilenEmail)
isPassword = (password == girilenSifre)

print(f'E-Posta Doğru mu: {isEmail}, Şifre Doğru mu: {isPassword}')