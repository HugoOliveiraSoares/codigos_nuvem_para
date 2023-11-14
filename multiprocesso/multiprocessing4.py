'''
A classe "Pool" pode lidar com um enorme número de processos em multiprocessing.

Ela possui a capacidade de enfileirar os trabalhos e a memória é alocada apenas para os processos em execução,
diferentemente da classe "Process", que aloca memória para todos os processos.

'''
import multiprocessing
import time, os
from random import randint

dados = (["Dado A", 7], ["Dado B", 4], ["Dado C", 14], ["Dado D", 2], ["Dado E", 20])


def tarefa(d):
    p = multiprocessing.current_process()
    print("\nPID : " + str(p.pid))

    print("Processando %s , com o valor %s" % (d[0], d[1]))
    time.sleep(randint(1, 5))
    print("\nTrabalho [ %s ] finalizado." % d[0])


if __name__ == '__main__':
    p = multiprocessing.Pool(3)
    p.map(tarefa, dados)

