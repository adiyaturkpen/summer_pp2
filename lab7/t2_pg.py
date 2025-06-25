import pygame
import sys
pygame.init()

songs=[
    "lab7\Smeshariki_-_Tema_Bibi_73308639.mp3",
"lab7\Smeshariki_-_Indijjskijj_chajj_74725116.mp3",
"lab7\Smeshariki_-_Gorod_Omsk_48225854.mp3"
]
ind=0
pygame.mixer.music.load(songs[ind]) 
pygame.mixer.music.play()

screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Music Player")
bc=pygame.image.load("lab7\\scale_1200.jpeg")
bc=pygame.transform.scale(bc,(800,450))

while 1:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
        elif i.type==pygame.KEYUP:
            if i.key==pygame.K_1:
                pygame.mixer.music.pause()
            elif i.key==pygame.K_2:
                pygame.mixer.music.unpause()
            elif i.key==pygame.K_3:
                ind=(ind+1)%len(songs)
                pygame.mixer.music.load(songs[ind])
                pygame.mixer.music.play()
            elif i.key==pygame.K_4:
                ind=(ind-1)%len(songs)
                pygame.mixer.music.load(songs[ind])
                pygame.mixer.music.play()
    screen.blit(bc, (0, 0))
    pygame.display.flip()
    pygame.time.delay(20)
