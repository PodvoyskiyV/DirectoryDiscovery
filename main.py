# to start main.py wordlists {Target URL} {Wordlist} level of recursion, switches to choose wordlist http://example.com

import pyfiglet
import requests
import sys

banner = pyfiglet.figlet_format('DirDiscovery')
print(banner)


def chosen_file(number):
    switcher = {
        1: 'best15.txt',
        2: 'best110.txt',
        3: 'best1050.txt',
        4: 'big.txt',
        5: 'small.txt',
        6: 'common.txt',
        7: 'indexes.txt',
        8: 'names.txt'
    }
    return switcher.get(number)


try:
    target_url = input('[*] Enter Target URL like http(s)://example.com: ')
    while True:
        if target_url[:8] == 'https://' or target_url[:7] == 'http://':
            break
        else:
            print('Target URL should be like http(s)://example.com')
            target_url = input('[*] Enter Target URL: ')

    print('You have some files to choose:')
    print('best15 [1], best110 [2], best1050 [3], big [4], small [5], common [6], indexes [7], names [8]')
    print('View all this files you can at https://github.com/PodvoyskiyV/DirectoryDiscovery/tree/master/wordlists')
    file_name = input('[*] Enter a number corresponding to the file name: ')
    while True:
        if file_name in ['1', '2', '3', '4', '5', '6', '7', '8']:
            file_name = chosen_file(int(file_name))
            break
        else:
            print("Typed that doesn't match any of the filenames")
            print('You have some files to choose:')
            print('best15 [1], best110 [2], best1050 [3], big [4], small [5], common [6], indexes [7], names [8]')
            file_name = input('[*] Enter a number corresponding to the file name from 1 to 8: ')

    print('Level of recursion can help you to make more deep search of directories')
    print('Example: http://example.com/lvl1/lvl2/lvl3/lvl4/lvl5')
    level_of_recursion = input('[*] Enter Level Of Recursion from 1 to 5: ')
    while True:
        if level_of_recursion in ['1', '2', '3', '4', '5']:
            level_of_recursion = int(level_of_recursion)
            break
        else:
            print('Level of Recursion is incorrect')
            level_of_recursion = input('[*] Enter Level Of Recursion from 1 to 5: ')


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
