import random as rand
from colorama import Fore

havuz = []
liste = []
tempListe = []
cizgi = Fore.GREEN + "-"
matrix = 8
siyah = Fore.RED + "x"
beyaz = Fore.BLUE + "O"


def ardisikKontrol(l):
    l.sort()
    for i in l:
        for k in l:
            if i + 1 == k:
                return True
    return False


def esitKontrol(l):
    for i in l:
        adet = l.count(i)
        if adet > 1:
            return True
    return False


def tazele():
    for i in range(0, matrix):  # ilk liste doldurma
        liste.append(beyaz)
        tempListe.append(beyaz)


tazele()
sayac = 1
say = 1
print(f"{' '.join(tempListe)} {cizgi} {say}")
print("*******************")

while sayac < 5000:
    rSayi1 = rand.randint(1, matrix - 1)
    tempListe[rSayi1] = siyah
    if tempListe not in havuz:
        say += 1
        havuz.append(tempListe)
        print(f"{' '.join(tempListe)} {cizgi} {say}")
        tempListe = list.copy(liste)
    else:
        tempListe = list.copy(liste)
    sayac += 1

print(f"Deneme sayisi: {sayac}")
print("*******************")

sayac = 0
while sayac < 5000:
    rSayi1 = rand.randint(1, matrix - 1)
    rSayi2 = rand.randint(1, matrix - 1)
    ardisikListe = [rSayi1, rSayi2]
    ardisikBayrak = ardisikKontrol(ardisikListe)
    esitMi = esitKontrol(ardisikListe)

    if esitMi == False and ardisikBayrak == False:
        tempListe[rSayi1] = siyah
        tempListe[rSayi2] = siyah
        if tempListe not in havuz:
            say += 1
            havuz.append(tempListe)
            print(f"{' '.join(tempListe)} {cizgi} {say}")
            tempListe = list.copy(liste)
        else:
            tempListe = list.copy(liste)
    sayac += 1

print(f"Deneme sayisi: {sayac}")
print("********************")

sayac = 0
while sayac < 5000:
    rSayi1 = rand.randint(1, matrix - 1)
    rSayi2 = rand.randint(1, matrix - 1)
    rSayi3 = rand.randint(1, matrix - 1)
    ardisikListe = [rSayi1, rSayi2, rSayi3]
    ardisikBayrak = ardisikKontrol(ardisikListe)
    estiMi = esitKontrol(ardisikListe)

    if estiMi == False and ardisikBayrak == False:
        tempListe[rSayi1] = siyah
        tempListe[rSayi2] = siyah
        tempListe[rSayi3] = siyah
        if tempListe not in havuz:
            say += 1
            havuz.append(tempListe)
            print(f"{' '.join(tempListe)} {cizgi} {say}")
            tempListe = list.copy(liste)
        else:
            tempListe = list.copy(liste)
    sayac += 1

print(f"Deneme sayisi: {sayac}")
print("********************")

sayac = 0
while sayac < 5000:
    rSayi1 = rand.randint(1, matrix - 1)
    rSayi2 = rand.randint(1, matrix - 1)
    rSayi3 = rand.randint(1, matrix - 1)
    rSayi4 = rand.randint(1, matrix - 1)
    ardisikListe = [rSayi1, rSayi2, rSayi3, rSayi4]
    ardisikBayrak = ardisikKontrol(ardisikListe)
    estiMi = esitKontrol(ardisikListe)

    if estiMi == False and ardisikBayrak == False:
        tempListe[rSayi1] = siyah
        tempListe[rSayi2] = siyah
        tempListe[rSayi3] = siyah
        tempListe[rSayi4] = siyah
        if tempListe not in havuz:
            say += 1
            havuz.append(tempListe)
            print(f"{' '.join(tempListe)} {cizgi} {say}")
            tempListe = list.copy(liste)
        else:
            tempListe = list.copy(liste)
    sayac += 1

print(f"Deneme sayisi: {sayac}")
print("********************")
print(Fore.WHITE)
print("""Bu varyasyonlar 8x8 olan satranc tahtasinin 8'li tek bir satiri icin 34 adettir.
8 satira da aynen uygulanirsa 8 x 34 = 272 adet olur.
Bu 34 varyasyonu 8 satira farkli ve ayri ayri uygulayacak olursak:
1.Satir icin 34
2.Satir icin 33
3.Satir icin 32
4.Satir icin 31
5.Satir icin 30
6.Satir icin 29
7.Satir icin 28
8.Satir icin 27 adet varyasyon olusacaktir.
Bu sekilde gecerli kosullarda 8x8 yerlestirme icin,
toplam 34 x 33 x 32 x 31 x 30 x 29 x 28 x 27 = 732.058.145.280 adet varyasyon cikmaktadir.
""")