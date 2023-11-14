from threading import Thread, Lock
from time import sleep
from random import randint
from datetime import datetime

contador = 0

def incrementar(valor, id, lock):
    global contador

    lock.acquire()

    local_contador = contador
    local_contador += valor

    sleep(randint(1, 5))

    contador = local_contador

    print(f'\n Thread {id} - contador = {contador} [{datetime.now()}]')

    lock.release()


if __name__ == "__main__":
    lock = Lock()

    threads = [Thread(target=incrementar, args=(randint(1, 5),i, lock)) for i in range(0,2)]
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'\n Contador final = {contador}')
