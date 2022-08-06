f = open('archivoe1.txt', 'w')
f.write('Un saludo desde el archivoe1!\n')
f.close()

f = open('archivoe1.txt', 'r+')
f.readline()
f.write('Otro saludo desde el archivoe1!\n')

