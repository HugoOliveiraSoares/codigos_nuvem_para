import multiprocessing
from time import sleep, perf_counter
from random import randint
import os

def tarefa():
    p = multiprocessing.current_process()
    pid = p.pid

    print('\nPID subprocesso = ' + str(pid))
    tempo = randint(1, 5)
    print(f'Vai esperar {tempo} segundo(s)')
    sleep(tempo)
    print('Feito')



if __name__ == "__main__":
    start_time = perf_counter()

    print('Quant. de nucleos : ', multiprocessing.cpu_count())
    print('PID do processo principal : ', os.getpid())
    print('')

    # Cria dois subprocessos
    p1 = multiprocessing.Process(target=tarefa)
    p2 = multiprocessing.Process(target=tarefa)

    # Inicializa os processos
    p1.start()
    p2.start()

    # Aguarda até que as threads sejam completadas
    p1.join()
    p2.join()

    end_time = perf_counter()

    print(f'\nAs tarefas levaram {end_time- start_time: 0.2f} segundo(s) para executar.')
