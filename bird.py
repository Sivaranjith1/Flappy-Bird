import pygame

class Bird:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.radius = 10
        self.alive = True

        self.jumping = False
        self.speed = 0
        self.maxSpeed = 7
        self.gravity = 0.7

    def move(self):
        if not self.alive:
            return


        self.speed += self.gravity
        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed
        elif self.speed > 0:
            self.jumping = False
        
        self.y += int(self.speed)
        self.checkBorderCollision()

    def jump(self):
        if not self.jumping:
            self.speed = -10 
            self.jumping = True

    def checkBorderCollision(self):
        if self.y - self.radius <= 0:
            self.alive = False
        elif self.y + self.radius >= 500:
            self.alive = False

    def checkPipeCollision(self, pipes):
        for pipe in pipes:
            yCollision = False
            #top collision
            if self.y - self.radius <= pipe.gapTop:
                yCollision = True
            elif self.y + self.radius >= pipe.y:
                yCollision = True

            if yCollision and self.x - self.radius <= pipe.x + pipe.width and self.x + self.radius >= pipe.x:
                self.alive = False

    def draw(self, win):
        pygame.draw.circle(win, (255, 170, 0), (self.x, self.y), self.radius)
