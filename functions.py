def sayHello(name = 'User'):
    return f"Hello, {name}!"

msg = sayHello("Çınar")

print(msg)

def total(num1, num2):
    return num1 + num2

result = total(5, 10)
print(result)

def yasHesapla(dogumYili):
    return 2026 - dogumYili

ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)
ageSena = yasHesapla(1999)
print(ageCinar, ageAda, ageSena)

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldığını hesaplar.
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f"{isim}, emekliliğine {emeklilik} yıl kaldı.")
    else:
        print(f"{isim}, zaten emekli olmuş.")

EmekliligeKacYilKaldi(1983, 'Ali')

print(help(EmekliligeKacYilKaldi))