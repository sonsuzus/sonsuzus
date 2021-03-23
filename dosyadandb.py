import os
import sqlite3

dosyalar = os.listdir("ruyoka")
vt = sqlite3.connect("ruyana.db")
imlec = vt.cursor()
for dosya in dosyalar:
	u = "ruyoka/"+dosya
	d = open(u,encoding="utf8")
	icerik = d.read()
	d.close()
	veri =(dosya,icerik)
	imlec.execute("""INSERT INTO ruyoka (baslik,icerik) VALUES(?,?)""",veri)
vt.commit()
vt.close()

"""
from basliklar import baslikdondur
linkler = baslikdondur()
a = 0
for link in linkler:
	dosya = open(link,encoding="utf8")
	icerik = dosya.read()
	dosya.close()
	print(icerik)
	a+=1
	if a==5:
		break
"""