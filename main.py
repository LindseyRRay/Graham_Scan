import pygame
import sys
from geometry import Point
import random
from renderer import Renderer
from algorithm import Algorithm


random.seed()

pygame.init()
window = pygame.display.set_mode((800, 600))

rend = Renderer(window)

point_list = Point.generate_points(200, 0, 100, 0, 100)
algo = Algorithm(point_list)

#rend.queue_algorithm(algo)

algo.next_step()
algo.next_step()

#print algo.state_manager.current_state

rend.queue_algorithm(algo)

rend.draw()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)
#pygame.draw.circle