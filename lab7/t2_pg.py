import pygame

pygame.init()

songs=[
    "lab7\\Smeshariki_-_Tema_Bibi_73308639.mp3",
    "lab7\\Smeshariki_-_Indijjskijj_chajj_74725116.mp3",
    "lab7\\Smeshariki_-_Gorod_Omsk_48225854.mp3"
]
ind=0
pygame.mixer.music.load(songs[ind]) 
pygame.mixer.music.play()

screen=pygame.display.set_mode((800,450))
pygame.display.set_caption("Music Player")
bc=pygame.image.load("lab7\\scale_1200.jpeg")
bc=pygame.transform.scale(bc,(800,450))

done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_1:
                pygame.mixer.music.pause()
            elif event.key==pygame.K_2:
                pygame.mixer.music.unpause()
            elif event.key==pygame.K_3:
                ind=(ind+1)%len(songs)
                pygame.mixer.music.load(songs[ind])
                pygame.mixer.music.play()
            elif event.key==pygame.K_4:
                ind=(ind-1)%len(songs)
                pygame.mixer.music.load(songs[ind])
                pygame.mixer.music.play()
    
    screen.blit(bc,(0,0))
    pygame.display.flip()
    pygame.time.delay(20)
