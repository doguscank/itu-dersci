import ders_class as ders
import gun_class as gun
import fonksiyonlar as func
import veritabani_guncelleme as db
from PyQt5.QtWidgets import QApplication, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QGridLayout, QAction, QMainWindow, QWidget, QPushButton, QComboBox, QLineEdit, QMenuBar, QCheckBox, QDialog
from PyQt5.QtCore import pyqtSlot, Qt

class App(QWidget):
	def __init__(self, gunler):
		super().__init__()
		self.title = 'Ders Programı Oluşturucu'
		self.left = 400
		self.right = 200
		self.width = 660
		self.height = 840
		self.cboxSayisi = 0
		self.cboxBaseSayi = 5
		self.ders_labellar = []
		self.initUI(gunler)

	def initUI(self, gunler):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.right, self.width, self.height)

		self.createTable(gunler)
		self.tabloyuDoldur(gunler)

		self.main_menu = QMenuBar()
		ayarlar_menu = self.main_menu.addMenu('Ayarlar')
		db_guncelleme = QAction('Veritabanını Güncelle', self)
		ayarlar_menu.addAction(db_guncelleme)

		db_guncelleme.triggered.connect(db.db_guncelle)

		self.dersKoduLbl = QLabel('Bölüm kodunuzu giriniz: ')
		self.dersKoduInput = QLineEdit(self)

		self.gun_label = QLabel('Boş bırakmak istediğiniz günleri seçiniz: ', self)
		self.pzt_check = QCheckBox('Pazartesi', self)
		self.sali_check = QCheckBox('Sali', self)
		self.crs_check = QCheckBox('Carsamba', self)
		self.prs_check = QCheckBox('Persembe', self)
		self.cuma_check = QCheckBox('Cuma', self)

		self.dersEklemeButonu = QPushButton('Ders Ekle', self)
		self.dersEklemeButonu.setToolTip('Ders eklemek için tıklayın.')
		self.dersEklemeButonu.clicked.connect(self.cboxEkleme)

		self.programOlusturmaButonu = QPushButton('Program Oluştur', self)
		self.programOlusturmaButonu.setToolTip('Ders programı oluşturmak için tıklayın.')
		self.programOlusturmaButonu.clicked.connect(self.programOlustur)

		self.layout = QGridLayout()
		self.layout.addWidget(self.main_menu, 0, 0, 1, 10)
		self.layout.addWidget(self.dersKoduLbl, 1, 0, 1, 2)
		self.layout.addWidget(self.dersKoduInput, 1, 2, 1, 2)
		self.layout.addWidget(self.gun_label, 2, 0, 1, 10)
		self.layout.addWidget(self.pzt_check, 3, 0, 1, 2)
		self.layout.addWidget(self.sali_check, 3, 2, 1, 2)
		self.layout.addWidget(self.crs_check, 3, 4, 1, 2)
		self.layout.addWidget(self.prs_check, 3, 6, 1, 2)
		self.layout.addWidget(self.cuma_check, 3, 8, 1, 2)
		self.layout.addWidget(self.programOlusturmaButonu, 101, 3, 1, 4)
		self.layout.addWidget(self.tableWidget, 100, 0, 1, 10)
		self.layout.addWidget(self.dersEklemeButonu, 99, 3, 1, 4)
		self.setLayout(self.layout)

		self.show()

	def widgetSil(self, widgetlar):
		if len(widgetlar) > 0:
			for widget in widgetlar:
				widget.close()

	def cboxSil(self, widgetlar):
		self.cboxSayisi -= 1
		self.widgetSil(widgetlar)

	def labelTemizle(self):
		self.widgetSil(self.ders_labellar)
		self.ders_labellar = []

	def comboboxEkle(self):
		cbox = QComboBox(self)
		cboxHoca = QComboBox(self)

		cboxSilmeButonu = QPushButton('Sil', self)
		cboxSilmeButonu.setToolTip('Dersi sil.')
		ders_adlari = func.ders_adlarini_cek()

		for ders_adi in ders_adlari:
			cbox.addItem(ders_adi)

		cbox.activated[str].connect(lambda text : self.dersDegisti(text, cboxHoca))
		cboxSilmeButonu.clicked.connect(lambda _: self.cboxSil([cbox, cboxSilmeButonu, cboxHoca]))
		self.layout.addWidget(cbox, self.cboxSayisi + self.cboxBaseSayi, 0, 1, 3)
		self.layout.addWidget(cboxHoca, self.cboxSayisi + self.cboxBaseSayi, 3, 1, 4)
		self.layout.addWidget(cboxSilmeButonu, self.cboxSayisi + self.cboxBaseSayi, 7, 1, 1)
		self.cboxSayisi += 1
		self.setLayout(self.layout)

	def createTable(self, gunler):
		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(11)
		self.tableWidget.setColumnCount(6)
		
	def tabloyuTemizle(self):
		for i in range(1, len(gunler) + 1):
			for j in range(1, len(gunler[0].saatler) + 1):
				self.tableWidget.setItem(j, i, QTableWidgetItem(""))

	def tabloyuDoldur(self, gunler):
		for i in range(1, len(gunler[0].saatler) + 1, 1):
			self.tableWidget.setItem(i, 0, QTableWidgetItem(f"{gunler[0].saatler[i - 1].saat}:30 - {int(gunler[0].saatler[i - 1].saat) + 1}:30"))

		for i in range(len(gunler)):
			for j in range(len(gunler[i].saatler) + 1):
				if j == 0:
					self.tableWidget.setItem(j, i + 1, QTableWidgetItem(gunler[i].ad))
				else:
					self.tableWidget.setItem(j, i + 1, QTableWidgetItem(gunler[i].saatler[j - 1].ders))

	def dersDegisti(self, text, cbox):
		cbox.clear()

		hocalar = func.ders_hocalarini_cek(text)
		cbox.addItem("Herhangi bir hoca")

		for hoca in hocalar:
			cbox.addItem(hoca)

	def dersLabelleriniKoy(self, dersler):
		self.labelTemizle()

		for ders in dersler:
			yeni_label = QLabel(f'{func.ayirma(ders.crn)}, {func.ayirma(ders.ad)}, {func.ayirma(ders.hoca)}, {func.ayirma(ders.gunler)}, {func.ayirma(ders.saatler)}, {func.ayirma(ders.binalar)}, {func.ayirma(ders.siniflar)}')
			self.ders_labellar.append(yeni_label)
			self.layout.addWidget(yeni_label, (99 - len(self.ders_labellar)), 0, 1, 10)
			self.setLayout(self.layout)

	def gunleriAyikla(self, dersler):
		gun_adlari = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]
		gun_cb = [self.pzt_check, self.sali_check, self.crs_check, self.prs_check, self.cuma_check]
		yeni_dersler = dersler
		for i in range(len(gun_cb)):
			if gun_cb[i].isChecked():
				yeni_dersler = func.gun_bos_birakma(gun_adlari[i], yeni_dersler)

		return yeni_dersler

	@pyqtSlot()
	def programOlustur(self):
		children = self.findChildren(QComboBox)
		istenen_dersler, istenen_hocalar = [], []
		bolum = self.dersKoduInput.text().upper()
		derslerListe = func.dersleri_cek()

		for child in children:
			if child.isVisible():
				child_index = children.index(child)
				if (child_index % 2 == 0):
					istenen_dersler.append(str(child.currentText()))
				else:
					istenen_hocalar.append(str(child.currentText()))

		dersler_elenecek = []
		dersler_gonderilecek = []

		for _ders in derslerListe.dersler:
			if _ders.ad in istenen_dersler:
				dersler_elenecek.append(_ders) 

		for ders_adi in istenen_dersler: 
			dersler_hoca_elenecek = []

			for _ders in dersler_elenecek:
				if _ders.ad == ders_adi: 
					dersler_hoca_elenecek.append(_ders)

			index = istenen_dersler.index(ders_adi) 
			gonderilecek_hoca = istenen_hocalar[index] 

			dersler_gonderilecek.extend(func.tek_ders_hoca_eleme(gonderilecek_hoca, dersler_hoca_elenecek))

		programdaki_dersler = func.program_olustur(bolum, func.karistir(dersler_gonderilecek), app = self)

		if not programdaki_dersler == None:
			self.dersLabelleriniKoy(programdaki_dersler)

	@pyqtSlot()
	def cboxEkleme(self):
		if self.cboxSayisi <= 9:
			self.comboboxEkle()
		else:
			print("Maksimum ders sayısına ulaşıldı!")

class DersProgramGUI:
	def __init__(self, gunler):
		self.app = QApplication([])
		self.executable = App(gunler)
		self.app.exec_()

	def get_GUI_app(self):
		return self.executable

	def update_GUI(gunler):
		self.executable.tabloyuDoldur(gunler)

def popup_olustur(popup_text, buton_text):
	popup = QDialog()
	layout = QVBoxLayout()
	label = QLabel(popup_text, popup)
	buton = QPushButton(buton_text, popup)
	buton.clicked.connect(popup.close)
	layout.addWidget(label, stretch = 12, alignment = Qt.AlignVCenter)
	layout.addWidget(buton, stretch = 12, alignment = Qt.AlignVCenter)
	popup.setLayout(layout)
	popup.setModal(True)
	popup.exec_()