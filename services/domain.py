import tldextract
from services.ip import *


# function to return root domain of input url
def clear_domain(url):
    try:
        extracted = tldextract.extract(url)
        root_domain = extracted.registered_domain
        return root_domain
    except ValueError:
        print('Something went wrong')


# function to input target url and return ip address of root domain
def ip_by_domain():
    try:
        domain = input("Input domain > ")
        root_domain = clear_domain(domain)
        ip_address = get_ip_address_of_domain(root_domain)
        if "0.0.0.0" == ip_address:
            print('invalid domain, please try another domain.')
            ip_by_domain()
        else:
            return ip_address
    except ValueError:
        print('Something went wrong')
        ip_by_domain()
