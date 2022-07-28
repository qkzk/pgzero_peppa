#! /usr/bin/python
"""
title: PEPPA
author: qkzk
date: 2022/07/14

Simple game for a very young kid.
"""


import math
import string

import pygame
import pgzrun
from random import choice, randint


TITLE = "PEPPA"
WIDTH = 1920
HEIGHT = 1080


OUTSIDE = (8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0)

SOUNDS = (
    sounds.bubble,
    sounds.fart,
    sounds.giggle,
    sounds.mario,
    sounds.monkey,
)

COLORS = (
    (0, 0, 100),
    (100, 0, 0),
    (0, 100, 0),
    (50, 50, 0),
    (50, 0, 50),
    (0, 50, 50),
)
LETTER_COLORS = (
    (0, 255, 255),
    (255, 255, 0),
    (255, 255, 0),
    (120, 120, 255),
    (255, 120, 120),
    (120, 255, 120),
)
LETTERS = string.ascii_lowercase


class Sprite:
    def __init__(self, image: str):
        self.image = image
        self.pos = (0, 0)
        self.actor = Actor(self.image, center=self.pos)

    def draw(self):
        self.actor.draw()

    def update(self):
        self.pos = pygame.mouse.get_pos()
        self.actor = Actor(self.image, center=self.pos)


def play_random_sound():
    choice(SOUNDS).play()


def pick_random_color():
    color[0] = choice(COLORS)


def draw_eye(eye_x, eye_y):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    distance_x = mouse_x - eye_x
    distance_y = mouse_y - eye_y

    distance = min(math.sqrt(distance_x**2 + distance_y**2), 30)
    angle = math.atan2(distance_y, distance_x)

    pupil_x = eye_x + (math.cos(angle) * distance)
    pupil_y = eye_y + (math.sin(angle) * distance)

    screen.draw.filled_circle((eye_x, eye_y), 50, color=(255, 255, 255))
    screen.draw.filled_circle((pupil_x, pupil_y), 15, color=color[0])


def new_symbol(symbol: str) -> tuple:
    fontsize = randint(60, 120)
    x = randint(0, WIDTH - fontsize)
    y = randint(0, HEIGHT - fontsize)
    owidth = 1
    color = choice(LETTER_COLORS)
    return (
        symbol.upper(),
        (x, y),
        {"fontsize": fontsize, "owidth": owidth, "ocolor": "black", "color": color},
    )


def draw_letters():
    for letter, pos, kwargs in letters:
        screen.draw.text(letter, pos, **kwargs)


def update_letters(key: str):
    letters.append(new_symbol(key))
    if len(letters) > 30:
        del letters[0]


def on_key_down():
    # if keyboard["escape"]:
    #     exit()
    if keyboard["space"]:
        play_random_sound()
        pick_random_color()
    for key in LETTERS:
        play_random_sound()
        pick_random_color()
        if keyboard[key]:
            update_letters(key)


def on_mouse_down(button):
    play_random_sound()
    pick_random_color()


def update():
    peppa.update()
    pygame.mouse.set_cursor(*OUTSIDE)


def draw():
    screen.fill(color[0])

    draw_eye(WIDTH // 2 - 100, HEIGHT // 2)
    draw_eye(WIDTH // 2 + 100, HEIGHT // 2)
    draw_letters()
    peppa.draw()


peppa = Sprite("peppa")
color = [COLORS[0]]
letters = []
pgzrun.go()
