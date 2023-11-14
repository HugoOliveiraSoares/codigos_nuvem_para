import multiprocessing

def tarefa(n):
    n.value = n.value * 2


if __name__ == '__main__':
    num = multiprocessing.Value('d', 5.0)

    p1 = multiprocessing.Process(target=tarefa, args=(num,))
    p2 = multiprocessing.Process(target=tarefa, args=(num,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(num.value)


