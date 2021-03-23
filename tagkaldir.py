from bs4 import BeautifulSoup
import sqlite3
def temizlegonder(gelen):
        gonder = ''
        temizle = BeautifulSoup(gelen,"html.parser")
        topla = temizle.find_all("p")
        for bol in topla:
                gonder+=bol.text
        return gonder
        


vt = sqlite3.connect("ruyana.db")
imlec = vt.cursor()
for i in range(1,32838):
        
        imlec.execute("""SELECT id,icerik FROM yeni WHERE id="""+str(i))
        oku = imlec.fetchone()
        temizveri = temizlegonder(oku[1])
        kk =(temizveri,i)
        imlec.execute("""UPDATE yeni SET icerik=(?) WHERE id=(?)""",kk)
        print(i)
vt.commit()
vt.close()

