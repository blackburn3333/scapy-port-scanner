from progress.spinner import PixelSpinner
from scapy.all import *

conf.verb = 0


# function to scan ports of ip address and return open ports array
def scan_ports(target, ports):
    bar = PixelSpinner('Scanning for ports ')
    open_ports = []
    # loop port range
    for port in range(ports[0], ports[1]):
        # creates a TCP packet for destination IP and destination Port, packet is set to SYN flag
        packet_req = IP(dst=target) / TCP(dport=port, flags="S")
        # send packet and waits for response, timeout sets to 1 second
        packet_res = sr1(packet_req, timeout=1)
        # send another packet to rest connection
        send(IP(dst=target) / TCP(dport=port, flags="R"), verbose=0)
        # check if the response in not none
        if packet_res is not None:
            # get flags field of TCP layer of response
            flags = packet_res.getlayer(TCP).flags
            # check if packet is successfully handshake
            if flags == 0x12:
                open_ports += open_ports + [port]
        bar.next()
    bar.finish()
    return open_ports


def print_ports(ip, open_ports):
    print("Results")
    print(ip)
    if not open_ports:
        print('No open ports found on target')
    else:
        for port in open_ports:
            print("Discovered open port -> ", port)
