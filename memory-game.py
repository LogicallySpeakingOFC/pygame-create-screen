import random, pygame, sys
from pygame.locals import *

# Set general game speed
FPS = 30

# Set the window's width and height
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

# Set speed of boxes' sliding reveals and covers
REVEALSPEED = 8

# Set size of box width and height
BOXSIZE = 40

# Set size of gap between boxes
GAPSIZE = 10

# Set number of rows and columns for board
BOARDWIDTH = 10
BOARDHEIGHT = 7
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

# Set up color pallet
GRAY       = (100, 100, 100)
NAVYBLUE   = (60, 60, 100)
WHITE      = (255, 255, 255)
RED        = (255, 0, 0)
GREEN      = (0, 255, 0)
BLUE       = (0, 0, 255)
YELLOW     = (255, 255, 0)
ORANGE     = (255, 128, 0)
PURPLE     = (255, 0, 255)
CYAN       = (0, 255, 255)

# Set colors of boxes, backgrounds, and highlight
BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

# Set shapes used for game
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

# Set colors of shapes
ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."