import pygame
import sys
import time
from geometry import Point
import random
from renderer import Renderer
from algorithm import Algorithm


random.seed()

pygame.init()
window = pygame.display.set_mode((800, 600))

rend = Renderer(window)

point_list = Point.generate_points(1000, -200, 200, -200, 200)


algo = Algorithm(point_list)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)
	algo.next_step()
	rend.queue_algorithm(algo)
	rend.draw()
	time.sleep(0.01)
#pygame.draw.circle