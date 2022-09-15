import numpy as np
import pygame
from pygame.locals import *
import sys
import rotation
from math import sin, cos
import engine

points = [
    [40, 40,  90],
    [90, 40,  90],
    [90,  90,  90],
    [40,  90,  90],
    [40, 40, 40],
    [90, 40, 40],
    [90,  90, 40],
    [40,  90, 40]
]

normals = [
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1],
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1]
]

center = np.array([65, 65, 65])

indices = [
    0, 1, 2,
    2, 3, 0,
    1, 5, 6,
    6, 2, 1,
    7, 6, 5,
    5, 4, 7,
    4, 0, 3,
    3, 7, 4,
    4, 5, 1,
    1, 0, 4,
    3, 2, 6,
    6, 7, 3
]
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
point = np.array([1, 1, 1])
rot =rotation.makeRotMatrix([0.001, 0.001, 0.001])

camPos = np.array([0, 0, 0, 1], dtype="float64")
camRot = np.array([0, 0, 0], dtype="float64")
right = 20
left = -20
top = 480/640 * 20
bottom = - 480/640 * 20
near = 30
far = 100
lightPos = np.array([30, 30, 0, 1])

def normalize(a):
    mag = np.linalg.norm(a)
    return a/mag

camera = engine.Camera(near, far, right, left, top, bottom)

frames = 0
# Game loop.
while True:
    screen.fill((0, 0, 0))
    frames += 1
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if(pygame.key.get_pressed()[K_w]):
        camera.camPos += np.array([-sin(camera.camRot[1]), 0, -cos(camera.camRot[1]), 0])
    if(pygame.key.get_pressed()[K_a]):
        camera.camPos += np.array([cos(camera.camRot[1]), 0, -sin(camera.camRot[1]), 0])
    if(pygame.key.get_pressed()[K_s]):
        camera.camPos += np.array([sin(camera.camRot[1]), 0, cos(camera.camRot[1]), 0])
    if(pygame.key.get_pressed()[K_d]):
        camera.camPos += np.array([-cos(camera.camRot[1]), 0, sin(camera.camRot[1]), 0])
    if(pygame.key.get_pressed()[K_SPACE]):
        camera.camPos += np.array([0, 1, 0, 0])
    if(pygame.key.get_pressed()[K_LSHIFT]):
        camera.camPos += np.array([0, -1, 0, 0])

    if(pygame.key.get_pressed()[K_LEFT]):
        camera.camRot += np.array([0, -0.01, 0])
    if(pygame.key.get_pressed()[K_RIGHT]):
        camera.camRot += np.array([0, 0.01, 0])

    for j in range(len(indices)-1):
        i = indices[j]
        i1= indices[j+1]
        projected1 = camera.project(np.array(points[i]+[1]), 640, 480)
        projected2 = camera.project(np.array(points[i1]+[1]), 640, 480)
        
        if(projected1 != None and projected2 != None):
            #pygame.draw.polygon(screen, (255, 255, 255), [projected, projected1, projected2], 1)
            pygame.draw.line(screen, (255, 255, 255), projected1, projected2)
    
    pygame.display.flip()
    fpsClock.tick(fps)
