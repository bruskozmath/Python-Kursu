names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
result = names

# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0, "Sena")
result = names

# 3-  "Deniz" ismini listeden siliniz.
# Opel

# 4-  "Deniz" isminin indeksi nedir ?
result = names.index("Deniz")

# 5-  "Ali" listenin bir elemanı mıdır ?
result = 'Ali' in names

# 6-  Liste elemanlarını ters çevirin.
names.reverse()
result = names

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
result = names

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
result = years

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
result = str.split(",")

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
result = min(years)
result = max(years)

# 11- years dizisinde kaç tane 1998 değeri vardır ?
result = years.count(1998)

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
result = years

# 13-  Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []

marka = input("Marka 1: ")
markalar.append(marka)
marka = input("Marka 2: ")
markalar.append(marka)
marka = input("Marka 3: ")
markalar.append(marka)
result = markalar

print(result)