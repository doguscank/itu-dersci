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
				yeni_ders = ders.Ders(ders_bilgisi[0], ders_bilgisi[1], ders_bilgisi[2], ders_bilgisi[5], ders_bilgisi[6], ders_bilgisi[7], ders_bilgisi[3], ders_bilgisi[4], ders_bilgisi[8], ders_bilgisi[9])
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
			yeni_ders = ders.Ders(ders_bilgisi[0], ders_bilgisi[1], ders_bilgisi[2], ders_bilgisi[5], ders_bilgisi[6], ders_bilgisi[7], ders_bilgisi[3], ders_bilgisi[4], ders_bilgisi[8], ders_bilgisi[9])
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

def binalari_cek():
	ders_kodlari = ders_kodlarini_cek()
	bina_adlari = []

	for kod in ders_kodlari:
		f = open(f"veritabani/dersler/{kod}.txt", "r")

		while(True):
			bilgi_satir = f.readline()
			if bilgi_satir == "\n" or bilgi_satir == "" or bilgi_satir == None or bilgi_satir == " " or len(bilgi_satir) == 0:
				break
			else:
				ders_bilgisi = bilgi_satir.split(";")
				if ',' in ders_bilgisi[8]:
					bina_bilgileri = ayirma(ders_bilgisi[8])
					for bilgi in bina_bilgileri:
						if not bilgi in bina_adlari:
							bina_adlari.append(bilgi)
				else:
					bina_bilgisi = ayirma(ders_bilgisi[8])
					if not bina_bilgisi in bina_adlari:
						bina_adlari.append(bina_bilgisi)
		f.close()

	bina_adlari.sort()
	return bina_adlari

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
	table = ayrilacak.maketrans(" ", " ", "[]\n' ")
	_ayrilacak = ayrilacak.translate(table)
	if "," in ayrilacak:
		_ayrilacak = _ayrilacak.split(",")
	return _ayrilacak

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

def crn_kontrol(crnler):
	tum_dersler = dersleri_cek()
	ders_sonuc, ders_sonuc_ad = [], []

	if len(crnler) > 0:
		for _ders in tum_dersler.dersler:
			if _ders.crn in crnler:
				ders_sonuc.append(_ders)
				ders_sonuc_ad.append(_ders.ad)
	return ders_sonuc, ders_sonuc_ad

def kampus_secme(dersler, kampus_index):
	ayazaga = ['DEP', 'BEB', 'DMB', 'EEB', 'FEB', 'GDB', 'HVZ', 'INB', 'KSB', 'KMB', 'KORT', 'MED', 'MEDB', 'MDB', 'MOB', 'PYB', 'RSLN-M', 'SLN-M', 'SDKM', 'SMB', 'STD', 'SYM', 'UUB', 'UZEM', 'YDB', 'MOBGAM', 'ENB', 'HLB']
	macka = ['DIB', 'ISB', 'TMB']
	tuzla = ['DZB']
	gumussuyu = ['MKB', 'SLN-G']
	taskisla = ['MMB']

	kampusler = [ayazaga, macka, tuzla, gumussuyu, taskisla]
	kampus_alinabilir, dersler_gonderilecek = [], []

	for i in range(len(kampusler)):
		if i in kampus_index:
			kampus_alinabilir.append(kampusler[i])

	for _ders in dersler:
		for kampus in kampus_alinabilir:
			binalar = ayirma(_ders.binalar)
			if isinstance(binalar, str):
				if binalar in kampus:
					dersler_gonderilecek.append(_ders)
					break
			else:
				for bina in binalar:
					if bina in kampus:
						dersler_gonderilecek.append(_ders)
						break

	return dersler_gonderilecek

def program_olustur(bolum, dersler, app = None, kontenjan = False):
	try:
		pzt = gun.Gun("Pazartesi")
		sali = gun.Gun("Sali")
		crs = gun.Gun("Carsamba")
		prs = gun.Gun("Persembe")
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
		_dersler = app.kampusleriAyikla(_dersler)

		for _ders in _dersler:				

			alabilir = False

			if bolum == "":
				alabilir = True
			elif " " in bolum:
				bolumler = bolum.split(" ")
				alabilen_bolumler = ayirma(_ders.alabilen)
				for _bolum in bolumler:
					if _bolum.upper() in alabilen_bolumler:
						alabilir = True
						break
			elif not "Tum Lisans ve Lisansustu Programlar" in _ders.alabilen:
				alabilen_bolumler = ayirma(_ders.alabilen)
				if bolum.upper() in alabilen_bolumler:
					alabilir = True
			else:
				alabilir = True

			if kontenjan:
				alabilir = alabilir & (int(_ders.dolu_kontenjan) < int(_ders.kontenjan))

			if alabilir:	
				if _ders.ad in eklenen_dersler.adlar:
					continue
				else:			
					onay = True
					_gunler = ayirma(_ders.gunler)
					_saatler = ayirma(_ders.saatler)
					#print(f"günler {_gunler} saatler {_saatler}")
					if isinstance(_gunler, str):						
						_gun_index = gun_adlari.index(_gunler)
						onay = (gunler[_gun_index].saate_ders_ekle(_saatler, _ders) & onay)
					else:
						for i in range(len(_saatler)):	
							_gun_index = gun_adlari.index(_gunler[i])
							onay = (gunler[_gun_index].saate_ders_ekle(_saatler[i], _ders) & onay)					

					if not onay:
						for i in range(len(_saatler)):
							if isinstance(_gunler, str):
								_gun_index = gun_adlari.index(_gunler)
							else:		
								_gun_index = gun_adlari.index(_gunler[i])
							if len(_saatler) == 9:
								_ayrik_saatler = _saatler.split("/")
							else:								
								_ayrik_saatler = _saatler[i].split("/")
							#print(_ayrik_saatler)
							_saat_skala = list(range(int(_ayrik_saatler[0]) // 100, int(_ayrik_saatler[1]) // 100))
							for j in range(len(gunler[_gun_index].saatler)):
								if gunler[_gun_index].saatler[j].saat in _saat_skala:							
									if gunler[_gun_index].saatler[j].ders == _ders.ad:
										if len(_saatler) == 9:
											gunler[_gun_index].saatten_dersi_kaldir(_saatler, _ders)
										else:
											gunler[_gun_index].saatten_dersi_kaldir(_saatler[i], _ders)
					else:
						eklenen_dersler.dersler.append(_ders)
						eklenen_dersler.adlar.append(_ders.ad)
						eklenen_dersler.crnler.append(_ders.crn)
						eklenen_dersler.hocalar.append(_ders.hoca)
						
						#print(f"eklenen dersler {eklenen_dersler.adlar}")

		if (len(istenen_ders_adlari) > len(eklenen_dersler.dersler)):
			#print(f'istenen_ders_adlari: {istenen_ders_adlari}, eklenen_dersler.dersler: {eklenen_dersler.dersler}')
			dersler = karistir(dersler)
			return program_olustur(bolum, dersler, app = app, kontenjan = kontenjan)

		else:
			for _ders in eklenen_dersler.dersler:
				_ders.yazdir()

			#programi_yazdir(gunler)

			if not hash_kontrol(hashler, hash_olustur(eklenen_dersler.dersler)):
				hashler.append(hash_olustur(eklenen_dersler.dersler))			
				app.tabloyuDoldur(gunler)
				return (eklenen_dersler.dersler, len(istenen_ders_adlari))				
			else:
				dersler = karistir(dersler)
				return program_olustur(bolum, dersler, app = app, kontenjan = kontenjan)		
		
	except RecursionError:		
		dp_gui.popup_olustur('Girilen dersler ile program oluşturulamıyor!', 'Tamam', 'Program')
		return (None, None)

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
