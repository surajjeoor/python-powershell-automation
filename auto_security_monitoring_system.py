from scapy.all import ARP, Ether, srp
import time
import socket

def scan_network(ip_range: str, timeout: float = 2.0):
    #create ARP packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=timeout, verbose=0)[0]
    clients = []

    for sent, received in result:
        try:
            hostname = socket.gethostbyaddr(received.psrc)[0]
        except socket.herror:
            hostname = "Unknown"
        clients.append({'ip': received.psrc, 'mac': received.hwsrc, 'hostname': hostname})
    return clients

#use your subnet range
subnet_range = "192.168.1.0/24"
devices = scan_network(subnet_range)
print("Available devices in the network:")
for device in devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}, Hostname: {device['hostname']}")