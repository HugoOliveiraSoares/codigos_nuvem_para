import multiprocessing

def tarefa(n, l):
    l.acquire()
    n.value = n.value * 2
    l.release()

if __name__ == '__main__':

    lock = multiprocessing.Lock()

    num = multiprocessing.Value('d', 5.0)

    p1 = multiprocessing.Process(target=tarefa, args=(num, lock))
    p2 = multiprocessing.Process(target=tarefa, args=(num, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(num.value)
