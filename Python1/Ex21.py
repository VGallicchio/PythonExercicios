#21-Faça um programa que abra e reproduza um audio de arquivo em MP3.


import pygame # este modulo e para jogos ele pode importar arquivos como de audio para o python.
# Existem vários tipos de módulos e sempre bom pesquisar e utilizar aquele que se adequar ao que você quer.
pygame.init() # este comando inicia o modulo. Algunos modulos tem que ser iniciados.
pygame.mixer.music.load('ex01.mp3'#nome do arquivo que vai ser carregado)
pygame.mixer.music.play() #para rodar, o arquivo.
pygame.event.wait() #para parar o evento.