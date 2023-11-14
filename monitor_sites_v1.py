#!/bin/python

from threading import Thread
from time import sleep
import requests
import os

def monitor(url, intervalo, quant):
   
    r1 = ''
    for i in range(0,quant):
          
        print(f"Acesso {i+1} no site {url} com PID: {os.getpid()}")
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        r = repr(r.text).encode('utf-8')
        if r != r1:
            print("O site ", url, " foi modificado")
        r1 = r
        sleep(intervalo)


if __name__ == "__main__":

    sites = ['https://g1.globo.com/', 'https://noticias.uol.com.br/', 'https://www.r7.com/', 'https://www.cnnbrasil.com.br/']

    threads = [Thread(target=monitor, args=(site, 5, 3)) for site in sites]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # for site in sites:
    #    r = requests.get(site, headers={'User-Agent': 'Mozilla/5.0'})
    #    print(r.text)

