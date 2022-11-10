#!/usr/bin/python
import socket
from sys import argv

script, subdomains, output = argv

def getip(assets, stdout):
    save = open(stdout, 'w')
    with open(assets, 'r') as dnames:
        for name in dnames:
            name = name.rstrip()
            name = name.split('/')[-1]
            try:
                ip = socket.gethostbyname(name)
            except Exception as e:
                print(f"[!] DNS error {str(e)} at '{name}' [!]" )
            print(f'{name} : {ip}')
            save.write('\n'+str(ip))
        save.close()

getip(subdomains, output)


