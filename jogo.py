import pygame
from random import randint

pygame.init()
x = 710
y = 100
pos_x = 360
pos_y_1 = 1300
pos_y_2 = 1300
pos_y_3 = 1300
pos_y_4 = 1300
pos_x_fundo = 0
pos_y_fundo = -2000
time = 0
tempo_seg = 0

posicao_linhas_y = -5
velocidade_linha = 15

velocidade = 15
velocidade_carros = 15
fundo = pygame.image.load('fundo2.png')
carro_amarelo = pygame.image.load('amarelo.png')
carro_azul = pygame.image.load('azul.png')
carro_branco = pygame.image.load('branco.png')
carro_verde = pygame.image.load('verde.png')
carro_preto = pygame.image.load('preto.png')
linhas = pygame.image.load('linhas.png')

font = pygame.font.SysFont('arial black', 30)
texto = font.render("Tempo: ", True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)

janela = pygame.display.set_mode((1350, 700))

pygame.display.set_caption("Jogo dos carros")
janela_aberta = True

while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT] and x<= 930:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 327:
        x -= velocidade

    if x - 90 < pos_x and y + 205 > pos_y_1:
        y = 3000

    if x + 60 > pos_x + 514.5 and y + 210 > pos_y_4:
        y = 3000

    #if x - 90 < pos_x and y + 205 > pos_y_2:
    #    y = 3000

    #if x + 60 > pos_x + 514.5 and y + 210 > pos_y_3:
    #    y = 3000



    if pos_y_fundo >= 0:
        pos_y_fundo = -2200
    pos_y_fundo += velocidade_linha

    if pos_y_1 <= -400:
        pos_y_1 = randint(800, 3000)

    if pos_y_2 <= -1000:
        pos_y_2 = randint(2000, 4000)

    if pos_y_3 <= -400:
        pos_y_3 = randint(1000, 3500)

    if pos_y_4 <= -400:
        pos_y_4 = randint(1500, 4000)

    pos_y_1 -= velocidade_carros
    pos_y_2 -= velocidade_carros + 10
    pos_y_3 -= velocidade_carros + 5
    pos_y_4 -= velocidade_carros + 15

    if posicao_linhas_y >= 80:
        posicao_linhas_y = 20
    posicao_linhas_y += velocidade_linha

    if time < 20:    #20 * 50 É 1 SEGUNDO
        time += 1
    else:
        tempo_seg += 1
        texto = font.render("Tempo: " + str(tempo_seg), True, (255, 255, 255), (0, 0, 0))
        time = 0

    janela.blit(fundo, (pos_x_fundo, pos_y_fundo))
    janela.blit(linhas, (pos_x + 130, posicao_linhas_y))
    janela.blit(linhas, (pos_x + 302, posicao_linhas_y))
    janela.blit(linhas, (pos_x + 476, posicao_linhas_y))
    janela.blit(carro_amarelo, (x, y))
    janela.blit(carro_preto, (pos_x, pos_y_1))
    janela.blit(carro_verde, (pos_x + 171.5, pos_y_2))
    janela.blit(carro_azul, (pos_x + 343, pos_y_3))
    janela.blit(carro_branco, (pos_x + 514.5, pos_y_4))
    janela.blit(texto, pos_texto)

    pygame.display.update()

var = pygame.QUIT
