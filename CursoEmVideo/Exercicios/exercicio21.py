import pygame
pygame.mixer.init()
pygame.mixer.music.load('MC Pedrinho - Gol Bolinha, Gol Quadrado 2 (GR6 Explode) DJ 900 (320 kbps).mp3')
pygame.mixer_music.play()
while pygame.mixer.music.get_busy():
    continue
