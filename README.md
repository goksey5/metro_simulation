# metro_simulation




# GokhanSen_MetroSimulation.

# Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)

## Proje Açıklaması
Bu proje, bir metro ağında istasyonlar arası en hızlı ve en az aktarmalı rotaları bulan bir simülasyon sistemidir. Sistem, farklı metro hatlarını, aktarma noktalarını ve seyahat sürelerini dikkate alarak optimum rotayı hesaplar.

## Kullanılan Teknolojiler ve Kütüphaneler

### collections
- `defaultdict`: Hat bilgilerini tutmak için kullanılan varsayılan değerli sözlük yapısı
- `deque`: BFS algoritması için kuyruk veri yapısı (First-In-First-Out prensibi)

### heapq
- Öncelik kuyruğu implementasyonu
- A* algoritmasında en düşük maliyetli yolu bulmak için kullanılır

### typing
- `Dict`: Sözlük tip tanımlamaları
- `List`: Liste tip tanımlamaları
- `Set`: Küme tip tanımlamaları
- `Tuple`: Demet tip tanımlamaları
- `Optional`: Opsiyonel dönüş değerleri için tip tanımlaması

## Algoritmaların Çalışma Mantığı

### BFS (Breadth-First Search) Algoritması
```python
def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str)
```
- Genişlik öncelikli arama yapar
- Her seviyeyi sırayla kontrol eder
- En kısa yolu (en az aktarmalı) garantiler
- Zaman karmaşıklığı: O(V + E) (V: düğüm sayısı, E: kenar sayısı)

Neden BFS?
- En az aktarma için ideal
- Her seviyeyi eşit şekilde kontrol eder
- İlk bulunan yol en az aktarmalı yoldur

### A* Algoritması
```python
def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str)
```
- Hedefe yönelik akıllı arama yapar
- Maliyet (süre) ve hedef tahmini kullanır
- En kısa süreyi garantiler
- Zaman karmaşıklığı: O(E log V)

Neden A*?
- En hızlı rotayı bulmak için optimal
- Hedef odaklı arama yapar
- Gereksiz yolları elemede etkili

## Örnek Kullanım ve Test Sonuçları

### Temel Kullanım
```python
metro = MetroAgi()
metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
metro.baglanti_ekle("K1", "K2", 4)

# En az aktarmalı rota bulma
rota = metro.en_az_aktarma_bul("M1", "K4")

# En hızlı rota bulma
sonuc = metro.en_hizli_rota_bul("M1", "K4")
```

### Test Sonuçları
=== Test Senaryoları ===

1. AŞTİ'den OSB'ye:
En az aktarmalı rota: AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
En hızlı rota (30 dakika): AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB

2. Batıkent'ten Keçiören'e:
En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören

3. Keçiören'den AŞTİ'ye:
En az aktarmalı rota: Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
En hızlı rota (24 dakika): Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ

=== Yeni Hat ve İstasyonlar Ekleniyor ===

=== Yeni Test Senaryoları ===

4. Sincan'dan Keçiören'e:
En az aktarmalı rota: Sincan -> Eryaman -> Batıkent -> Batıkent -> Demetevler -> Gar -> Keçiören
En hızlı rota (40 dakika): Sincan -> Eryaman -> Batıkent -> Batıkent -> Demetevler -> Gar -> Keçiören

5. Macunköy'den AŞTİ'ye:
En az aktarmalı rota: Macunköy -> Batıkent -> Batıkent -> Demetevler -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
En hızlı rota (47 dakika): Macunköy -> Batıkent -> Batıkent -> Demetevler -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ

=== Metro Ağı İstatistikleri ===
Toplam istasyon sayısı: 16
Hat başına istasyon sayısı:
- Kırmızı Hat: 4 istasyon
- Mavi Hat: 4 istasyon
- Turuncu Hat: 4 istasyon
- Yeşil Hat: 4 istasyon

En uzun hat: Kırmızı Hat (4 istasyon)

Aktarma noktaları:
- Batıkent
- Demetevler
- Gar
- Kızılay

=== Performans Testi ===
100 rota hesaplama süresi: 0.000 saniye
### İstatistikler
- Toplam İstasyon Sayısı
- Hat Başına İstasyon Sayısı
- Aktarma Noktaları
- Performans Metrikleri

## Projeyi Geliştirme Fikirleri

1. Görselleştirme
   - Metro ağı haritası
   - Rota animasyonu
   - Gerçek zamanlı simülasyon

2. Ek Özellikler
   - Yoğunluk analizi
   - Sefer zamanları
   - Alternatif rota önerileri
   - Bakım/Arıza senaryoları

3. Optimizasyonlar
   - Paralel hesaplama
   - Önbellek mekanizması
   - Dinamik rota güncelleme

4. Kullanıcı Arayüzü
   - Web arayüzü
   - Mobil uygulama
   - Gerçek zamanlı güncelleme

5. Veri Analizi
   - Yolcu istatistikleri
   - Hat verimliliği
   - Zirve saat analizi


