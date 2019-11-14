import pygame
from bird import Bird
from pipe import Pipe
from nn import NN

#Init for pygame
pygame.init()
fps = 30

pygame.font.init()
comicSans = pygame.font.SysFont('Comic Sans MS', 30)

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

#objects
players = [] #Bird(50,250)
pipes = [Pipe()]
nns = []

numberOfNN = 50

#generate machine learning bird
def newNN():
    for _ in range(numberOfNN):
        nns.append(NN())

def findBestNN():
    highestScore = -1
    parent = None
    for nn in nns:
        distance = 0
        try:
            distance = 1/(abs((pipes[-2].gapTop + (pipes[-2].gapDistanse)/2) - nn.bird.y)*100 + 1)
        except:
            distance = 0
        if distance >= 0.5:
            distance = 0.5
        score = nn.bird.score + distance
        if score > highestScore:
            parent = nn
            highestScore = score


    return parent

def createChildren(parent):
    for _ in range(numberOfNN-1):
        nns.append(NN.child(parent))
    nns.append(parent)

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

    for nn in nns:
        if nn.bird.alive:
            nn.bird.draw(win)
        nn.bird.checkPipeCollision(pipes)

    
    scoreBoard = comicSans.render('Score: {}'.format(nns[0].bird.score), False, (0,0,0))
    win.blit(scoreBoard, (0,0))

    pygame.display.update()

#will handle all key presses
def handleKeyPress():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        #players[0].jump()
        pass


#everything that have to do with pshycis and logic
def logic():
    global nns
    global pipes
    for player in players:
        player.move()

    for pipe in pipes:
        pipe.move()

    someoneIsAlive = False
    for nn in nns:
        jump = nn.predict(pipes)
        if jump == 1:
            nn.bird.jump()

        nn.bird.move()

        if nn.bird.alive == True:
            someoneIsAlive = True


    if not someoneIsAlive:
        parent = findBestNN()
        nns = []
        pipes = [Pipe()]
        createChildren(parent)
    generatePipe()

run = True
newNN()
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