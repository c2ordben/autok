def beolvas_autok(file_nev):
    autok = []
    with open(file_nev, 'r') as file:
        sorok = file.readlines()
        for i in range(0, len(sorok), 2):
            marka = sorok[i].strip()  
            km = int(sorok[i+1].strip())  
            autok.append((marka, km))
    return autok


def kevesebb_20ezer(autok):
    szam = 0
    for auto in autok:
        if auto[1] < 20000:
            szam += 1
    print('20km-nél kevesebb: ',szam)
    return szam


def toyota_szamol(autok):
    szam = 0
    for auto in autok:
        if 'Toyota' in auto[0]:
            szam += 1
    print('Toyoták száma: ',szam)
    return szam


def legtobb_km_auto(autok):
    max_auto = autok[0] 
    for auto in autok:
        if auto[1] > max_auto[1]:
            max_auto = auto
    print('legtöbb km: ',max_auto)
    return max_auto


def atlagos_km(autok):
    osszes_km = 0
    for auto in autok:
        osszes_km += auto[1]
    atlag = osszes_km / len(autok)
    print('átlag sebesség: ',atlag)
    return atlag


file_nev = 'autok2sorban.txt'
autok = beolvas_autok(file_nev)

kevesebb_20ezer_count = kevesebb_20ezer(autok)
toyota_count = toyota_szamol(autok)
legtobb_km_auto_info = legtobb_km_auto(autok)
atlag_km_value = atlagos_km(autok)
