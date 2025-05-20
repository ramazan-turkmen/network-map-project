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






Kodların bir kısmı!! Tüm proje dosyaların içinde paylaşıma açılmıştır.
.....

    result = srp(packet, timeout=2, verbose=0)[0]
    devices = []

    for sent, received in result:
        mac = received.hwsrc
        vendor = get_vendor(mac, vendors)
        devices.append({
            "ip": received.psrc,
            "mac": mac,
            "hostname": get_hostname(received.psrc),
            "vendor": vendor
        })

    return devices

.....

    for device in devices:
        label = f"{device['ip']}\n{device['mac']}\n{device['hostname']}\n{device['vendor']}"
        dot.node(device['ip'], label)
        dot.edge("Router", device['ip'])

    dot.render(output_file, view=False)
    print(f"[✓] Ağ haritası kaydedildi: {output_file}.png")

.....

    filter_text = filter_entry.get().lower()

    for dev in devices:
        if filter_text in dev['ip'].lower() or filter_text in dev['mac'].lower() or filter_text in dev['vendor'].lower():
            tree.insert('', tk.END, values=(dev['ip'], dev['mac'], dev['hostname'], dev['vendor']))

.....

    devices = scan(ip_range, vendors)
    update_device_list(devices, tree, filter_entry)
    draw_graph(devices)
    messagebox.showinfo("Tarama Tamamlandı", f"{len(devices)} cihaz bulundu.")

.....

    if platform.system() == "Linux":
        messagebox.showinfo("Linux Uyarısı", "Lütfen sistem paketlerinin yüklü olduğundan emin olun:\n\n- graphviz\n- python3-tk\n- xdg-utils")

    frame_top = tk.Frame(window)
    frame_top.pack(pady=10)

    tk.Label(frame_top, text="IP Aralığı:").pack(side=tk.LEFT)
    ip_entry = tk.Entry(frame_top, width=30)
    ip_entry.insert(0, "192.168.1.0/24")
    ip_entry.pack(side=tk.LEFT, padx=5)

    filter_entry = tk.Entry(frame_top, width=20)
    filter_entry.pack(side=tk.LEFT, padx=5)
    filter_entry.insert(0, "")

    scan_button = tk.Button(frame_top, text="Taramayı Başlat", command=lambda: start_scan(ip_entry, tree, vendors, filter_entry))
    scan_button.pack(side=tk.LEFT, padx=5)

    frame_tree = tk.Frame(window)
    frame_tree.pack(fill=tk.BOTH, expand=True)

    tree = ttk.Treeview(frame_tree, columns=("IP", "MAC", "Hostname", "Vendor"), show="headings")
    for col in ("IP", "MAC", "Hostname", "Vendor"):
        tree.heading(col, text=col)
        tree.column(col, width=150)
    tree.pack(fill=tk.BOTH, expand=True)

    frame_bottom = tk.Frame(window)
    frame_bottom.pack(pady=10)

    btn_open_map = tk.Button(frame_bottom, text="PNG'yi Harici Aç", command=lambda: open_image("network_map.png"))
    btn_open_map.pack()

    window.mainloop()








