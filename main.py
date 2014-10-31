import pygame
import sys
from geometry import Point
import random
from renderer import Renderer


random.seed()

pygame.init()
window = pygame.display.set_mode((800, 600))

rend = Renderer(window)

point_list = Point.generate_points(100, -500, 500, -500, 500)
map(lambda x: rend.queue_point(x), point_list)

rend.draw()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)
#pygame.draw.circle