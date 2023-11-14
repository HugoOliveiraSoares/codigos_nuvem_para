import multiprocessing

def tarefa(a, inicio, fim):
    p = multiprocessing.current_process()
    for i in range(inicio, fim):
        a[i] = p.pid
    print(p.pid)


if __name__ == '__main__':
    array = multiprocessing.Array('i', range(20))

    p1 = multiprocessing.Process(target=tarefa, args=(array,  0, 10))
    p2 = multiprocessing.Process(target=tarefa, args=(array, 10, 20))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(array[:])
