import fonksiyonlar as func
import ders_class as ders
import os
import veritabani_guncelleme as db_guncelle
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QApplication, QVBoxLayout, QCheckBox
from PyQt5.QtCore import pyqtSlot, Qt
from ders_programi_gui import popup_olustur

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'Alternatif CRNci'
		self.left = 500
		self.right = 400
		self.width = 200
		self.height = 120
		self.label_sayi = 0
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.right, self.width, self.height)

		self.crn_giris_label = QLabel('CRNleri virgul ile ayirarak giriniz:', self)
		self.crn_giris = QLineEdit(self)
		self.crn_getir = QPushButton('Alternatif Getir', self)
		self.crn_getir.clicked.connect(lambda _: self.alternatif_getir(self.crn_giris.text()))

		self.alt_kaydet = QPushButton('Alternatifleri Kaydet', self)
		self.alt_kaydet.clicked.connect(lambda _: self.kaydet(self.crn_giris.text()))

		self.kontenjan_bos = QCheckBox('Bos kontenjani olsun')

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.crn_giris_label)
		self.layout.addWidget(self.crn_giris)
		self.layout.addWidget(self.kontenjan_bos)
		self.layout.addWidget(self.crn_getir)
		self.layout.addWidget(self.alt_kaydet)

		self.setLayout(self.layout)
		self.show()

	@pyqtSlot()
	def alternatif_getir(self, crnler):
		crn_liste = func.ayirma(crnler)

		if isinstance(crn_liste, list):
			for crn in crn_liste:
				self.label_ekle(self.dersleri_getir(crn))
		else:
			self.label_ekle(self.dersleri_getir(crn_liste))

	def dersleri_getir(self, crn):		
		kontrol = crn.isnumeric()

		if kontrol:
			try:
				dersler = func.dersleri_cek().dersler
			except Exception:
				db_guncelle.db_guncelle()
				dersler = func.dersleri_cek().dersler

			referans_dersler, alternatif_dersler = [], []

			for ders in dersler:
				if ders.crn == crn:
					referans_dersler.append(ders)

			for ders in dersler:
				for _ders in referans_dersler:
					if ders.ad == _ders.ad and ders.gunler == _ders.gunler and ders.saatler == _ders.saatler and (ders not in alternatif_dersler):
						if self.kontenjan_bos.isChecked():
							if ders.dolu_kontenjan < ders.kontenjan:
								alternatif_dersler.append(ders)
						else:
							alternatif_dersler.append(ders)

			return alternatif_dersler

		else:
			popup_olustur('Lutfen gecerli CRN giriniz!', 'Tamam', 'CRN')
			return None

	def ders_info(self, ders):
		info = f'{func.ayirma(ders.ad)}, {func.ayirma(ders.gunler)}, {func.ayirma(ders.saatler)}'

		return info

	def label_ekle(self, dersler):
		if isinstance(dersler, list) and len(dersler) > 0:
			info = self.ders_info(dersler[0])
		else:
			info = None

		if info != None:
			ayirici = ','
			crn_text = ayirici.join(ders.crn for ders in dersler)
			info_text = f'{info}: {crn_text}'
			alternatif_crn_label = QLabel(info_text, self)

			self.layout.addWidget(alternatif_crn_label)		
			self.setLayout(self.layout)

	@pyqtSlot()
	def kaydet(self, crnler):
		path = os.getcwd()
		path_to_check = path + r"\kayitlar"

		if not os.path.exists(path_to_check):
			os.mkdir(path_to_check)

		f = open('kayitlar/alternatif_crnler.txt', 'a+')
		crn_liste = func.ayirma(crnler)

		if isinstance(crn_liste, list):
			for crn in crn_liste:
				alt = self.dersleri_getir(crn)				
				ayirici = ','
				alt_text = ayirici.join(ders.crn for ders in alt)

				if len(alt) > 0 and isinstance(alt, list):
					info_text = self.ders_info(alt[0])
				else:
					continue

				f.write(f'{info_text}: {alt_text}\n')
			f.write('\n\n')
		else:
			alt = self.dersleri_getir(crn_liste)
			ayirici = ','
			alt_text = ayirici.join(ders.crn for ders in alt)
			info_text = self.ders_info(alt[0])
			f.write(f'{info_text}: {alt_text}\n')
			f.write('\n\n')
		f.close()

if __name__ == '__main__':
	app = QApplication([])
	exe_ = App()
	app.exec_()