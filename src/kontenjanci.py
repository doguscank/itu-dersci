import threading
import sys
import ders_class as ders
import veritabani_guncelleme as db_guncelleme
import fonksiyonlar as func
import os
from notify_run import Notify
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot, Qt

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'Kontenjanci'
		self.left = 400
		self.right = 200
		self.width = 300
		self.height = 300
		self.notify = Notify()
		self.gonderilmis_bildirim = 0
		self.gonderilecek_bildirim = 10

		self.InitUI()

	def InitUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.right, self.width, self.height)

		#widgetlar

		#crn giris yeri
		self.crn_label = QLabel("CRN'leri giriniz: ")
		self.crn_giris = QLineEdit(self)

		#kac saniyede bir yenilensin
		self.sure_label = QLabel("Kac saniyede yenilensin: ")
		self.sure_giris = QLineEdit(self)

		#loop baslatma butonu
		self.kontrol_baslat = QPushButton("Kontrolu Baslat", self)
		self.kontrol_baslat.clicked.connect(self.guncelle)

		self.layout = QGridLayout()
		
		#widgetları ekle
		self.layout.addWidget(self.crn_label, 0, 0, 1, 3)
		self.layout.addWidget(self.crn_giris, 0, 3, 1, 3)
		self.layout.addWidget(self.sure_label, 1, 0, 1, 3)
		self.layout.addWidget(self.sure_giris, 1, 3, 1, 3)
		self.layout.addWidget(self.kontrol_baslat, 2, 1, 1, 4)

		self.setLayout(self.layout)
		self.show()

	def bildirim_sifirla(self):
		self.gonderilmis_bildirim = 0

	def kontenjan_kontrol(self, kodlar, crnler):
		dersler = []

		for kod in kodlar:
			dersler.extend(func.ders_cek(kod).dersler)

		for ders in dersler:
			if ders.crn in crnler:
				if (int(ders.dolu_kontenjan) < int(ders.kontenjan)) and (self.gonderilmis_bildirim < self.gonderilecek_bildirim):
					self.notify.send(f"{ders.crn} CRN'li derste boş kontenjan mevcut! {ders.dolu_kontenjan}/{ders.kontenjan}")
					self.gonderilmis_bildirim += 1
					threading.Timer(15 * 60, self.bildirim_sifirla).start()

	def bekle(self):		
		threading.Thread(target = self.guncelle, daemon = True).start()

	@pyqtSlot()
	def guncelle(self):
		cwd = os.getcwd()
		path_to_check = cwd + r"\veritabani\dersler"

		if not os.path.exists(path_to_check):
			db_guncelleme.db_guncelle()

		ders_adlari = []
		ders_kodlari = []

		crnler = func.ayirma(self.crn_giris.text())

		if isinstance(crnler, str):
			crnler = [crnler]

		ders_liste = func.dersleri_cek().dersler

		for ders in ders_liste:
			if (ders.crn in crnler) and (ders.ad not in ders_adlari):
				ders_adlari.append(ders.ad)
				ders_kodu = ders.ad.split(" ")[0]
				print(ders_kodu)
				if ders_kodu not in ders_kodlari:
					ders_kodlari.append(ders_kodu)

		print(ders_kodlari)
		db_guncelleme.db_guncelle(ders_guncellenecek = True, guncellenecek_dersler = ders_kodlari)
		
		self.kontenjan_kontrol(ders_kodlari, crnler)

		sure = float(self.sure_giris.text())
		threading.Timer(sure, self.bekle).start()

if __name__ == '__main__':
	app = QApplication([])
	exe_ = App()
	sys.exit(app.exec_())