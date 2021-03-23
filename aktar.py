import sqlite3
from basliklar import baslikdondur
linkler = baslikdondur()
vt = sqlite3.connect("ruyana.db")
imlec = vt.cursor()
for link in linkler:
	dosya = open(link,encoding="utf8")
	icerik = dosya.read()
	dosya.close()
	veri =(link,icerik)
	imlec.execute("""INSERT INTO ruyatabirleri (baslik,icerik) VALUES(?,?)""",veri)
vt.commit()
vt.close()


