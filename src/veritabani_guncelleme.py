from bs4 import BeautifulSoup
import urllib3
import ders_class
import ders_programi_gui as dp_gui
import os.path

def db_guncelle(app = None):

	path = os.path.dirname(os.path.abspath(__file__))
	path_to_check = path + r"\veritabani"

	if not os.path.exists(path_to_check):
		os.mkdir(path_to_check)
		os.mkdir(path_to_check + r"\dersler")
		db_guncelle()

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

	#print(ders_kodlari)

	for ders_kodu in ders_kodlari:
		
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
			
			ders = ders_class.Ders("crn", "ad", "hoca", [], [], [], "kontenjan", [], [])

			ders.crn = td_list[0].string
			ders.ad = td_list[1].string
			ders.hoca = td_list[3].string
			ders.kontenjan = td_list[8].string

			gun_sayisi = len(td_list[5].find_all('br'))

			for i in range(len(td_list[4].find_all('a')[0].contents)):
				if i % 2  == 0:
					ders.binalar.append(td_list[4].find_all('a')[0].contents[i])

			for i in range(gun_sayisi):
				ders.gunler.append(td_list[5].contents[2 * i])
				ders.saatler.append(td_list[6].contents[2 * i])
				ders.siniflar.append(td_list[7].contents[2 * i])

			if not td_list[11].string is None:
				if ',' in td_list[11].string:
					ders.alabilen = td_list[11].string.split(',')
				else:
					ders.alabilen = td_list[11].string
			else:
				ders.alabilen = ""
			#print(f"crn: {ders.crn}\nad: {ders.ad}\nhoca: {ders.hoca}\nkontejan: {ders.kontenjan}\ngünler: {ders.gunler}\nsaatler: {ders.saatler}\nsınıflar: {ders.siniflar}\nalabilenler: {ders.alabilen}")
			dersler.append(ders)

			f = open(f"veritabani/dersler/{ders_kodu}.txt", "a")
			f.write(f"{ders.crn};{ders.ad};{ders.hoca};{ders.kontenjan};{ders.gunler};{ders.saatler};{ders.siniflar};{ders.alabilen};{ders.binalar}\n")
			f.close()

	dp_gui.popup_olustur('Veritabanı başarıyla güncellendi!', 'Tamam')