import pygame

window = pygame.display.set_mode((400, 400))
pygame.display.update()

gameOver = False

class Rect:
	def __init__(self, xcor, ycor):
		self.xcor = xcor
		self.ycor = ycor
		self.width = 20
		self.height = 20
		self.color = (55, 250, 86)
	
	def draw(self, window):
		pygame.draw.rect(
			window, self.color, 
			(self.xcor, self.ycor, self.width, self.height)
		)


def update():
	pygame.display.update()


rect = Rect(100, 100)
# while not gameOver:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			gameOver = True
# 	rect.draw(window)
# 	update()


pygame.quit()
# quit()


def moveRight(rec):
	rec.xcor = rec.xcor + 10
	return

print(rect.xcor)
moveRight(rect)
print(rect.xcor)
