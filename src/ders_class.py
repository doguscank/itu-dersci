class Ders:
	def __init__(self, crn, ad, hoca, gunler, saatler, siniflar, dolu_kontenjan, kontenjan, alabilen, binalar):
		self.crn = crn
		self.ad = ad
		self.hoca = hoca
		self.binalar = binalar
		self.gunler = gunler
		self.saatler = saatler
		self.siniflar = siniflar
		self.dolu_kontenjan = dolu_kontenjan
		self.kontenjan = kontenjan
		self.alabilen = alabilen

	def yazdir(self):
		print(f'CRN = {self.crn}\nAd = {self.ad}\nHoca = {self.hoca}\nBinalar = {self.binalar}\nGünler = {self.gunler}\nSaatler = {self.saatler}\nSınıflar = {self.siniflar}\nKontenjan = {self.dolu_kontenjan}/{self.kontenjan}\nAlabilen bölümler = {self.alabilen}')

class DersListe:
	def __init__(self, dersler, crnler, adlar, hocalar):
		self.dersler = dersler
		self.crnler = crnler
		self.adlar = adlar
		self.hocalar = hocalar

	def liste_yazdir(self):
		for _ders in self.dersler:
			_ders.yazdir()
