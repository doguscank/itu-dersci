from bs4 import BeautifulSoup
import urllib3
import ders_class
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QWidget

def db_guncelle():
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
			
			ders = ders_class.Ders("crn", "ad", "hoca", [], [], [], "kontenjan", [])

			ders.crn = td_list[0].string
			ders.ad = td_list[1].string
			ders.hoca = td_list[3].string
			ders.kontenjan = td_list[8].string

			gun_sayisi = len(td_list[5].find_all('br'))

			for i in range(gun_sayisi):
				ders.gunler.append(td_list[5].contents[2 * i])
				ders.saatler.append(td_list[6].contents[2 * i])
				ders.siniflar.append(td_list[7].contents[2 * i])

			ders.alabilen = td_list[11].string.split(',')

			#print(f"crn: {ders.crn}\nad: {ders.ad}\nhoca: {ders.hoca}\nkontejan: {ders.kontenjan}\ngünler: {ders.gunler}\nsaatler: {ders.saatler}\nsınıflar: {ders.siniflar}\nalabilenler: {ders.alabilen}")
			dersler.append(ders)

			f = open(f"veritabani/dersler/{ders_kodu}.txt", "a")
			f.write(f"{ders.crn};{ders.ad};{ders.hoca};{ders.kontenjan};{ders.gunler};{ders.saatler};{ders.siniflar};{ders.alabilen}\n")
			f.close()

	update_onay = QDialog()
	update_onay.setGeometry(400, 200, 240, 100)
	onay_label = QLabel('Veritabanı başarıyla güncellendi!', update_onay)
	onay_label.move(35, 20)
	onay_btn = QPushButton('Tamam', update_onay)
	onay_btn.move(80, 55)
	onay_btn.clicked.connect(update_onay.close)
	update_onay.setModal(True)
	update_onay.exec_()