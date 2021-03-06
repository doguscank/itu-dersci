from bs4 import BeautifulSoup
import urllib3
import ders_class
import ders_programi_gui as dp_gui
import fonksiyonlar as func
import os.path

def duzeltme(duzeltilecek): 
	table = duzeltilecek.maketrans("İıÜüĞğÇçŞşÖö", "IiUuGgCcSsOo")
	duzgun = duzeltilecek.translate(table)
	return duzgun

def db_guncelle(ders_guncellenecek = False, guncellenecek_dersler = None):

	path = os.getcwd()
	path_to_check = path + r"\veritabani"

	if not os.path.exists(path_to_check):
		os.mkdir(path_to_check)
		os.mkdir(path_to_check + r"\dersler")

	manager = urllib3.PoolManager(1)
	url = 'http://www.sis.itu.edu.tr/tr/ders_programlari/LSprogramlar/prg.php?fb=MAT'
	html = manager.urlopen('GET', url)

	soup = BeautifulSoup(html.data, 'lxml')

	f = open('veritabani/ders_kodlari.txt', 'w').close()
	f = open('veritabani/ders_kodlari.txt', 'a')

	ders_kodlari = []

	for option in soup.find_all('option'):
		if option['value'] != '':
			f.write(f"{option['value']}\n")
			ders_kodlari.append(option['value'])

	f.close()

	#ders guncelleyemeye gore secim yap

	if ders_guncellenecek and guncellenecek_dersler != None and isinstance(guncellenecek_dersler, list):
		ders_kodlari.clear()

		for ders_kodu in guncellenecek_dersler:
			ders_kodlari.append(ders_kodu)

	try:
		for ders_kodu in ders_kodlari:
			
			print(f'{ders_kodu} veritabani guncelleniyor...')

			url = f'http://www.sis.itu.edu.tr/tr/ders_programlari/LSprogramlar/prg.php?fb={ders_kodu}'

			html = manager.urlopen('GET', url)

			soup = BeautifulSoup(html.data, 'lxml')

			f = open(f"veritabani/dersler/{ders_kodu}.txt", "w").close()

			dersler = []

			tr_sayisi = len(soup.find_all('tr'))

			for j in range(4, tr_sayisi - 1):
				td_list = []
				
				for td in soup.find_all('tr')[j].find_all('td'):
					td_list.append(td)
				
				ders = ders_class.Ders("crn", "ad", "hoca", [], [], [], "dolu_kontenjan","kontenjan", [], [])

				ders.crn = td_list[0].string
				ders.ad = duzeltme(td_list[1].string)
				ders.hoca = duzeltme(td_list[3].string)
				ders.dolu_kontenjan = duzeltme(td_list[9].string)
				ders.kontenjan = duzeltme(td_list[8].string)

				gun_sayisi = len(td_list[5].find_all('br'))

				for i in range(len(td_list[4].find_all('a')[0].contents)):
					if i % 2  == 0:
						ders.binalar.append(td_list[4].find_all('a')[0].contents[i])

				for i in range(gun_sayisi):
					ders.gunler.append(duzeltme(td_list[5].contents[2 * i]))
					ders.saatler.append(duzeltme(td_list[6].contents[2 * i]))
					try:
						ders.siniflar.append(duzeltme(td_list[7].contents[2 * i]))
					except:
						pass

				if not td_list[11].string is None:
					if ',' in td_list[11].string:
						ders.alabilen = duzeltme(td_list[11].string).split(',')
					else:
						ders.alabilen = duzeltme(td_list[11].string)
				else:
					ders.alabilen = ""
				#print(f"crn: {ders.crn}\nad: {ders.ad}\nhoca: {ders.hoca}\nkontejan: {ders.kontenjan}\ngünler: {ders.gunler}\nsaatler: {ders.saatler}\nsınıflar: {ders.siniflar}\nalabilenler: {ders.alabilen}")
				dersler.append(ders)

				f = open(f"veritabani/dersler/{ders_kodu}.txt", "a")
				f.write(f"{ders.crn};{ders.ad};{ders.hoca};{ders.dolu_kontenjan};{ders.kontenjan};{ders.gunler};{ders.saatler};{ders.siniflar};{ders.alabilen};{ders.binalar}\n")
				f.close()

	except Exception:
		dp_gui.popup_olustur('Veritabani guncellenirken bir hata meydana geldi!', 'Tamam', 'Veritabani')

	if not ders_guncellenecek:
		dp_gui.popup_olustur('Veritabani basariyla guncellendi!', 'Tamam', 'Veritabani')