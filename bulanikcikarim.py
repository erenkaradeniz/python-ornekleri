"""
Eren Karadeniz
201313172085
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
    yavas ve yakin --> Hafif Fren 0
    yavas ve orta --> Hafif Fren 1
    yavas ve uzak --> Hafif Fren 2
    normal ve yakin --> Normal Fren 3
    normal ve orta --> Normal Fren 4
    normal ve uzak --> Hafif Fren 5
    hizli ve yakin --> Güçlü Fren 6
    hizli ve orta --> Güçlü Fren 7
    hizli ve uzak --> Normal Fren 8
    """
    
    for i in range(3):
        for j in range(3):
            if(hizdegerler[i] < mesafedegerler[j]):
                ciktilar.append(hizdegerler[i])
            else:
                ciktilar.append(mesafedegerler[j])

    return ciktilar

def min_max(degerler):
	return max(degerler)

def main():
    hiz = float(input('Hiz giriniz(Km) : '))
    mesafe = float(input('Mesafe giriniz(Metre) : '))

    kural = kurallar(hizbulanik(hiz), mesafebulanik(mesafe))
    hafifdegerler = [kural[0], kural[1], kural[2], kural[5]]
    normaldegerler = [kural[3], kural[4], kural[8]]
    gucludegerler = [kural[6], kural[7]]



    print("Hafif Fren : ", hafifdegerler, "\nNormal Fren : ", normaldegerler, "\nGuclu Fren : ", gucludegerler)
    print(min_max(hafifdegerler), min_max(normaldegerler), min_max(gucludegerler))


main()
