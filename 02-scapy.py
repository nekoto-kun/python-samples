from scapy.all import sniff
from scapy.layers.inet import IP

def packet_sniffer(interface):
    print(f"Sniffing on {interface}")
    sniff(iface=interface, prn=process_packet, store=False)

def process_packet(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        print(f"New Packet: {ip_layer.src} -> {ip_layer.dst}")

interface = input("Enter network interface: ")
packet_sniffer(interface)