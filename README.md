🛰️ Ağ Haritası Tarayıcı (Network Topology Visualizer)

Bu proje, yerel ağda bulunan cihazları otomatik olarak tespit edip, onların IP, MAC, Hostname ve üretici bilgilerini listeleyen ve ağ haritasını .png formatında görsel olarak sunan bir Python uygulamasıdır.

🚀 Özellikler

- IP aralığını vererek tüm ağdaki cihazları bulur
- MAC adresinden üretici (vendor) tespiti yapar
- Graphviz ile ağ topolojisi diyagramı çizer
- Tkinter arayüzü ile kullanıcı dostu deneyim sunar
- Cihaz listesi filtrelenebilir (IP, MAC veya vendor’a göre)
- Linux ve Windows desteklidir

 📷 Ekran Görüntüsü


![1](https://github.com/user-attachments/assets/fe0f9297-1e5f-4b40-95dd-f230131b386d)

![2](https://github.com/user-attachments/assets/6cd5f1df-54fd-4f7f-b247-224eb3834eec)

![3](https://github.com/user-attachments/assets/d613fed1-ad80-408e-91cd-ce5c73a107ea)


🛠 Gereksinimler

- Python 3.6+
- graphviz
- scapy
- pillow
- tkinter (Windows'ta varsayılan, Linux’ta `python3-tk` yüklenmeli)
- vendors.txt (MAC adresi - vendor eşlemesi için)

Kurulum:
pip install -r requirements.txt



⚙️ Kullanım
python main.py

GUI arayüzü üzerinden IP aralığını girip taramayı başlatabilirsiniz. Ağ haritası network_map.png olarak oluşturulur.


Projeyi faydalı bulduysanız GitHub’da yıldızlamayı ve paylaşmayı unutmayın!

---

🖼️ **3. Demo Görseli (`network_map.png`) Hakkında**

- Görselin sade, okunabilir olması önemli.
- Router merkezde, cihazlar dışta, her biri altında IP-MAC-hostname-vendor bilgileri olacak şekilde gösterilmeli.
- PNG dosyası doğrudan README altında gösterilmeli (`![network_map](network_map.png)`)

---

📦 **4. Ekstra Tavsiye – GitHub İçeriği Dosya Yapısı Önerisi**
