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

![Image](https://github.com/user-attachments/assets/1213c012-31b1-4b03-8e89-6b6b130e8004)

![Image](https://github.com/user-attachments/assets/2a0d4682-56bc-491d-8bfc-71b9cc456acd)

![Image](https://github.com/user-attachments/assets/72a8fc30-1aea-437f-9ef2-785ae7a7f13e)

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
