# Otomatik Ders Programı Hazırlama Programı
Program asıl olarak iki alt programdan oluşmaktadır. Bunlar "Programcı" ve "Alternatif CRNci"dir.
- Programcı, seçilen dersleri çeşitli filtrelemelerden geçirerek otomatik ders programı oluşturan bir yazılımdır.
- Alternatif CRNci ise verilen CRNler ile aynı gün aynı saatte bulunan derslerin CRNlerini gösterir. Kontenjan filtresi kullanılarak kontenjanı dolmuş dersleri elemenizi kolaylaştırır.

## Programcı'nın Özellikleri
- Bölüme göre filtreleme
- Kampüse göre filtreleme
- Gün boş bırakma
- CRN girerek spesifik ders ekleme
- Programdaki dersleri metin belgesine kaydetme

## Alternatif CRNci'nin Özellikleri
- Girilen CRN'deki ders ile aynı gün ve saatte bulunan dersleri getirme
- Kontenjana göre alternatif ders getirme

## Kontenjancı'nın özellikleri
- Girilen CRN'nin kontenjanını istediğimiz sıklıkta kontrol eder
- Kontenjanda boşluk olması halinde cihazlarımıza bildirim gönderir

## Programı Python ile Çalıştırmak İçin Gerekli Kütüphaneler
- Minimum Python 3.6
- PyQt5
- BeautifulSoup4
- urllib3
- Notify (Kontenjancı için)

**Not:** Programların .exe hallerini kullansanız bile Notify kütüphanesini yüklemeniz gerekmekte.

## Programın Kullanımı
Programcı için hub.py dosyasını Python ile çalıştırın. Ardından karşınıza iki adet seçenek gelecek. Programcı veya Alternatif CRNci programlarından istediğinizi seçin.

Kontenjancı için ise Python ile önce notify.py dosyasını, ardından kontenjanci.py dosyasını çalıştırın.

#### Programcı'nın Kullanımı
Öncelikle en üstteki **Ayarlar** kısmından veritabanını güncelliyoruz. Veritabanı güncellemesi internet hızınıza bağlı olarak bir kaç dakika sürebilir. Ardından ekrana gelen "Veritabanı güncellendi" uyarısını kapatıyoruz. Sol üst köşedeki bölüm kodu girme yerine **bölüm kodumuzu** giriyoruz. Program oluşturulurken kontenjanlara dikkat edilmesini istiyorsak kutucuğu işaretliyoruz. İstediğimiz kampüs varsa kampüs seçiyor, boş bırakmak istediğimiz gün varsa boş bırakmak istediğimiz günleri seçiyoruz. Ardından almak istediğimiz spesifik bir ders varsa CRN'sini giriyoruz. ***Ders ekle*** butonuna basıp ilk dersimizi ekliyoruz. Ders kodunu seçiyoruz ve ardından istediğimiz dersi seçiyoruz. İsteğe bağlı hoca seçimi yapıyoruz. İstediğimiz dersleri bu şekilde seçtikten sonra ***Program Oluştur*** butonuna basıyoruz ve programımız oluşturulmaya **çalışılıyor**. Eğer program oluşturulamazsa ekranda bir hata pop-up'ı beliriyor. Hatalı dersleri yanındaki **sil** butonuna basarak çıkarıp programı tekrar oluşturuyoruz. Oluşturduğunuz programı isterseniz kaydedebilir, isterseniz kendiniz not alabilirsiniz. Kayıtlı programlar ***kayitlar*** klasörünün içindeki ***kayitli_programlar.txt*** belgesinin içindedir.

#### Alternatif CRNci'nin Kullanımı
Programın da belirttiği gibi CRN'lerimizi virgül ile ayırarak yazıyoruz. Getirilecek alternatiflerin kontenjanları önemli ise işaretleme kutusunu işaretliyoruz. Ardından ***Alternatif Getir*** butonuna basıyoruz. Alternatif CRNler programımızda gözükecektir. İsteğe bağlı olarak ***Alternatifleri Kaydet*** butonuna basarak alternatif CRNleri kaydediyoruz. Kayıtlı CRNler ***kayitlar*** klasörünün içerisindeki ***alternatif_crnler.txt*** belgesinin içindedir.

#### Kontenjancı'nın Kullanımı
Programı çalıştırmadan önce ***Configure Notify*** programını çalıştırıyoruz. Ardından oluşan ***config.txt*** dosyasını açıp **To subscribe, open:** kısmındaki linki, bildirim almak istediğimiz cihazın **anlık bildirimleri destekleyen bir tarayıcısından** açıyoruz. Sayfanın alt kısmındaki **Add Subscription** kısmındaki **Subscribe on this device** butonuna çift tıklıyoruz. Ekrana gelen pencereden **anlık bildirimlere izin ver** diyoruz. Konfigürasyon kısmı böylelikle bitiyor. Şimdi **Kontenjanci.exe** dosyasını açıp istediğimiz CRNleri giriyoruz. Alt kısma ise kaç saniyede bir veritabanını güncellemesini istediğimizi giriyoruz. Programı başlattıktan sonra kontenjanda boş yer var ise 15 saniyede bir toplamda 10 adet bildirim cihazlarımıza iletilecek.
