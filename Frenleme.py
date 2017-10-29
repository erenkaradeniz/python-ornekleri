"""
Bulanık Mantık Fren Sistemi
"""

yavas = 50
normal = 100
hizli = 150
yakin = 25
orta = 50
uzak = 75


def hizbulanik(hiz):
    hizlist = []
    if(0 < hiz <= yavas):
        hizlist.append(1)
    elif(yavas < hiz <= normal):
        hizlist.append((normal - hiz) / (normal - yavas))
    else:
        hizlist.append(0)

    if(yavas < hiz <= normal):
        hizlist.append((hiz - yavas) / (normal - yavas))
    elif(normal < hiz <= hizli):
        hizlist.append((hizli - hiz) / (hizli - normal))
    else:
        hizlist.append(0)

    if(normal < hiz <= hizli):
        hizlist.append((hiz - normal) / (hizli - normal))
    elif(hizli < hiz):
        hizlist.append(hizli/hizli)
    else:
        hizlist.append(0)
    return hizlist


def mesafebulanik(mesafe):
    mesafelist = []
    if(0 < mesafe <= yakin):
        mesafelist.append(1)
    elif(yakin < mesafe <= orta):
        mesafelist.append((orta - mesafe) / (orta - yakin))
    else:
        mesafelist.append(0)

    if(yakin < mesafe <= orta):
        mesafelist.append((mesafe - yakin) / (orta - yakin))
    elif(orta < mesafe <= uzak):
        mesafelist.append((uzak - mesafe) / (uzak - orta))
    else:
        mesafelist.append(0)

    if(orta < mesafe <= uzak):
        mesafelist.append((mesafe - orta) / (uzak - orta))
    elif(uzak < mesafe):
        mesafelist.append(uzak/uzak)
    else:
        mesafelist.append(0)
    return mesafelist


def main():
    hiz = float(input('Hiz giriniz(Km) : '))
    mesafe = float(input('Mesafe giriniz(Metre) : '))

    #print(hizbulanik(hiz))
    #print(mesafebulanik(mesafe))


main()