import ders_programi_gui as dp
import alternatif_crn as alt
import fonksiyonlar as func
import gun_class as gun
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSizePolicy
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QFont

class HubGUI(QWidget):
	def __init__(self, parent = None):
		super().__init__()
		self.title = 'Scheduler Hub'
		self.left = 400
		self.right = 200
		self.width = 300
		self.height = 300
		self.parent = parent

		self.InitGunler()
		self.InitUI()

	def InitGunler(self):
		pzt = gun.Gun("Pazartesi")
		sali = gun.Gun("Sali")
		crs = gun.Gun("Carsamba")
		prs = gun.Gun("Persembe")
		cuma = gun.Gun("Cuma")
		
		self.gunler = [pzt, sali, crs, prs, cuma]

	def InitUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.right, self.width, self.height)

		self.prog_btn = QPushButton('Programci', self)
		self.prog_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.prog_btn.clicked.connect(lambda _: self.parent.programci(self.gunler))

		self.alt_btn = QPushButton('Alternatif CRNci', self)
		self.alt_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.alt_btn.clicked.connect(lambda _: self.parent.alternatif())

		font = self.prog_btn.font()
		font.setPointSize(26)
		self.prog_btn.setFont(font)
		self.alt_btn.setFont(font)

		self.layout = QVBoxLayout()

		self.layout.addWidget(self.prog_btn)
		self.layout.addWidget(self.alt_btn)

		self.setLayout(self.layout)
		self.show()

class Hub():
	def __init__(self):
		self.app = QApplication([])
		self.hub = HubGUI(self)
		self.exe = None
		self.app.exec_()

	def alternatif(self):
		if self.exe is not None:
			self.exe.close()
		self.exe = alt.App()

	def programci(self, gunler):
		if self.exe is not None:
			self.exe.close()
		self.exe = dp.App(gunler)

if __name__ == '__main__':
	hub = Hub()