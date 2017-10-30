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
        hizlist.append(1.0)
    elif(yavas < hiz <= normal):
        hizlist.append((normal - hiz) / (normal - yavas))
    else:
        hizlist.append(0.0)

    if(yavas < hiz <= normal):
        hizlist.append((hiz - yavas) / (normal - yavas))
    elif(normal < hiz <= hizli):
        hizlist.append((hizli - hiz) / (hizli - normal))
    else:
        hizlist.append(0.0)

    if(normal < hiz <= hizli):
        hizlist.append((hiz - normal) / (hizli - normal))
    elif(hizli < hiz):
        hizlist.append(hizli/hizli)
    else:
        hizlist.append(0.0)
    return hizlist


def mesafebulanik(mesafe):
    mesafelist = []
    if(0 < mesafe <= yakin):
        mesafelist.append(1.0)
    elif(yakin < mesafe <= orta):
        mesafelist.append((orta - mesafe) / (orta - yakin))
    else:
        mesafelist.append(0.0)

    if(yakin < mesafe <= orta):
        mesafelist.append((mesafe - yakin) / (orta - yakin))
    elif(orta < mesafe <= uzak):
        mesafelist.append((uzak - mesafe) / (uzak - orta))
    else:
        mesafelist.append(0.0)

    if(orta < mesafe <= uzak):
        mesafelist.append((mesafe - orta) / (uzak - orta))
    elif(uzak < mesafe):
        mesafelist.append(uzak/uzak)
    else:
        mesafelist.append(0.0)
    return mesafelist


def kurallar(hizdegerler, mesafedegerler):
    ciktilar = []
    """
    yavas ve yakin --> Hafif Fren
    yavas ve orta --> Hafif Fren
    yavas ve uzak --> Hafif Fren
    normal ve yakin --> Normal Fren
    normal ve orta --> Normal Fren
    normal ve uzak --> Hafif Fren
    hizli ve yakin --> Güçlü Fren
    hizli ve orta --> Güçlü Fren
    hizli ve uzak --> Normal Fren
    """
    
    if(hizdegerler[0] < mesafedegerler[0]):
        ciktilar.append(hizdegerler[0])
    else:
        ciktilar.append(mesafedegerler[0])

    if(hizdegerler[0] < mesafedegerler[1]):
        ciktilar.append(hizdegerler[0])
    else:
        ciktilar.append(mesafedegerler[1])

    if(hizdegerler[0] < mesafedegerler[2]):
        ciktilar.append(hizdegerler[0])
    else:
        ciktilar.append(mesafedegerler[2])

    if(hizdegerler[1] < mesafedegerler[0]):
        ciktilar.append(hizdegerler[1])
    else:
        ciktilar.append(mesafedegerler[0])

    if(hizdegerler[1] < mesafedegerler[1]):
        ciktilar.append(hizdegerler[1])
    else:
        ciktilar.append(mesafedegerler[1])

    if(hizdegerler[1] < mesafedegerler[2]):
        ciktilar.append(hizdegerler[1])
    else:
        ciktilar.append(mesafedegerler[2])

    if(hizdegerler[2] < mesafedegerler[0]):
        ciktilar.append(hizdegerler[2])
    else:
        ciktilar.append(mesafedegerler[0])

    if(hizdegerler[2] < mesafedegerler[1]):
        ciktilar.append(hizdegerler[2])
    else:
        ciktilar.append(mesafedegerler[1])

    if(hizdegerler[2] < mesafedegerler[2]):
        ciktilar.append(hizdegerler[2])
    else:
        ciktilar.append(mesafedegerler[2])

    return ciktilar


def main():
    hiz = float(input('Hiz giriniz(Km) : '))
    mesafe = float(input('Mesafe giriniz(Metre) : '))

    print(kurallar(hizbulanik(hiz), mesafebulanik(mesafe)))


main()
