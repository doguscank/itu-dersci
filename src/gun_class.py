import ders_class

class Gun:
	def __init__(self, ad):
		self.ad = ad
		self.saatler = [Saat(8,""), Saat(9,""), Saat(10,""), Saat(11,""), Saat(12,""), Saat(13,""), Saat(14,""), Saat(15,""), Saat(16,""), Saat(17,""), Saat(18,"")]

	def saate_ders_ekle(self, saat_araligi, ders):
		_saatler = saat_araligi.split("/")
		saat_bas = int(_saatler[0]) // 100
		saat_son = int(_saatler[1]) // 100
		saat_skala = list(range(saat_bas, saat_son))
		ders_eklenebilir = True

		for j in range(len(self.saatler)):
			if self.saatler[j].saat in saat_skala:
				if not self.saatler[j].ders == "":
					ders_eklenebilir = False
		
		if ders_eklenebilir:
			for i in range(len(self.saatler)):		
				if self.saatler[i].saat in saat_skala:
					self.saatler[i].ders = ders.ad
					
		return ders_eklenebilir

	def saatten_dersi_kaldir(self, saat_araligi, ders):
		_saatler = saat_araligi.split("/")
		saat_bas = int(_saatler[0]) // 100
		saat_son = int(_saatler[1]) // 100
		saat_skala = list(range(saat_bas, saat_son))
		ders_kaldirilabilir = False

		for j in range(len(self.saatler)):
			if self.saatler[j].saat in saat_skala:
				if self.saatler[j].ders != "":
					ders_kaldirilabilir = True

		if ders_kaldirilabilir:
			for i in range(len(self.saatler)):		
				if self.saatler[i].saat in saat_skala:
					self.saatler[i].ders = ""

		return ders_kaldirilabilir

class Saat:
	def __init__(self, saat, ders):
		self.saat = saat
		self.ders = ders