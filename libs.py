
def nome():
    file = open ("historia.txt", "a")
    file.write("\n")
    file.write(str(input("Insira Nome: ")))
    file.write("\n")
    file.write(str(input("Insira Email: ")))
    file.write("\n")
    file.close()
    
def printMenu():
    pg.mixer.music.load('musica.wav')
    pg.mixer.music.play(-1) 
    text = fonte.render('Bem vindo/a!', True, discos[0])
    screen.blit(text, (size[0]//2-(text.get_rect().width//2),size[1]//5-(text.get_rect().height//2)))
    text = fonte.render('Jogar ou assistir a resolução?', True, discos[0])
    screen.blit(text, (size[0]//2-(text.get_rect().width//2),size[1]//3-(text.get_rect().height//2)))
    text = fonte.render('Jogar', True, discos[0])
    opcao1 = pg.draw.rect(screen, discos[0], ((size[0]//4) - ((text.get_rect().width//2)+10), (size[1]//2) - ((text.get_rect().height//2)+10), \
                                         text.get_rect().width + 20, text.get_rect().height + 20), 5)
    screen.blit(text, ((size[0]//4) - (text.get_rect().width//2), (size[1]//2) - (text.get_rect().height//2)))
    text = fonte.render('Assistir', True, discos[0])
    opcao2 = pg.draw.rect(screen, discos[0], ((3*(size[0]//4)) - ((text.get_rect().width//2)+10), (size[1]//2) - ((text.get_rect().height//2)+10), \
                                         text.get_rect().width + 20, text.get_rect().height + 20), 5)
    screen.blit(text, ((3*(size[0]//4)) - (text.get_rect().width//2), (size[1]//2) - (text.get_rect().height//2)))
    pg.display.update()
    return opcao1, opcao2