# 🎯 YOLOv8 + ByteTrack Nesne Takip Sistemi

Bu proje, yüksek performanslı **YOLOv8** nesne algılama modelini ve **ByteTrack** veri ilişkilendirme algoritmasını kullanarak videolardaki nesneleri benzersiz kimliklerle (ID) takip eder.

## 🚀 Özellikler
* **GPU Hızlandırma:** `CUDA` desteği ile gerçek zamanlıya yakın işleme hızı.
* **Akıllı Takip:** ByteTrack sayesinde nesnelerin önüne engel çıksa dahi takibi sürdürme kabiliyeti.
* **Hedef Kilitleme:** Belirlenen bir ID'ye odaklanarak sadece o nesneyi görselleştirme.

## 🛠️ Kurulum
1. Gerekli Python kütüphanelerini yükleyin:
   ```bash
   pip install ultralytics opencv-python numpy