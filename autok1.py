f = open('autok2sorban.txt', 'r', encoding='utf-8')
autok = []
kmAllasok = []

for sor in f:
    autok.append(sor.strip())
    sor = f.readline()
    kmAllasok.append(sor.strip())
print(autok)
print(kmAllasok)