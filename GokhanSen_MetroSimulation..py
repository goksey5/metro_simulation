from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        kuyruk = deque([(baslangic, [baslangic])])
        ziyaret_edildi = {baslangic}
        
        while kuyruk:
            current, path = kuyruk.popleft()
            
            if current == hedef:
                return path
                
            for komsu, _ in current.komsular:
                if komsu not in ziyaret_edildi:
                    ziyaret_edildi.add(komsu)
                    yeni_rota = path + [komsu]
                    kuyruk.append((komsu, yeni_rota))
        
        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        pq = [(0, id(baslangic), baslangic, [baslangic])]
        ziyaret_edildi = set()
        mesafeler = {baslangic: 0}
        
        while pq:
            toplam_sure, _, current, path = heapq.heappop(pq)
            
            if current == hedef:
                return (path, toplam_sure)
                
            if current in ziyaret_edildi:
                continue
                
            ziyaret_edildi.add(current)
            
            for komsu, sure in current.komsular:
                if komsu not in ziyaret_edildi:
                    yeni_sure = toplam_sure + sure
                    if komsu.hat != current.hat:
                        yeni_sure += 5
                    
                    if komsu not in mesafeler or yeni_sure < mesafeler[komsu]:
                        mesafeler[komsu] = yeni_sure
                        yeni_rota = path + [komsu]
                        heapq.heappush(pq, (yeni_sure, id(komsu), komsu, yeni_rota))
        
        return None

if __name__ == "__main__":
    metro = MetroAgi()
    
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)
    metro.baglanti_ekle("K2", "K3", 6)
    metro.baglanti_ekle("K3", "K4", 8)
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)
    metro.baglanti_ekle("M2", "M3", 3)
    metro.baglanti_ekle("M3", "M4", 4)
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)
    metro.baglanti_ekle("T2", "T3", 9)
    metro.baglanti_ekle("T3", "T4", 5)
    
    # Hat aktarma bağlantıları
    metro.baglanti_ekle("K1", "M2", 2)
    metro.baglanti_ekle("K3", "T2", 3)
    metro.baglanti_ekle("M4", "T3", 2)
    
    print("\n=== Test Senaryoları ===")
    
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

            # Yeni hat ve istasyonlar ekleyelim (Yeşil Hat)
    print("\n=== Yeni Hat ve İstasyonlar Ekleniyor ===")
    metro.istasyon_ekle("Y1", "Sincan", "Yeşil Hat")
    metro.istasyon_ekle("Y2", "Eryaman", "Yeşil Hat")
    metro.istasyon_ekle("Y3", "Batıkent", "Yeşil Hat")  # Aktarma noktası
    metro.istasyon_ekle("Y4", "Macunköy", "Yeşil Hat")
    
    # Yeşil Hat bağlantıları
    metro.baglanti_ekle("Y1", "Y2", 6)
    metro.baglanti_ekle("Y2", "Y3", 5)
    metro.baglanti_ekle("Y3", "Y4", 4)
    
    # Aktarma bağlantısı
    metro.baglanti_ekle("Y3", "T1", 3)  # Batıkent aktarma
    
    print("\n=== Yeni Test Senaryoları ===")
    
    # Test 4: Sincan'dan Keçiören'e
    print("\n4. Sincan'dan Keçiören'e:")
    try:
        rota = metro.en_az_aktarma_bul("Y1", "T4")
        if rota:
            print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
        else:
            print("Rota bulunamadı!")
        
        sonuc = metro.en_hizli_rota_bul("Y1", "T4")
        if sonuc:
            rota, sure = sonuc
            print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
        else:
            print("Rota bulunamadı!")
    except Exception as e:
        print(f"Hata oluştu: {e}")
    
    # Test 5: Macunköy'den AŞTİ'ye
    print("\n5. Macunköy'den AŞTİ'ye:")
    try:
        rota = metro.en_az_aktarma_bul("Y4", "M1")
        if rota:
            print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
        else:
            print("Rota bulunamadı!")
        
        sonuc = metro.en_hizli_rota_bul("Y4", "M1")
        if sonuc:
            rota, sure = sonuc
            print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
        else:
            print("Rota bulunamadı!")
    except Exception as e:
        print(f"Hata oluştu: {e}")
    
    # İstatistik bilgileri
    print("\n=== Metro Ağı İstatistikleri ===")
    print(f"Toplam istasyon sayısı: {len(metro.istasyonlar)}")
    print("Hat başına istasyon sayısı:")
    for hat, istasyonlar in metro.hatlar.items():
        print(f"- {hat}: {len(istasyonlar)} istasyon")
    
    # En uzun hat bulma
    en_uzun_hat = max(metro.hatlar.items(), key=lambda x: len(x[1]))
    print(f"\nEn uzun hat: {en_uzun_hat[0]} ({len(en_uzun_hat[1])} istasyon)")
    
    # Aktarma noktalarını bulma
    aktarma_noktalari = set()
    for istasyon in metro.istasyonlar.values():
        komsu_hatlar = {komsu[0].hat for komsu in istasyon.komsular}
        if len(komsu_hatlar) > 1:
            aktarma_noktalari.add(istasyon.ad)
    
    print("\nAktarma noktaları:")
    for nokta in sorted(aktarma_noktalari):
        print(f"- {nokta}")
    
    # Performans testi
    print("\n=== Performans Testi ===")
    import time
    
    baslangic = time.time()
    for _ in range(100):
        metro.en_hizli_rota_bul("Y1", "M1")
    bitis = time.time()
    print(f"100 rota hesaplama süresi: {bitis - baslangic:.3f} saniye")