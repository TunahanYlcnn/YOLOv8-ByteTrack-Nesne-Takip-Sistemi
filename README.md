# 🚀 YOLOv8 & ByteTrack: Yüksek Performanslı Nesne Takip Sistemi

Bu proje, **YOLOv8**'in güçlü nesne tespit yeteneklerini, nesne takip dünyasında devrim yaratan **ByteTrack** algoritması ile birleştirir. Standart takipçilerin aksine ByteTrack, her tespit kutusunu (detection box) değerlendirerek, nesnelerin birbirini kapattığı veya görüntüden kısa süreli çıktığı durumlarda dahi takibin sürekliliğini sağlar.

---

## 🧠 ByteTrack Algoritması Nedir?

ByteTrack, "Tracking-by-Detection" felsefesini **BYTE** (Tracking by Associating Every detection box) veri ilişkilendirme yöntemiyle optimize eder. 

*   **Birinci Derece İlişkilendirme:** Yüksek güven skoruna sahip tespitler, mevcut takip yollarıyla (tracklets) eşleştirilir.
*   **İkinci Derece İlişkilendirme:** İlk aşamada eşleşmeyen düşük skorlu kutular, "gerçekten bir nesne mi yoksa gürültü mü" olduklarını anlamak için $IoU$ (Intersection over Union) benzerliği üzerinden tekrar değerlendirilir.

Matematiksel olarak eşleşme skoru şu şekilde optimize edilir:
$$Similarity = \alpha \cdot IoU(D, T) + (1 - \alpha) \cdot Appearance(D, T)$$

---

## 🛠️ Teknik Özellikler

*   **Düşük Güven Skorlu Takip:** Düşük ışık veya yarı-kapalı (partial occlusion) durumlarda takibi bırakmaz.
*   **Hız ve Verimlilik:** YOLOv8'in hafif modelleri (n/s) ile gerçek zamanlı (FPS) performans sağlar.
*   **Kimlik Koruma:** Nesnelerin ID'lerini uzun süre boyunca sabit tutar, ID switch (kimlik değişimi) hatalarını minimize eder.

---

## 📋 Gereksinimler

### ⚙️ Kurulum ve Kullanım (Sıfırdan Hazırlık)
Sistemi bilgisayarında en temelden ayağa kaldırmak için şu adımları izle:
1. Depoyu Klonla:
```bash
git clone [https://github.com/TunahanYlcnn/YOLOv8-ByteTrack-Nesne-Takip-Sistemi.git](https://github.com/TunahanYlcnn/YOLOv8-ByteTrack-Nesne-Takip-Sistemi.git)
cd YOLOv8-ByteTrack-Nesne-Takip-Sistemi
```
2. Projenin çalışması için gerekli kütüphaneleri şu komutla yükleyebilirsin:
```bash
pip install ultralytics opencv-python numpy
```
