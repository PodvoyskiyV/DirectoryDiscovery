# to start main.py wordlists {Target URL} {Wordlist} level of recursive

import pyfiglet
import requests
import sys

banner = pyfiglet.figlet_format('DirDiscovery')
print(banner)

try:
    target_url = input('[*] Enter Target URL: ')
    file_name = input('[*] Enter Name Of The File Containing Directories: ')


    def request(url):
        try:
            return requests.get(url)
        except requests.exceptions.ConnectionError:
            pass


    file = open(f'wordlists/{file_name}', 'r')
    for line in file:
        directory = line.strip()
        full_url = target_url + '/' + directory
        response = request(full_url)
        if response:
            print('[*] Discovered Directory At This Path: ' + full_url)

except KeyboardInterrupt:
    print("\n Program finished !!!!")
    sys.exit()
