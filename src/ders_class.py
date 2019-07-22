class Ders:
	def __init__(self, crn, ad, hoca, gunler, saatler, siniflar, kontenjan, alabilen):
		self.crn = crn
		self.ad = ad
		self.hoca = hoca
		self.gunler = gunler
		self.saatler = saatler
		self.siniflar = siniflar
		self.kontenjan = kontenjan
		self.alabilen = alabilen

	def yazdir(self):
		print(f'CRN = {self.crn}\nAd = {self.ad}\nHoca = {self.hoca}\nGünler = {self.gunler}\nSaatler = {self.saatler}\nSınıflar = {self.siniflar}\nKontejan = {self.kontenjan}\nAlabilen bölümler = {self.alabilen}')

class DersListe:
	def __init__(self, dersler, crnler, adlar, hocalar):
		self.dersler = dersler
		self.crnler = crnler
		self.adlar = adlar
		self.hocalar = hocalar

	def liste_yazdir(self):
		for _ders in self.dersler:
			_ders.yazdir()
