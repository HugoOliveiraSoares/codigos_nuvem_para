from time import sleep, perf_counter
from threading import Thread
from random import randint


def tarefa(name):
    print('Iniciando tarefa ', name, '...')
    tempo = randint(1, 15)
    print(f'Vai esperar {tempo} segundo(s)')
    sleep(tempo)
    print('Feito ', name)


start_time = perf_counter()

# Cria duas threads
t1 = Thread(target=tarefa, args=(1,))
t2 = Thread(target=tarefa, args=(2,))

# Inicializa as threads
t1.start()
t2.start()

# Aguarda até que as threads sejam completadas
t1.join()
t2.join()

end_time = perf_counter()

print(f'As tarefas levaram {end_time- start_time: 0.2f} segundo(s) para executar.')
