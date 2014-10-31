import pygame
import geometry as g

BLACK = (0, 0, 0)


class Renderer:
	def __init__(self, window):
		self.window = window
		self.window.fill((255, 255, 255))
		#fill with white 
	
	def queue_point(self, point, color=BLACK):
		pygame.draw.circle(self.window, color, self.local_to_world(point.tup()), 2, 0)

	def queue_segment(self, segment, color=BLACK):
		pygame.draw.line(self.window, color, self.local_to_world(segment.start.tup()), self.local_to_world(segment.end.tup())) 


	def local_to_world(self, tup):
		new_x = int(tup[0] + self.window.get_width()/2)
		new_y = int(self.window.get_height()/2 - tup[1]) 
		return (new_x, new_y)


	def draw(self):
		pygame.display.update()
		self.window.fill((255, 255, 255))

if __name__ =='__main__':

	test_point = g.Point(0, 0)
	test_point2 = g.Point(100,50)
	test_segment = g.Segment(test_point, test_point2)

	pygame.init()
	window = pygame.display.set_mode((800, 600))
	rend = Renderer(window)
	rend.queue_point(test_point)
	rend.queue_segment(test_segment)
	rend.draw()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)

