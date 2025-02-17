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
for km in kmAllasok:
    if km < 20000:
        kis += 1
print(kis, 'autó ment 20 ezernél kevesebbet')


'''
for auto in autok:
    gyarto = auto.split(' ')[0]
    if gyarto = 'Toyota':
        toyotaSzama += 1
'''
for auto in autok:
    if 'toyota' in auto.lower():
        toyotaSzama += 1
print(toyotaSzama, 'Toyota van')
