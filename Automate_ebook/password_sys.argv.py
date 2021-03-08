#! python3
# pw.py - An insecure password locker program.

from sys import argv, exit
from pyperclip import copy

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}


if __name__ == '__main__':

    if len(argv) < 2:
        print("Usage: python pw.py [account] - copy account password")
        exit()

    account = argv[1]

    if account in PASSWORDS:
        copy(PASSWORDS[account])
        print("Password for {a} copied to clipboard".format(a=account))
    else:
        print("There is no account named {a}".format(a=account))
