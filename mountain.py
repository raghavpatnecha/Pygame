import os, pygame;
from pygame.locals import *

pygame.init();
clock = pygame.time.Clock()
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Mountains")
screen = pygame.display.set_mode([600, 382], 0, 32)

sky = pygame.Surface((600, 255))
r = 0;
g = 64;
b = 128

for l in range(0, 255):
    pygame.draw.rect(sky, (r, g, b), (0, l - 1, 600, l))
    r = r + 1;
    g = g + 1;
    b = b + 1
    if r >= 255: r = 255
    if g >= 255: g = 255
    if b >= 255: b = 255

ground = pygame.Surface((600, 128))
r = 192;
g = 255;
b = 192

for l in range(0, 128):
    pygame.draw.rect(ground, (r, g, b), (0, l - 2, 600, l))
    r = r - 2;
    g = g - 2;
    b = b - 2
    if r <= 0: r = 0
    if g <= 0: g = 0
    if b <= 0: b = 0

# Add in an extra surface for the mountains
mountain = pygame.Surface((600, 128))
mountain.set_colorkey([0, 0, 0])  # Black is transparent
r = 96;
g = 64;
b = 255

for l in range(0, 128):
    pygame.draw.rect(mountain, (r, g, b), (0, l - 2, 600, l))
    r = r + 2;
    g = g + 2;
    b = b + 2
    if r >= 255: r = 255
    if g >= 255: g = 255
    if b >= 255: b = 255

# Draw some black (Transparent) polygons to create mountain peaks
# The screen is 600 wide so I've drawn 10 polygons at 60 pixels wide each
pygame.draw.polygon(mountain, [0, 0, 0], [(0, 0), (60, 0), (60, 10), (0, 40)])
pygame.draw.polygon(mountain, [0, 0, 0], [(60, 0), (120, 0), (120, 30), (60, 10)])
pygame.draw.polygon(mountain, [0, 0, 0], [(120, 0), (180, 0), (180, 20), (120, 30)])
pygame.draw.polygon(mountain, [0, 0, 0], [(180, 0), (240, 0), (240, 50), (180, 20)])
pygame.draw.polygon(mountain, [0, 0, 0], [(240, 0), (300, 0), (300, 40), (240, 50)])
pygame.draw.polygon(mountain, [0, 0, 0], [(300, 0), (360, 0), (360, 10), (300, 40)])
pygame.draw.polygon(mountain, [0, 0, 0], [(360, 0), (420, 0), (420, 35), (360, 10)])
pygame.draw.polygon(mountain, [0, 0, 0], [(420, 0), (480, 0), (480, 45), (420, 35)])
pygame.draw.polygon(mountain, [0, 0, 0], [(480, 0), (540, 0), (540, 42), (480, 45)])
pygame.draw.polygon(mountain, [0, 0, 0], [(540, 0), (600, 0), (600, 15), (540, 42)])

screen.blit(sky, (0, 0))
screen.blit(ground, (0, 255))
screen.blit(mountain, (0, 128))
pygame.display.update()

pygame.time.wait(30000)
