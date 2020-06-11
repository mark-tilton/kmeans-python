import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random as r

import math


def Circle(radius = 100, point_count = 100):
    glBegin(GL_LINE_STRIP)
    for i in range(point_count):
        theta = i / (point_count - 1) * math.pi * 2
        glVertex3fv((math.cos(theta) * radius, math.sin(theta) * radius, 0))
    glEnd()


def dist(pointA, pointB):
    return math.sqrt((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluOrtho2D(0, display[0], 0, display[1])

    points = []
    for i in range(15):
        points.append((r.random() * display[0], r.random() * display[1]))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        for point in points:
            glPushMatrix()
            glTranslatef(point[0], point[1], 0)
            Circle(5)
            glPopMatrix()

        mouse_pos = (pygame.mouse.get_pos()[0], display[1]-pygame.mouse.get_pos()[1])
        distances = map(lambda x: dist(x, mouse_pos), points)
        distances = list(distances)
        distances.sort()
        radius = distances[2] + 2.5

        glPushMatrix()
        glTranslatef(mouse_pos[0], mouse_pos[1], 0)
        #print(f'{mouse_pos[0]}, {mouse_pos[1]}')
        
        Circle(radius=radius)
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)


main()