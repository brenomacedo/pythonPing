from os import *
from termcolor import colored
from art import text2art

print(colored(text2art('PING'), 'yellow', attrs=['bold']))

host = str(input(colored('Digite o ip ou o host a ser verificado:', 'red', attrs=['bold'])))
packs = int(input(colored('Digite o numero de pacotes a ser enviado', 'blue', attrs=['bold'])))

system('ping -n {} {}'.format(packs, host))