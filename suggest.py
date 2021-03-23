import sqlite3

def convertTuple(tup): 
    str =  ''.join(tup)
    return str

vt = sqlite3.connect("ruyana.db")
imlec = vt.cursor()
imlec.execute("""SELECT icerik FROM ruyatabirleri WHERE 1""")
veriler = imlec.fetchall()
f = open("sg.xml","a")
sayac = 0

for veri in veriler:
	cek = convertTuple(veri)
	bol = cek.split(" :::")
	son = bol[0]
	f.write("\n\t<Autocompletion term=\""+son+"\" type=\"1\" match=\"1\"/>")
	sayac=sayac+1
	

	