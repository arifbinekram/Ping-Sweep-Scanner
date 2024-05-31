import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import sys
import re
from scapy.all import *

def validate_ip(ip):
    ip_regex = re.compile(r"^([0-9]{1,3}\.){3}[0-9]{1,3}$")
    if ip_regex.match(ip) is None:
        return False
    parts = ip.split(".")
    for part in parts:
        if int(part) < 0 or int(part) > 255:
            return False
    return True

if len(sys.argv) != 3:
    print(f"usage: {sys.argv[0]} start_ip_addr end_ip_addr")
    sys.exit(0)

start_ip = sys.argv[1]
end_ip = sys.argv[2]

if not validate_ip(start_ip):
    print("Starting IP address is invalid")
    sys.exit(0)

if not validate_ip(end_ip):
    print("End IP address is invalid")
    sys.exit(0)

ip_list1 = start_ip.split(".")
ip_list2 = end_ip.split(".")
if not (ip_list1[0] == ip_list2[0] and ip_list1[1] == ip_list2[1] and ip_list1[2] == ip_list2[2]):
    print("IP addresses are not in the same class C subnet")
    sys.exit(0)

if int(ip_list1[3]) > int(ip_list2[3]):
    print("Starting IP address is greater than ending IP address")
    sys.exit(0)

network_addr = ip_list1[0] + "." + ip_list1[1] + "." + ip_list1[2] + "."
start_ip_last_octet = int(ip_list1[3])
end_ip_last_octet = int(ip_list2[3])

if start_ip_last_octet < end_ip_last_octet:
    print(f"Pinging range {network_addr}{start_ip_last_octet}-{end_ip_last_octet}")
else:
    print(f"Pinging {network_addr}{start_ip_last_octet}\n")

live_hosts = []

for x in range(start_ip_last_octet, end_ip_last_octet + 1):
    ip = network_addr + str(x)
    packet = IP(dst=ip) / ICMP()
    response = sr1(packet, timeout=2, verbose=0)
    if response is not None:
        if response[ICMP].type == 0:
            live_hosts.append(ip)

print("Scan complete!\n")
if live_hosts:
    print("Hosts found:\n")
    for host in live_hosts:
        print(host)
else:
    print("No live hosts found\n")

