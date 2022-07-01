# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 23 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que mostre todos os primos entre 1 e N sendo N um número
# inteiro fornecido pelo usuário. O programa deverá mostrar também o número
# de divisões que ele executou para encontrar os números primos. Serão
# avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

# Existem 168 números primos positivos menores do que 1000. 
#  
# São eles: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
# 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
# 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
# 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
# 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373,
# 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457,
# 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557,
# 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
# 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
# 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827,
# 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929,
# 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
# (sequência A000040 na OEIS).

import os, time

os.system('clear')

n = int(input('\nDigite um numero: '))
inicio = time.time()

for i in range(n+1):
    k = 0 
    print('-'*50)
    if str(i) in '01':
        print(f'\033[1;31m{i} não é primo\033[1;m')
        continue
    for j in range(2,i+1):
        if i%j == 0:
            print(f'{i} divisivel por {j}')
            k +=1
    if k == 1:
        print(f'\033[1;32m{i} é primo, Divisões realizadas: {k}\033[1;m')
    else:
        print(f'\033[1;31m{i} não é primo, Divisões realizadas: {k}\033[1;m')

termino = time.time()
print(f'\n\033[1;44mTempo de Execução: {termino - inicio:.1f} segundos\033[1;m\n')
