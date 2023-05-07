from common import *
from services.domain import *
from services.ip import *
from services.port import *
from services.scan import *


def start():
    window_len = title_container('PORT SCANNER', 'Port Scanner')
    menu_container(["[1] Scan ports with IP address.", "[2] Scan ports with root domain.", "[3] Exit."], window_len)
    choice = check_choice_input(input("> "), ["1", "2", "3"], ">")
    if "3" == choice:
        exit_terminal()
    else:
        ip_address = None
        if "2" == choice:
            ip_address = ip_by_domain()
        elif "1" == choice:
            ip_address = get_ip_address()

        if ip_address is None:
            print('[3] Exit.')
            print('[4] Restart')
            choice = check_choice_input(input("> "), ["3", "4"], ">")
            if "3" == choice:
                exit_terminal()
            else:
                clean_terminal()
                start()
        else:
            print("#" * window_len)
            ports = input_port()
            ports.sort()
            open_ports = scan_ports(ip_address, ports)
            open_ports = list(dict.fromkeys(open_ports))
            print_ports(ip_address, open_ports)


if __name__ == '__main__':
    start()
