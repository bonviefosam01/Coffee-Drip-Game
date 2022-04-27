#Bonvie Fosam

import pygame, sys, random
from pygame.locals import *

#Constants
screenHeight= 500
screenWidth= 500
blue=(0,0,255)
brown = (139, 69, 19)
rainNum = 2
rainSize = 5
vel = 10
height = 40
width = 60
FPS = 20
gravity = 10
score = 10

starting = 0
started = 1

def create_window (dimensions, caption):
    pygame.init()
    pygame.display.set_caption(caption)
    window = pygame.display.set_mode(dimensions)
    return window

def basketpic():
	basket = pygame.image.load("images/basket.jpg")
    return basket

def startbasket(basketRect):
    basketPosX = 0
    basketPosY = 450
    basketRect.bottomleft = (basketPosX, basketPosY)
    return basketPosX, basketPosY

def make_coffee_rain():
	rainNum = 2
	rain=[]
    for q in range(rainNum):
        rainX = random.randrange(0,screenWidth)
        rainY = random.randrange(0,screenHeight)
        rain.append([rainX,rainY])
    clock = pygame.time.Clock()

def movebasket(basketX, basketY, event):
    if event.key == K_RIGHT:
        basketX += 10
    if event.key == K_LEFT:
        basketX -=10
    if event.key == K_UP:
        basketY += -10 
    if event.key == K_DOWN:
        basketY += 10
    return basketX, basketY	

def hit(basketRect, rainRect):
    return basket.colliderect(rainRect)


def play_game():
	pygame.init()
    DISPLAYSURF = pygame.display.set_mode((500,500))
    pygame.display.set_caption("CATCH THE COFFEE!")
    window.fill((135,206,250))

    basket = basketpic()
    basketRect = basket.get_rect()
    basketRect.bottomleft = (0, 450)


    run = True
    while run:
        pygame.time.delay(100) #this is in milliseconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= vel
        if keys[pygame.K_RIGHT] and x < screenWidth - width:
            x += vel


    window.fill((135,206,250))
    
    for i in rain:
        i[1] += gravity

        pygame.draw.circle(window, brown, i, rainSize)

        if i[1] > height:
            i[1] = random.randrange(screenHeight)
            i[0] = random.randrange(screenWidth)

    clock.tick(FPS)
    basket = pygame.image.load("images/gamebasket.jpg")
    basketX, basketY = movebasket(basketX, basketY, event):
    #basket=pygame.draw.rect(win, (255,0,0),(x,y, width, height,))
    coffee_caught = pygame.sprite.spritecollide(i, basket, True)
    for coffee in coffee_caught:
        score += 1


    pygame.draw.rect(win,(255,255,255),(0,0,60,20))
    font = pygame.font.get_default_font()
    text = font.render("Your Score is: " + str(score) , True, (0,0,0), (255,255,255))
    screen.blit(text, (x,y))


    pygame.display.update()


        
pygame.quit()


if __name__=='__main__':
    play_game()

