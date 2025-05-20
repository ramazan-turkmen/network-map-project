import os
import socket
import subprocess
import platform
import tkinter as tk
from tkinter import ttk, messagebox
from scapy.all import ARP, Ether, srp
from graphviz import Graph
from PIL import Image, ImageTk

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "unknown"

def load_vendors(filename='vendors.txt'):
    vendors = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                if ',' in line:
                    prefix, name = line.strip().split(',', 1)
                    vendors[prefix.upper()] = name.strip()
    except FileNotFoundError:
        print("vendors.txt bulunamadı.")
    return vendors

def get_vendor(mac, vendors):
    mac_prefix = mac.upper().replace(":", "")[:6]
    return vendors.get(mac_prefix, "Bilinmeyen")

def scan(ip_range, vendors):
    print(f"[+] Ağ taranıyor: {ip_range}")
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

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

def draw_graph(devices, output_file="network_map"):
    dot = Graph('Network Map', format='png')
    dot.attr('node', shape='box', style='filled', color='lightblue2')
    dot.node("Router", "Router")

    for device in devices:
        label = f"{device['ip']}\n{device['mac']}\n{device['hostname']}\n{device['vendor']}"
        dot.node(device['ip'], label)
        dot.edge("Router", device['ip'])

    dot.render(output_file, view=False)
    print(f"[✓] Ağ haritası kaydedildi: {output_file}.png")

def open_image(image_path):
    try:
        if platform.system() == "Windows":
            os.startfile(image_path)
        elif platform.system() == "Darwin":
            subprocess.call(["open", image_path])
        else:
            subprocess.call(["xdg-open", image_path])
    except Exception as e:
        print(f"Görüntü açılamadı: {e}")

def update_device_list(devices, tree, filter_entry):
    for row in tree.get_children():
        tree.delete(row)

    filter_text = filter_entry.get().lower()

    for dev in devices:
        if filter_text in dev['ip'].lower() or filter_text in dev['mac'].lower() or filter_text in dev['vendor'].lower():
            tree.insert('', tk.END, values=(dev['ip'], dev['mac'], dev['hostname'], dev['vendor']))

def start_scan(ip_entry, tree, vendors, filter_entry):
    ip_range = ip_entry.get().strip()
    if not ip_range:
        messagebox.showerror("Hata", "IP aralığı giriniz.")
        return

    devices = scan(ip_range, vendors)
    update_device_list(devices, tree, filter_entry)
    draw_graph(devices)
    messagebox.showinfo("Tarama Tamamlandı", f"{len(devices)} cihaz bulundu.")

def build_gui():
    vendors = load_vendors()

    window = tk.Tk()
    window.title("Ağ Haritası Tarayıcı - V7")
    window.geometry("800x600")

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

if __name__ == "__main__":
    build_gui()
