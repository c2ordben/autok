f = open('autok2sorban.txt', 'r', encoding='utf-8')
autok = []
kmAllasok = []

for sor in f:
    autok.append(sor.strip())
    sor = f.readline()
    kmAllasok.append(int(sor.strip()))
print(autok)
print(kmAllasok)


kis = 0
toyotaSzama = 0
osszFutas = sum(kmAllasok) # Összes autó ennyi km-t tett meg
maxFutasTelj = 0 # Helyet tárolunk, nem az értéket / lista indexét tárolom
for km in kmAllasok:
    if km < 20000:
        kis += 1



'''
for auto in autok:
    gyarto = auto.split(' ')[0]
    if gyarto = 'Toyota':
        toyotaSzama += 1
'''
for auto in autok:
    if 'toyota' in auto.lower():
        toyotaSzama += 1

for i in range(len(kmAllasok)):
    if kmAllasok[maxFutasTelj] < kmAllasok[i]:
        maxFutasTelj = i        # Ezen a helyen lesz a legnagyobb futásteljesítmény


print(kis, 'autó ment 20 ezernél kevesebbet')
print(toyotaSzama, 'Toyota van')
print('a legnagyobb futás teljesítményű autó:', autok[maxFutasTelj])
print('Átlagos futásteljesítmény:', round(osszFutas/len(kmAllasok), 2))