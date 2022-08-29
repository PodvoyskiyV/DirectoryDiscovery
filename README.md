# DirectoryDiscovery

Directory Discovery is a Python program for finding directories in web applications.

## Description

When you explore a web application, you need to understand what directories and pages it contains. This program gives you the opportunity to automate this process. Also you can choose recursion level (http://example.com/lvl1/lvl2/lvl3/lvl4/lvl5...) and word lists.

Word lists:
- best15.txt
- best110.txt
- best1050.txt
- small.txt
- big.txt
- common.txt
- names.txt
- indexes.txt

(You can view them here - https://github.com/PodvoyskiyV/DirectoryDiscovery/tree/master/wordlists)

## External modules

1. DATETIME - used in the user interface
2. PYFIGLET - to create a banner and use in the user interface
3. REQUESTS - check for pages and directories
4. TERMCOLOR - for banner color and used in user interface.
5. SYS - for the correct termination of the program, if the user wants to stop the search

## Installation

```bash
git clone https://github.com/PodvoyskiyV/DirectoryDiscovery.git

pip install pyfiglet
pip install requests
pip install termcolor
```

## Usage

PATH is the path to the project directory on your system.

```bash
python3 {PATH}/DirectoryDiscovery/DirectoryDiscovery.py
```

## Support

mail: vadim.podvoykiy@gmail.com
telegram: https://t.me/rise_up_with_sun
