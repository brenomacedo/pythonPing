from os import *
from termcolor import colored
from art import text2art
from time import sleep

print(colored(text2art('MULTI PING'), 'red', attrs=['bold']))

pack = int(input(colored('Digite o numero de pacotes a ser enviado', 'blue', attrs=['bold'])))

with open('hosts.txt', 'r') as file:
    dump = file.read()
    for ip in dump:
        print(colored('Verificando o ip: ' + ip, 'red', attrs=['bold']))
        print('-'*60)
        system('ping -n {} {}'.format(pack, ip))
        print('-'*60)
        sleep(3)