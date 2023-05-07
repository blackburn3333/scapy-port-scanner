import re as regex


# function to return ports that needs to scan,
# user can input * to return all ports to scan
# user can give single port to scan
# user can give range of ports [8080,8085] separated by comma
def input_port():
    print('To scan all ports enter [*]')
    print('To scan port by range enter ports separated by comma [80,84]')
    print('To scan single port enter port number [80]')
    ports_to_scan = input('> ')

    # Regex pattern to validate if the user input is port range
    range_regex = "\d+,\d+$"
    # Regex pattern to validate if the user input is single port
    single_regex = "^\d+$"

    # if input is matches to range Regex pattern return port range array
    if regex.match(range_regex, ports_to_scan) is not None:
        ports = ports_to_scan.split(",")
        return [int(ports[0]), int(ports[1]) + 1]
    # if input is matches to single port Regex pattern return port array
    elif regex.match(single_regex, ports_to_scan) is not None:
        return [int(ports_to_scan), int(ports_to_scan) + 1]
    # if input is * return all port range array
    elif "*" == ports_to_scan:
        return [1, 65536]
    else:
        print("Invalid input")
        input_port()
