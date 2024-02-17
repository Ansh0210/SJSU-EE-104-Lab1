"""
Created on Wed Aug 23 10:12:25 2023

@author: Nathan Lee
"""
import pgzrun 
import pygame 
import pgzero
from pgzero.builtins import Actor
from random import randint

apple = Actor("apple", (400,300))           #apple, rotten apple, and apple with worm set as actors, with set coordinates to prevent overlap on start
orange = Actor("appleworm", (200,100))         #
pineapple = Actor("rottenapple", (100,400))      #

Hit=0       #hit counter
Miss=0      #miss counter

def draw():
    screen.clear()      #clears the screen
    apple.draw()        #draws the apple
    orange.draw()       #draws apple with worm
    pineapple.draw()    #draws rotten apple
    screen.draw.text("Hit: " +str(Hit) +"Miss: " +str(Miss), color="white", topleft=(10,10))
    #draws the hit and miss with an offset of 10 by 10 pixels
    

def place_apple():#places the apple image at a random place with teh top left coner being at somewhere between 10 and 800 pixels in the x axis and 10 and 600 pixels in the y axis
    apple.x = randint(10,800)
    apple.y = randint(10,600)


def place_orange():#places the apple with worm image at a random place with teh top left coner being at somewhere between 40 and 800 pixels in the x axis and 50 and 600 pixels in the y axis
    orange.x = randint(40,800)
    orange.y = randint(50,600)


def place_pineapple():#places the rotten apple image at a random place with teh top left coner being at somewhere between 80 and 800 pixels in the x axis and 100 and 600 pixels in the y axis
    pineapple.x = randint(80,800)
    pineapple.y = randint(100,600)    


def on_mouse_down(pos):# check happens everytime you click
    global Hit  #checks for a hit or a miss
    global Miss
    if apple.collidepoint(pos):#click collides with an apple execute this
        print("Good shot!")
        place_apple()
        Hit=Hit+1 #hitcounter plus 1

    else:
        print("Missed!")
        Miss=Miss+1 #miss counter plus 1
        if randint(1,10)%2 : #randomly move the orange or the pineapple
            place_orange()
        else:
            place_pineapple()


pgzrun.go()