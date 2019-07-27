import ders_class as ders
import gun_class as gun
import ders_programi_gui as dp_gui
import random

#tüm ders kodlarını çeker
def ders_kodlarini_cek():
	f = open("veritabani/ders_kodlari.txt", "r")
	ders_kodlari = f.read()
	ders_kodlari = ders_kodlari.split("\n")
	ders_kodlari.pop()
	f.close()

	return ders_kodlari

#tüm ders adlarını çeker
def ders_adlarini_cek():
	ders_kodlari = ders_kodlarini_cek()
	ders_adlari = []

	for kod in ders_kodlari:
		f = open(f"veritabani/dersler/{kod}.txt", "r")

		while(True):
			bilgi_satir = f.readline()
			if bilgi_satir == "\n" or bilgi_satir == "" or bilgi_satir == None or bilgi_satir == " " or len(bilgi_satir) == 0:
				break
			else:
				ders_bilgisi = bilgi_satir.split(";")
				if not ders_bilgisi[1] in ders_adlari:
					ders_adlari.append(ders_bilgisi[1])
		f.close()

	return ders_adlari

#tüm dersleri çeker
def dersleri_cek():
	dersler = ders.DersListe([], [], [], [])

	ders_kodlari = ders_kodlarini_cek()

	for kod in ders_kodlari:
		f = open(f"veritabani/dersler/{kod}.txt", "r")

		while(True):
			bilgi_satir = f.readline()
			if bilgi_satir == "\n" or bilgi_satir == "" or bilgi_satir == None or bilgi_satir == " " or len(bilgi_satir) == 0:
				break
			else:
				ders_bilgisi = bilgi_satir.split(";")
				yeni_ders = ders.Ders(ders_bilgisi[0], ders_bilgisi[1], ders_bilgisi[2], ders_bilgisi[4], ders_bilgisi[5], ders_bilgisi[6], ders_bilgisi[3], ders_bilgisi[7])
				dersler.dersler.append(yeni_ders)
				dersler.crnler.append(ders_bilgisi[0])
				dersler.adlar.append(ders_bilgisi[1])
				dersler.hocalar.append(ders_bilgisi[2])
		f.close()	

	return dersler

#yalnızca kodu verilen dersleri çeker
def ders_cek(ders_kodu):
	f = open(f"veritabani/dersler/{ders_kodu}.txt", "r")

	dersler = ders.DersListe([], [], [], [])

	while(True):
		bilgi_satir = f.readline()
		if bilgi_satir == "\n" or bilgi_satir == "" or bilgi_satir == None or bilgi_satir == " " or len(bilgi_satir) == 0:
			break
		else:
			ders_bilgisi = bilgi_satir.split(";")
			yeni_ders = ders.Ders(ders_bilgisi[0], ders_bilgisi[1], ders_bilgisi[2], ders_bilgisi[4], ders_bilgisi[5], ders_bilgisi[6], ders_bilgisi[3], ders_bilgisi[7])
			dersler.dersler.append(yeni_ders)
			dersler.crnler.append(ders_bilgisi[0])
			dersler.adlar.append(ders_bilgisi[1])
			dersler.hocalar.append(ders_bilgisi[2])
	f.close()

	return dersler

#adı verilen dersin hocalarını çeker
def ders_hocalarini_cek(ders_adi):
	ders_kodu = ders_adi.split(" ")[0]
	hocalar = []

	dersler = ders_cek(ders_kodu)
	for hoca, ad in zip(dersler.hocalar, dersler.adlar):
		if ad == ders_adi:
			if not hoca in hocalar:
				if not hoca == "--":
					hocalar.append(hoca)

	return hocalar

def hash_olustur(dersler):
	crnler = []
	hash_ = ""

	for _ders in dersler:
		crnler.append(int(_ders.crn))

	crnler.sort()

	for crn in crnler:
		hash_ = hash_ + str(crn)

	return hash_

def hash_kontrol(hashler, yeni_hash):
	return (yeni_hash in hashler)

def karistir(liste):
	random.shuffle(liste)
	return liste

def ayirma(ayrilacak): 
	table = ayrilacak.maketrans(" ", " ", "[]' ")
	_ayrilacak = ayrilacak.translate(table)
	if "," in ayrilacak:
		_ayrilacak = _ayrilacak.split(",")
	return _ayrilacak

def crn_kontrol(crn_liste, dersler):
	ayiklanmis_dersler = []

	for _ders in dersler:
		if _ders.crn in crn_liste:
			ayiklanmis_dersler.append(_ders)

def hoca_kontrol(hoca_liste, dersler):
	ayiklanmis_dersler = []
	ders_adi_karaliste = []

	for _ders in dersler:
		if _ders.hoca in hoca_liste:
			if not _ders.ad in ders_adi_karaliste:
				ders_adi_karaliste.append(_ders.ad)

	for _ders in dersler:
		if (_ders.ad not in ders_adi_karaliste) or (_ders.hoca in hoca_liste):
			ayiklanmis_dersler.append(_ders)

	#print("Hoca kontrol yapıldı. Ayıklanmış dersler: ")
	#ayiklanmis_dersler.liste_yazdir()

	return ayiklanmis_dersler

def tek_ders_hoca_eleme(hoca_adi, dersler):
	
	if hoca_adi == "Herhangi bir hoca":
		return dersler
	else:
		ayiklanmis_dersler = []

		for _ders in dersler:
			if _ders.hoca == hoca_adi:
				ayiklanmis_dersler.append(_ders)

		return ayiklanmis_dersler
	
def gun_bos_birakma(gun, dersler):
	ayiklanmis_dersler = []

	for _ders in dersler:
		if not gun.upper() in _ders.gunler.upper():
			ayiklanmis_dersler.append(_ders)

	return ayiklanmis_dersler

def program_olustur(bolum, dersler, app = None):
	try:
		pzt = gun.Gun("Pazartesi")
		sali = gun.Gun("Salı")
		crs = gun.Gun("Çarşamba")
		prs = gun.Gun("Perşembe")
		cuma = gun.Gun("Cuma")
		
		gunler = [pzt, sali, crs, prs, cuma]
		gun_adlari = [pzt.ad, sali.ad, crs.ad, prs.ad, cuma.ad]

		if app == None:
			ex = dp_gui.DersProgramGUI(gunler)
			app = ex.get_GUI_app()

		eklenen_dersler = ders.DersListe([], [], [], [])
		istenen_ders_adlari = []
		hashler = []

		for _ders in dersler:
			if not _ders.ad in istenen_ders_adlari:
				istenen_ders_adlari.append(_ders.ad)

		_dersler = app.gunleriAyikla(dersler)

		for _ders in _dersler:
			alabilir = False

			if bolum == "":
				alabilir = True
			elif not _ders.alabilen == "['Tüm Lisans ve Lisansüstü Programlar']":
				alabilen_bolumler = ayirma(_ders.alabilen)
				if bolum.upper() in alabilen_bolumler:
					alabilir = True
			else:
				alabilir = True

			if alabilir:	
				if _ders.ad in eklenen_dersler.adlar:
					continue
				else:			
					onay = True
					_gunler = ayirma(_ders.gunler)
					_saatler = ayirma(_ders.saatler)
					print(f"günler {_gunler} saatler {_saatler}")
					for i in range(len(_saatler)):
						_gun_index = gun_adlari.index(_gunler[i])
						onay = (gunler[_gun_index].saate_ders_ekle(_saatler[i], _ders) & onay)

					if not onay:
						for i in range(len(_saatler)):
							_gun_index = gun_adlari.index(_gunler[i])
							_ayrik_saatler = _saatler[i].split("/")
							_saat_skala = list(range(int(_ayrik_saatler[0]) // 100, int(_ayrik_saatler[1]) // 100))
							for j in range(len(gunler[_gun_index].saatler)):
								if gunler[_gun_index].saatler[j].saat in _saat_skala:							
									if gunler[_gun_index].saatler[j].ders == _ders.ad:
										gunler[_gun_index].saatten_dersi_kaldir(_saatler[i], _ders)
					else:
						eklenen_dersler.dersler.append(_ders)
						eklenen_dersler.adlar.append(_ders.ad)
						eklenen_dersler.crnler.append(_ders.crn)
						eklenen_dersler.hocalar.append(_ders.hoca)
						
						print(f"eklenen dersler {eklenen_dersler.adlar}")

		if (len(istenen_ders_adlari) > len(eklenen_dersler.dersler)):
			print(f'istenen_ders_adlari: {istenen_ders_adlari}, eklenen_dersler.dersler: {eklenen_dersler.dersler}')
			dersler = karistir(dersler)
			program_olustur(bolum, dersler, app = app)

		else:
			for _ders in eklenen_dersler.dersler:
				_ders.yazdir()

			#programi_yazdir(gunler)

			if not hash_kontrol(hashler, hash_olustur(eklenen_dersler.dersler)):
				hashler.append(hash_olustur(eklenen_dersler.dersler))			
				app.tabloyuDoldur(gunler)				
			else:
				dersler = karistir(dersler)
				program_olustur(bolum, dersler, app = app)

		return eklenen_dersler.dersler
		
	except RecursionError:
		dp_gui.popup_olustur('Girilen dersler ile program oluşturulamıyor!', 'Tamam')
		return None

def programi_yazdir(gunler):
	ders_programi = [["" for i in range(len(gunler[0].saatler))] for j in range(len(gunler))]

	for i in range(len(gunler)):
		for j in range(len(gunler[i].saatler)):
			ders_programi[i][j] = gunler[i].saatler[j].ders

	for i in range(len(gunler)):
		print(f"--------{gunler[i].ad}--------")
		for j in range(len(gunler[i].saatler)):
			print(f"{gunler[i].saatler[j].saat}:30 : {ders_programi[i][j]}")
		print("\n")
