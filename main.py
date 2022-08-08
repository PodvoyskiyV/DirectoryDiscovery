import pyfiglet
import requests
import sys
import datetime
from termcolor import colored

banner = pyfiglet.figlet_format('DirDiscovery')
print(colored(banner, 'green'))


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


def request(url):
    try:
        return requests.get(url, timeout=None).status_code
    except requests.exceptions.ConnectionError:
        pass


def directory_discovery(current_lvl, target):
    file = open(f'wordlists/{file_name}', 'r')
    for line in file:
        directory = line.strip()
        full_url = target + '/' + directory
        response = request(full_url)
        if response != 404:
            result.write(f'{full_url} {response} \n')
            if response // 100 == 1:
                print('Discovered Directory At This Path: ' + colored(full_url, 'blue'), colored(response, 'blue'))
            elif response // 100 == 2:
                print('Discovered Directory At This Path: ' + colored(full_url, 'blue'), colored(response, 'green'))
            elif response // 100 == 3:
                print('Discovered Directory At This Path: ' + colored(full_url, 'blue'), colored(response, 'yellow'))
            else:
                print('Discovered Directory At This Path: ' + colored(full_url, 'blue'), colored(response, 'red'))
            if current_lvl + 1 <= lvl_of_recursion:
                directory_discovery(current_lvl + 1, full_url)
    file.close()


try:
    target_url = input('[*] Enter Target URL like http(s)://example.com: ')
    while True:
        if target_url[:8] == 'https://' or target_url[:7] == 'http://':
            if request(target_url) == 200:
                break
            else:
                print(colored('Response of your URL is not 200', 'red'))
                print('Check your URL')
                target_url = input('[*] Enter Target URL: ')
        else:
            print(colored('Target URL is incorrect.', 'red'))
            print('Target URL should be like', colored('http(s)://example.com', 'green'))
            target_url = input('[*] Enter Target URL: ')

    git = 'https://github.com/PodvoyskiyV/DirectoryDiscovery/tree/master/wordlists'
    print('\n You have some files to choose:')
    print('best15 [1], best110 [2], best1050 [3], big [4], small [5], common [6], indexes [7], names [8]')
    print('View all this files you can at', colored(git, 'blue'))
    file_name = input('[*] Enter a number corresponding to the file name: ')
    while True:
        if file_name in ['1', '2', '3', '4', '5', '6', '7', '8']:
            file_name = chosen_file(int(file_name))
            break
        else:
            print(colored("Typed that doesn't match any of the filenames", 'red'))
            print('You have some files to choose:')
            print('best15 [1], best110 [2], best1050 [3], big [4], small [5], common [6], indexes [7], names [8]')
            file_name = input('[*] Enter a number corresponding to the file name from 1 to 8: ')

    print('\n Level of recursion can help you to make more deep search of directories')
    print('Example:', colored('http://example.com/lvl1/lvl2/lvl3/lvl4/lvl5', 'blue'))
    lvl_of_recursion = input('[*] Enter Level Of Recursion from 1 to 9: ')
    while True:
        if lvl_of_recursion in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            lvl_of_recursion = int(lvl_of_recursion)
            break
        else:
            print(colored('Level of Recursion is incorrect', 'red'))
            lvl_of_recursion = input('[*] Enter Level Of Recursion from 1 to 9: ')

    start = datetime.datetime.now()
    print("\n" + "-" * 50)
    print("Scanning Target: " + target_url)
    print("Level of Recursion:", lvl_of_recursion)
    print("Wordlist: " + file_name)
    print("Scanning started at: " + str(start))
    print("-" * 50 + "\n")

    result = open('result.txt', 'w+')
    result.write(pyfiglet.figlet_format('Directories'))
    result.write('\n')
    result.close()
    result = open('result.txt', 'a+')

    directory_discovery(1, target_url)

    result.close()

    end = datetime.datetime.now()
    print("\n" + "-" * 50)
    print("Scanning ended at: " + str(end))
    print("Scanning duration is: " + str(end-start))
    print("-" * 50 + "\n")


except KeyboardInterrupt:
    try:
        result.close()
    except NameError:
        pass

    print("\n Program finished by user !!!!")
    sys.exit()
