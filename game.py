import pygame
import os
import time
import random

#load images
Red_space_ship=pygame.image.load(os.path.join('assets','pixel_ship_red_small.png')) #cargar la imagen on os,
#basicamente lo que hace os.path.join es assets\pixel_ship_red_small.png
Blue_space_ship=pygame.image.load('assets/pixel_ship_blue_small.png') #cargar la imagen directamente a pygame
a= os.path.join('assets','pixel_ship_red_small.png')
print(a)
print(Blue_space_ship)
