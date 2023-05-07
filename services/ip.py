import socket
import ipaddress


def get_ip_address_of_domain(root_domain):
    try:
        _ip = socket.gethostbyname(root_domain)
        return _ip
    except:
        print('Something went wrong, when gathering IP of root domain')


def get_ip_address():
    try:
        ip = input("Input target IP > ")
        ipaddress.ip_address(ip)
        return ip
    except ValueError:
        print("Invalid IP address, please try again")
        get_ip_address()


def is_ip_is_v4_or_v6(ip):
    try:
        if type(ipaddress.ip_address(ip)) is ipaddress.IPv4Address:
            return "V4"
        else:
            return "V6"
    except ValueError:
        print('Something went wrong')
