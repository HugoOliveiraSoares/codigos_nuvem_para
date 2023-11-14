#!/usr/bin/python
'''
Este código carrega uma imagem jpg, quebra em duas partes (metades superior e inferior) e
realiza um ajuste de brilho e contraste

22/08/2022
'''

import numpy as np
from PIL import Image
from time import perf_counter
import multiprocessing
from random import randint
import os

def define_brilho(id,matriz, alpha, beta):
    imagem_result = np.zeros(matriz.shape, matriz.dtype)

    y, x, c = matriz.shape

    for ypos in range(y):
        for xpos in range(x):
            for canal in range(c):
                imagem_result[ypos, xpos, canal] = np.clip((alpha * matriz[ypos, xpos, canal]) + beta, 0, 255)

    Image.fromarray(imagem_result).save(f'img_{id}.jpeg')



if __name__ == '__main__':
    start_time = perf_counter()

    imagem_original = Image.open('img001.jpeg')

    matriz_original = np.asarray(imagem_original)

    y, x, c = matriz_original.shape


    matriz_superior = np.copy(matriz_original[:int(y/2)])
    matriz_superior_1 = np.copy(matriz_superior[:,:int(x/2)])
    matriz_superior_2 = np.copy(matriz_superior[:,int(x/2):])

    matriz_inferior = np.copy(matriz_original[int(y/2):])
    matriz_inferior_1 = np.copy(matriz_inferior[:,:int(x/2)])
    matriz_inferior_2 = np.copy(matriz_inferior[:,int(x/2):])


    p1 = multiprocessing.Process(target=define_brilho, args=('quadrante1',matriz_superior_1,3, 100))
    p2 = multiprocessing.Process(target=define_brilho, args=('quadrante2',matriz_superior_2,3, 100))
    p3 = multiprocessing.Process(target=define_brilho, args=('quadrante3',matriz_inferior_1,3, 100))
    p4 = multiprocessing.Process(target=define_brilho, args=('quadrante4',matriz_inferior_2,3, 100))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()


    img_quadrante1 = Image.open('img_quadrante1.jpeg')
    img_quadrante2 = Image.open('img_quadrante2.jpeg')
    img_quadrante3 = Image.open('img_quadrante3.jpeg')
    img_quadrante4 = Image.open('img_quadrante4.jpeg')

    matriz_qua1 = np.asarray(img_quadrante1)
    matriz_qua2 = np.asarray(img_quadrante2)
    matriz_qua3 = np.asarray(img_quadrante3)
    matriz_qua4 = np.asarray(img_quadrante4)


    matriz_sup = np.concatenate(( matriz_qua1, matriz_qua2), axis=1)
    matriz_inf = np.concatenate(( matriz_qua3, matriz_qua4), axis=1)

    matriz_comp = np.concatenate(( matriz_sup, matriz_inf))

    imagem_comp = Image.fromarray(matriz_comp)

    imagem_comp.save('img005.jpeg')

    end_time = perf_counter()
    print(f'As tarefas levaram {end_time- start_time: 0.2f} segundo(s) para executar.')

