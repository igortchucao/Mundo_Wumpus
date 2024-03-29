import pygame, os, Musicas

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Mundo do Wumpus')
width = 1200
height = 800

'''Fonte da Escrita'''
font = pygame.font.SysFont(None, 49)

'''Imagens'''
Imagem_buraco = pygame.image.load(os.path.join('Imagens', 'buraco1.png'))
Imagem_wumpus = pygame.image.load(os.path.join('Imagens', 'Wumpus1.png'))
Imagem_Ouro = pygame.image.load(os.path.join('Imagens', 'Ouro.png'))

'''Cores'''
BLACK = 0, 0, 0
WHITE = 255, 255, 255
YELLOW = 238, 221, 130
ROSA = 255, 0, 255
ROSA_c = 238, 130, 238
MARROM_c = 184, 134, 11
RED = 255, 0, 0

'''Tamanho da janela'''
size = width, height

'''Personagem do Jogo'''
screen = pygame.display.set_mode(size)

'''DESENHA O TABULEIRO'''
def desenha_tabuleiro(tm):
    textRef = ""
    for ref in range(0, 16, +1):
        x = ((ref % 4) * tm)
        y = ((ref // 4) * tm)
        pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, tm, tm), 5)
        pygame.draw.rect(screen, WHITE, pygame.Rect(x + 8, y + 8, tm - 15, tm - 15), 5)
        textRef = ref
        screen.blit(pygame.font.SysFont(None, 40).render(str(ref), True, RED), [x + 20, y + 20])

    pygame.draw.rect(screen, BLACK, pygame.Rect(100, 60, 600, 75))
    pygame.draw.rect(screen, BLACK, pygame.Rect(100, 260, 600, 75))
    pygame.draw.rect(screen, BLACK, pygame.Rect(100, 460, 600, 75))
    pygame.draw.rect(screen, BLACK, pygame.Rect(100, 660, 600, 75))

    pygame.draw.rect(screen, BLACK, pygame.Rect(60, 100, 75, 600))
    pygame.draw.rect(screen, BLACK, pygame.Rect(260, 100, 75, 600))
    pygame.draw.rect(screen, BLACK, pygame.Rect(460, 100, 75, 600))
    pygame.draw.rect(screen, BLACK, pygame.Rect(660, 100, 75, 600))
    menu()

'''DESENHA O MENU LATERAL'''
def menu():
    pygame.draw.rect(screen, WHITE, pygame.Rect(805, 0, 395, 800), 5)
    pygame.draw.rect(screen, WHITE, pygame.Rect(815, 10, 375, 780))
    text = font.render('MUNDO DO WUMPUS ', True, BLACK)
    screen.blit(text, [832, 40])

class Person():
    def __init__(self, ref):
        '''IMAGENS DISTINTAS QUE FAZEM OS FRAMES DO JOGO'''
        self.frames = [pygame.image.load(os.path.join('Imagens', 'Personagem_Frente1.png')), 
                       pygame.image.load(os.path.join('Imagens', 'Personagem_Frente2.png')),
                       pygame.image.load(os.path.join('Imagens', 'Personagem_Frente3.png')),

                       pygame.image.load(os.path.join('Imagens', 'Personagem_Lado1.png')),
                       pygame.image.load(os.path.join('Imagens', 'Personagem_Lado2.png')),
                       pygame.image.load(os.path.join('Imagens', 'Personagem_Lado3.png')),

                       pygame.image.load(os.path.join('Imagens', 'Personagem_Esquerda1.png')),
                       pygame.image.load(os.path.join('Imagens', 'Personagem_Esquerda2.png')),
                       pygame.image.load(os.path.join('Imagens', 'Personagem_Esquerda3.png')),

                       pygame.image.load(os.path.join('Imagens', 'Personagem_Tras1.png')),
                       pygame.image.load(os.path.join('Imagens', 'Personagem_Tras2.png'))]
        self.image = self.frames[0]
        self.i = 0

    '''ANIMAÇÃO DO PERSONAGEM PARADO'''
    def updatePerson(self):
        self.image = self.frames[self.i%2]
        self.i += 1

    '''ANIMAÇÃO PARA PERSONAGEM IR PARA ESQUERDA'''
    def updateEsquerda(self, pos_atual):
        pos_final = (pos_atual[0] - 150, pos_atual[1]) 
        while(pos_atual != pos_final):
            clock.tick(10)
            pos_atual = (pos_atual[0] - 15, pos_atual[1])
            self.image = self.frames[6 + (self.i%2)]
            self.i += 1
            screen.fill(BLACK)
            desenha_tabuleiro(200)
            screen.blit(self.image, pos_atual)
            pygame.display.update()

    '''ANIMAÇÃO PARA PERSONAGEM IR PARA DIREITA'''
    def updateDireita(self, pos_atual):
        pos_final = (pos_atual[0] + 150, pos_atual[1]) 
        while(pos_atual != pos_final):
            clock.tick(10)
            pos_atual = (pos_atual[0] + 15, pos_atual[1])
            self.image = self.frames[3 + (self.i%2)]
            self.i += 1
            screen.fill(BLACK)
            desenha_tabuleiro(200)
            screen.blit(self.image, pos_atual)
            pygame.display.update()

    '''ANIMAÇÃO PARA PERSONAGEM IR PARA BAIXO'''    
    def updateDown(self, pos_atual):
        pos_final = (pos_atual[0], pos_atual[1] + 150) 
        while(pos_atual != pos_final):
            clock.tick(10)
            pos_atual = (pos_atual[0], pos_atual[1] + 15)
            self.image = self.frames[(self.i%2)]
            self.i += 1
            screen.fill(BLACK)
            desenha_tabuleiro(200)
            screen.blit(self.image, pos_atual)
            pygame.display.update()
    
    '''ANIMAÇÃO PARA PERSONAGEM IR PARA CIMA'''
    def updateUp(self, pos_atual):
        pos_final = (pos_atual[0], pos_atual[1] - 150) 
        while(pos_atual != pos_final):
            clock.tick(10)
            pos_atual = (pos_atual[0], pos_atual[1] - 15)
            self.image = self.frames[9 + (self.i%2)]
            self.i += 1
            screen.fill(BLACK)
            desenha_tabuleiro(200)
            screen.blit(self.image, pos_atual)
            pygame.display.update()

    '''FUNÇÃO DO TIRO'''
    def tiro(self, ambiente, ref):
        hor = ref % 4
        vert = ref // 4
        pos_atual = ((hor * 197 + 50), (vert * 197 + 17))  

        '''DISPARO PRA DIREITA'''
        if(hor + 1 < 4 and ambiente[ref + 1]['Wumpus']):
            Musicas.somTiro()     
            pos_tiro = (pos_atual[0] + 120, pos_atual[1] + 60)
            pos_final = (pos_tiro[0] + 150, pos_tiro[1])
            while(pos_tiro != pos_final):
                clock.tick(10)
                pos_tiro = (pos_tiro[0] + 15, pos_tiro[1])
                self.image = self.frames[5]
                self.i += 1
                screen.fill(BLACK)
                desenha_tabuleiro(200)
                screen.blit(self.image, pos_atual)
                pygame.draw.rect(screen, YELLOW, pygame.Rect(pos_tiro[0], pos_tiro[1], 10, 10))
                pygame.display.update()
            Musicas.somMorreu()
            
        '''DISPARO PRA ESQUERDA'''
        if(hor - 1 >= 0 and ambiente[ref - 1]['Wumpus']):
            Musicas.somTiro()     
            pos_tiro = (pos_atual[0], pos_atual[1] + 60)
            pos_final = (pos_tiro[0] - 150, pos_tiro[1])
            while(pos_tiro != pos_final):
                clock.tick(10)
                pos_tiro = (pos_tiro[0] - 15, pos_tiro[1])
                self.image = self.frames[8]
                self.i += 1
                screen.fill(BLACK)
                desenha_tabuleiro(200)
                screen.blit(self.image, pos_atual)
                pygame.draw.rect(screen, YELLOW, pygame.Rect(pos_tiro[0], pos_tiro[1], 10, 10))
                pygame.display.update()
            Musicas.somMorreu()

        '''DISPARO PRA BAIXO'''
        if(vert + 1 < 4 and ambiente[ref + 4]['Wumpus']):
            Musicas.somTiro()     
            pos_tiro = (pos_atual[0] + 90, pos_atual[1] + 90)
            pos_final = (pos_tiro[0], pos_tiro[1] + 150)
            while(pos_tiro != pos_final):
                clock.tick(10)
                pos_tiro = (pos_tiro[0], pos_tiro[1] + 15)
                self.image = self.frames[2]
                self.i += 1
                screen.fill(BLACK)
                desenha_tabuleiro(200)
                screen.blit(self.image, pos_atual)
                pygame.draw.rect(screen, YELLOW, pygame.Rect(pos_tiro[0], pos_tiro[1], 10, 10))
                pygame.display.update()
            Musicas.somMorreu()

        '''DISPARO PRA CIMA'''
        if(vert - 1 >= 0 and ambiente[ref - 4]['Wumpus']):
            Musicas.somTiro()     
            pos_tiro = (pos_atual[0] + 100, pos_atual[1] + 40)
            pos_final = (pos_tiro[0], pos_tiro[1] - 150)
            while(pos_tiro != pos_final):
                clock.tick(10)
                pos_tiro = (pos_tiro[0], pos_tiro[1] - 15)
                self.image = self.frames[10]
                self.i += 1
                screen.fill(BLACK)
                desenha_tabuleiro(200)
                screen.blit(self.image, pos_atual)
                pygame.draw.rect(screen, YELLOW, pygame.Rect(pos_tiro[0], pos_tiro[1], 10, 10))
                pygame.display.update()
            Musicas.somMorreu()

    '''ANIMAÇÂO DE CAIR NO BURACO'''
    def cairBuraco(self, ref):
        aux = 0
        pos_atual = (ref % 4 * 197 + 75, ref // 4 * 197 + 75)
        Musicas.somPoco()
        while(aux < 5):
            x_poco = ((ref % 4) * 200) + 100
            y_poco = ((ref // 4) * 200) + 100
            clock.tick(10)
            self.image = pygame.transform.smoothscale(self.image, (100 - aux * 15, 100 - aux * 15) )
            aux += 1
            screen.fill(BLACK)
            desenha_tabuleiro(200)
            screen.blit(Imagem_buraco, (x_poco - 74, y_poco - 74))
            screen.blit(self.image,pos_atual)
            pygame.display.update()

'''Cria a tela do pygamegame'''
class Menu():
    def __init__(self, tm):
        self.tm = tm
        self.menu = open('Arquivos/Menu.txt', 'r')
        self.personagem = Person([100,100])
        self.i = 0
    
    '''MENU LATERAL PARA RESUMO'''
    def menuLateral(self):
        texto = self.menu.readlines()
        for linha in texto :
            screen.blit(font.render(linha, True, BLACK), [950, 200])
            
    '''FUNÇÃO QUE DESENHA O TABULEIRO'''
    def draw(self):
        desenha_tabuleiro(self.tm)
        self.menuLateral()

    '''FUNÇÃO QUE MOSTRA UM DETERMINADO QUADRADO'''
    def view_rect(self, ref, ambiente):
        '''99 É A REFERENCIA PARA PRINTAR TODO TABULEIRO'''
        if(0 <= ref < 16):
            if(ref == 99):
                for i in range(0, 16, +1):
                    if ambiente[i]['Wumpus']:
                        x_wumpus = ((i % 4) * self.tm) + 100
                        y_wumpus = ((i // 4) * self.tm) + 100
                        screen.blit(Imagem_wumpus, (x_wumpus - 74, y_wumpus - 74))
                    else:

                        if ambiente[i]['Poço']:
                            x_poco = ((i % 4) * self.tm) + 100
                            y_poco = ((i // 4) * self.tm) + 100
                            screen.blit(Imagem_buraco, (x_poco - 74, y_poco - 74))
                        else:

                            if ambiente[i]['Ouro']:
                                x_ouro = ((i % 4) * self.tm) + 100
                                y_ouro = ((i // 4) * self.tm) + 100
                                screen.blit(Imagem_Ouro, (x_ouro - 74, y_ouro - 74))
                            else:

                                if ambiente[i]['Fedor']:
                                    fedor_text = font.render('Fedor', True, MARROM_c)
                                    x_Fedor = ((i % 4) * self.tm) + 40
                                    y_Fedor = ((i // 4) * self.tm) + 20
                                    screen.blit(fedor_text, [x_Fedor, y_Fedor])

                                if ambiente[i]['Brisa']:
                                    brisa_text = font.render('Brisa', True, ROSA_c)
                                    x_brisa = ((i % 4) * self.tm) + 40
                                    y_brisa = ((i // 4) * self.tm) + 60
                                    screen.blit(brisa_text, [x_brisa, y_brisa])

                    screen.blit(pygame.font.SysFont(None, 150).render('G', True, BLACK), [970, 100])
                    screen.blit(pygame.font.SysFont(None, 150).render('A', True, BLACK), [970, 180])
                    screen.blit(pygame.font.SysFont(None, 150).render('M', True, BLACK), [970, 260])
                    screen.blit(pygame.font.SysFont(None, 150).render('E', True, BLACK), [970, 340])
                    screen.blit(pygame.font.SysFont(None, 150).render('O', True, BLACK), [970, 450])
                    screen.blit(pygame.font.SysFont(None, 150).render('V', True, BLACK), [970, 530])
                    screen.blit(pygame.font.SysFont(None, 150).render('E', True, BLACK), [970, 610])
                    screen.blit(pygame.font.SysFont(None, 150).render('R', True, BLACK), [970, 690])

            else:
                x = ((ref % 4) * self.tm) + 100
                y = ((ref // 4) * self.tm) + 100
                pygame.draw.circle(screen, YELLOW, (x, y), 90)
                pygame.draw.circle(screen, BLACK, (x, y), 88, 1)
                pygame.draw.circle(screen, BLACK, (x, y), 85, 2)
                
                screen.blit(self.personagem.image, (x-60,y-60))
                self.personagem.updatePerson()

                '''CRIA OS TEXTOS A PARTIR DA VARIAVEL'''
                if ambiente[ref]['Wumpus']:
                    screen.blit(Imagem_wumpus, (x - 74, y - 74))
                elif ambiente[ref]['Ouro']:
                    screen.blit(Imagem_Ouro, (x - 74, y - 74))
                elif ambiente[ref]['Poço']:
                    screen.blit(Imagem_buraco, (x - 74, y - 74))
                else:
                    if ambiente[ref]['Brisa']:
                        screen.blit(pygame.font.SysFont(None, 150).render('BRISA', True, BLACK), [830, 100])
                    if ambiente[ref]['Fedor']:
                        screen.blit(pygame.font.SysFont(None, 150).render('FEDOR', True, MARROM_c), [820, 200])