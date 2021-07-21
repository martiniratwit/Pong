import pygame
import sys
import random

WIDTH = 800
HEIGHT = 800

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    #Create ball class, Utilized design from Dr Isaac Triguero

class Ball():
    RADIUS = 10
    fgColor = pygame.Color("white")
    bgColor = pygame.Color("black")

        #Velocity for each axis
    xVelocity = 4
    yVelocity = 4

    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

        #Create Sphere for ball
    def show(self, screen, color):
        pygame.draw.circle(screen, color, (self.xPos, self.yPos), self.RADIUS)

        #Moves ball across the screen
    def move(self, screen):
        self.show(screen, self.bgColor)
        self.xPos += self.xVelocity
        self.yPos += self.yVelocity
        self.show(screen, self.fgColor)

    #Class for game to run
class Pong():

        #General parameters for game
    WIDTH = 800
    HEIGHT = 800

    pygame.display.set_caption("Pong")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = pygame.Rect(WIDTH - 20, HEIGHT / 2 - 70, 10, 140)
    player2 = pygame.Rect(10, HEIGHT / 2 - 70, 10, 140)
    playerMoveSpeed = 0
    player2MoveSpeed = 0

    ball = Ball(WIDTH / 2, HEIGHT / 2)

    def __init__(self):
        pass

    def playerNum(self, playNum):
        self.playNum = playNum

        #Prints Paddles and allows their movement
    def playerMove(self):
        pygame.draw.rect(self.screen, pygame.Color("black"), self.player)
        pygame.draw.rect(self.screen, pygame.Color("black"), self.player2)
        self.player.y -= self.playerMoveSpeed
        if self.player.top < 0:
            self.player.top = 0
        if self.player.bottom > self.HEIGHT:
            self.player.bottom = self.HEIGHT

        self.player2.y -= self.player2MoveSpeed
        if self.player2.top < 0:
            self.player2.top = 0
        if self.player2.bottom > self.HEIGHT:
            self.player2.bottom = self.HEIGHT

        pygame.draw.rect(self.screen, pygame.Color("white"), self.player)
        pygame.draw.rect(self.screen, pygame.Color("white"), self.player2)

    def player2Move(self):
        pygame.draw.rect(self.screen, pygame.Color("black"), self.player2)

        self.player2.y += self.ball.yVelocity
        if self.player2.top < 0:
            self.player2.top = 0
        if self.player2.bottom > self.HEIGHT:
            self.player2.bottom = self.HEIGHT

        pygame.draw.rect(self.screen, pygame.Color("white"), self.player2)



        #Detect collision between ball and paddle
    def ballCollision(self):
        if self.ball.xPos >= self.player.left:
            if self.ball.yPos < self.player.top:
                self.ball.show(self.screen, self.ball.bgColor)
                self.ball.xPos = self.WIDTH / 2
                self.ball.yPos = self.HEIGHT / 2
                self.ball.xVelocity *= -1

            elif self.ball.yPos > self.player.bottom:
                self.ball.show(self.screen, self.ball.bgColor)
                self.ball.xPos = self.WIDTH / 2
                self.ball.yPos = self.HEIGHT / 2
                self.ball.xVelocity *= -1

            else:
                    #Randomize ball trajecory when hit
                newX = random.randint(3,6)
                newY = 8 - newX

                self.ball.xVelocity = newX
                self.ball.yVelocity = newY

                self.ball.xVelocity *= -1

        if self.ball.xPos <= self.player2.right:
            if self.ball.yPos < self.player2.top:
                self.ball.show(self.screen, self.ball.bgColor)
                self.ball.xPos = self.WIDTH / 2
                self.ball.yPos = self.HEIGHT / 2
                self.ball.xVelocity *= -1

            elif self.ball.yPos > self.player2.bottom:
                self.ball.show(self.screen, self.ball.bgColor)
                self.ball.xPos = self.WIDTH / 2
                self.ball.yPos = self.HEIGHT / 2
                self.ball.xVelocity *= -1

            else:
                # Randomize ball trajecory when hit
                newX = random.randint(3, 6)
                newY = 8 - newX

                self.ball.xVelocity = newX
                self.ball.yVelocity = newY

                self.ball.xVelocity *= -1

        if self.ball.xPos >= self.WIDTH:
            self.ball.xVelocity *= -1
        if self.ball.xPos <= self.player2.right:
            self.ball.xVelocity *= -1
        if self.ball.yPos >= self.HEIGHT:
            self.ball.yVelocity *= -1
        if self.ball.yPos <= 0:
            self.ball.yVelocity *= -1

    def play(self):

            #Initializes Game
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    sys.exit()



                    #Takes key press to allow for movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        playing = False
                    if event.key == pygame.K_DOWN:
                        self.playerMoveSpeed -= 7
                    if event.key == pygame.K_UP:
                        self.playerMoveSpeed += 7

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.playerMoveSpeed += 7
                    if event.key == pygame.K_UP:
                        self.playerMoveSpeed -= 7

                #Add ball movement and collison
            self.player2Move()
            self.ballCollision()
            self.ball.move(self.screen)
            pygame.draw.rect(self.screen, pygame.Color("white"), self.player)
            self.playerMove()
            pygame.display.flip()
            self.clock.tick(60)

def mainMenu():
    while True:


                    # Sending instance of game object to client
        pong = Pong()
        screen.fill(pygame.Color("black"))
        pong.play()
        screen.fill(pygame.Color("black"))



        pygame.display.update()
        clock.tick(60)

mainMenu()