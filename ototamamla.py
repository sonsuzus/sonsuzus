import os
dosyalar = os.listdir("pages")
f = open("suggestions.xml","a")
sayac = 0
for dosya in dosyalar:
	ruyara = dosya.replace('-',' ')
	f.write("\n\t<Autocompletion term=\""+ruyara+"\" type=\"1\" match=\"1\"/>")
	sayac=sayac+1
print(sayac)