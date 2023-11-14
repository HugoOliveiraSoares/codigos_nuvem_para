import numpy as np
from PIL import Image
from time import perf_counter

# matriz = imagem para operação; alpha = contraste ;  beta= brilho ;
def define_brilho(matriz, alpha, beta):
    # Cria-se uma imagem temporária, "vazia", com as dimensões e tipo da original (passada por parâmetro)
    imagem_result = np.zeros(matriz.shape, matriz.dtype)

    # Obtem-se as dimensões e quantidade de canais da imagem original (passada por parâmetro)
    # No nosso caso, vamos obter as dimensões em pixels (y, x) e a quantidade de canais (RGB = 3)
    y, x, c = matriz.shape

    # Percorre todos os pares x,y da imagem em todos os canais
    for ypos in range(y):
        for xpos in range(x):
            for canal in range(c):
                # Realiza-se os cálculos necessários para cada ponto e canal, mantendo o valor resultante dentro
                # do limite de 0 a 255
                imagem_result[ypos, xpos, canal] = np.clip((alpha * matriz[ypos, xpos, canal]) + beta, 0, 255)

    # Retorna a matriz modificada da imagem
    return imagem_result

if __name__ == '__main__':
    start_time = perf_counter()

    # Carrega uma imagem de um arquivo
    img = Image.open('img001.jpeg')

    # Converte a imagem em uma matriz RGB
    imagem_original = np.asarray(img)

    # Executa a função de contraste e brilho
    imagem_brilho = define_brilho(imagem_original, 3, 100)

    # Salva a nova imagem (matriz) em um novo arquivo
    imagem2 = Image.fromarray(imagem_brilho)
    imagem2.save('img002.jpeg')

    end_time = perf_counter()
    print(f'As tarefas levaram {end_time- start_time: 0.2f} segundo(s) para executar.')

