import pygame
from bird import Bird
from pipe import Pipe

#Init for pygame
pygame.init()
fps = 30

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

#objects
players = [Bird(50,250)]
pipes = [Pipe()]

#create new pipes
def generatePipe():
    distance = 250
    lastPipe = pipes[-1]

    if 500 - lastPipe.x >= distance:
        pipes.append(Pipe())

#the drawing function
def draw():
    win.fill((0, 163, 204))

    for player in players:
        player.draw(win)
        player.checkPipeCollision(pipes)

    for pipe in pipes:
        pipe.draw(win)

    pygame.display.update()

#will handle all key presses
def handleKeyPress():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        players[0].jump()


#everything that have to do with pshycis and logic
def logic():
    for player in players:
        player.move()

    for pipe in pipes:
        pipe.move()

    generatePipe()

run = True
while run:
    pygame.time.delay(30)
    timedelta = clock.tick(30)
    timedelta /= 1000
    win.fill((0,0,255))

    handleKeyPress()

    logic()
    draw()

    #quiting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()