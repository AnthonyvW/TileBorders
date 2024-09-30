import pygame
import random

from SpriteSheet import SpriteSheet

# game window
pygame.init()
map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 3, 3, 0],
    [0, 0, 2, 1, 2, 2, 1, 2, 0, 2, 2, 3, 1, 3, 2, 2, 3, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 2, 1, 3, 1, 3, 1, 2, 0, 0],
    [0, 0, 2, 1, 2, 2, 1, 2, 0, 3, 3, 3, 1, 3, 3, 3, 2, 0],
    [0, 0, 2, 1, 2, 2, 1, 2, 0, 2, 2, 2, 3, 2, 2, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 1, 3, 3, 3, 2, 0],
    [0, 0, 2, 1, 2, 2, 1, 2, 0, 2, 1, 3, 1, 3, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 3, 1, 3, 2, 2, 0, 0],
    [0, 0, 1, 0, 0, 2, 0, 1, 3, 0, 3, 2, 0, 2, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
'''
map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 3, 2, 0, 0],
    [0, 0, 1, 3, 1, 0, 1, 2, 1, 0, 3, 2, 3, 0, 3, 3, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 2, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 3, 3, 3, 0, 3, 0, 3, 0, 0, 1, 3, 0, 3, 0, 0, 0],
    [0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 3, 3, 3, 0, 3, 0, 3, 0, 3, 3, 3, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
'''

Scale = 8
SCREEN_WIDTH = (len(map[0]) - 2) * 8 * Scale
SCREEN_HEIGHT = (len(map) - 2) * 8 * Scale

# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
# Title
pygame.display.set_caption('Tile Border Test')


class Tile():
    def __init__(self, TileSheet, variations = 1):
        self.tileTextures = []
        self.variations = variations - 1
        for i in range(variations):
            self.tileTextures.append([])
            xOffset = 16 * i
            yOffset = 0

            self.tileTextures[i].append(TileSheet.get_image_scale(0 * 4 + xOffset, 0 * 4 + yOffset, 4, 4, Scale))
            self.tileTextures[i].append(TileSheet.get_image_scale(1 * 4 + xOffset, 0 * 4 + yOffset, 4, 4, Scale))
            self.tileTextures[i].append(TileSheet.get_image_scale(0 * 4 + xOffset, 1 * 4 + yOffset, 4, 4, Scale))
            self.tileTextures[i].append(TileSheet.get_image_scale(1 * 4 + xOffset, 1 * 4 + yOffset, 4, 4, Scale))

            yOffset = 8
            # Get Center Block Texture
            self.tileTextures[i].append(TileSheet.get_image_scale(1 * 4 + xOffset, 1 * 4 + yOffset, 8, 8, Scale))

            # Get Top Row Textures
            self.tileTextures[i].append(TileSheet.get_image_scale(0 * 4 + xOffset, 0 * 4 + yOffset, 4, 4, Scale))
            self.tileTextures[i].append(TileSheet.get_image_scale(1 * 4 + xOffset, 0 * 4 + yOffset, 4, 4, Scale))
            self.tileTextures[i].append(TileSheet.get_image_scale(2 * 4 + xOffset, 0 * 4 + yOffset, 4, 4, Scale))
            self.tileTextures[i].append(TileSheet.get_image_scale(3 * 4 + xOffset, 0 * 4 + yOffset, 4, 4, Scale))

            # Get Middle 2 Rows Textures
            self.tileTextures[i].append(TileSheet.get_image_scale(0 * 4 + xOffset, 1 * 4 + yOffset, 4, 4, Scale))
            self.tileTextures[i].append(TileSheet.get_image_scale(0 * 4 + xOffset, 2 * 4 + yOffset, 4, 4, Scale))
            self.tileTextures[i].append(TileSheet.get_image_scale(3 * 4 + xOffset, 1 * 4 + yOffset, 4, 4, Scale))
            self.tileTextures[i].append(TileSheet.get_image_scale(3 * 4 + xOffset, 2 * 4 + yOffset, 4, 4, Scale))

            # Get Bottom Row Textures
            self.tileTextures[i].append(TileSheet.get_image_scale(0 * 4 + xOffset, 3 * 4 + yOffset, 4, 4, Scale))
            self.tileTextures[i].append(TileSheet.get_image_scale(1 * 4 + xOffset, 3 * 4 + yOffset, 4, 4, Scale))
            self.tileTextures[i].append(TileSheet.get_image_scale(2 * 4 + xOffset, 3 * 4 + yOffset, 4, 4, Scale))
            self.tileTextures[i].append(TileSheet.get_image_scale(3 * 4 + xOffset, 3 * 4 + yOffset, 4, 4, Scale))

    def getRVar(self):
        return random.randint(0,self.variations)

    def getTile(self, index, variation=-1):
        if(variation < 0):
            return self.tileTextures[self.getRVar()][index]
        return self.tileTextures[variation][index]

    def drawTileTexture(self, screen, variation = -1, xOffset = 0, yOffset = 0):
        yOffset *= Scale
        xOffset *= Scale

        # Corners
        screen.blit(self.getTile(0,variation),(0 * 4 * Scale + xOffset, 0 * 4 * Scale + yOffset))
        screen.blit(self.getTile(1,variation),(1 * 4 * Scale + xOffset, 0 * 4 * Scale + yOffset))
        screen.blit(self.getTile(2,variation),(0 * 4 * Scale + xOffset, 1 * 4 * Scale + yOffset))
        screen.blit(self.getTile(3,variation),(1 * 4 * Scale + xOffset, 1 * 4 * Scale + yOffset))

        yOffset += 8 * Scale
        # Middle Square
        screen.blit(self.getTile(4, variation),(1 * 4 * Scale + xOffset, 1 * 4 * Scale + yOffset))
        # Top Row
        screen.blit(self.getTile(5, variation),(0 * 4 * Scale + xOffset, 0 * 4 * Scale + yOffset))
        screen.blit(self.getTile(6, variation),(1 * 4 * Scale + xOffset, 0 * 4 * Scale + yOffset))
        screen.blit(self.getTile(7, variation),(2 * 4 * Scale + xOffset, 0 * 4 * Scale + yOffset))
        screen.blit(self.getTile(8, variation),(3 * 4 * Scale + xOffset, 0 * 4 * Scale + yOffset))
        # Middle Two Rows
        screen.blit(self.getTile(9, variation), (0 * 4 * Scale + xOffset, 1 * 4 * Scale + yOffset))
        screen.blit(self.getTile(10, variation),(0 * 4 * Scale + xOffset, 2 * 4 * Scale + yOffset))
        screen.blit(self.getTile(11, variation),(3 * 4 * Scale + xOffset, 1 * 4 * Scale + yOffset))
        screen.blit(self.getTile(12, variation),(3 * 4 * Scale + xOffset, 2 * 4 * Scale + yOffset))
        # Bottom Row
        screen.blit(self.getTile(13, variation),(0 * 4 * Scale + xOffset, 3 * 4 * Scale + yOffset))
        screen.blit(self.getTile(14, variation),(1 * 4 * Scale + xOffset, 3 * 4 * Scale + yOffset))
        screen.blit(self.getTile(15, variation),(2 * 4 * Scale + xOffset, 3 * 4 * Scale + yOffset))
        screen.blit(self.getTile(16, variation),(3 * 4 * Scale + xOffset, 3 * 4 * Scale + yOffset))

tiles = [
    0,
    Tile(SpriteSheet("debug1.png"), 1), # Orange
    Tile(SpriteSheet("debug2.png"), 1), # Blue
    Tile(SpriteSheet("debug3.png"), 1), # Yellow
    Tile(SpriteSheet("debug4.png"), 1),
]

def draw():
    for i in range(tiles[0].variations):
        tiles[0].drawTileTexture(screen, variation= i,xOffset= i * 16,yOffset= 0)
        tiles[1].drawTileTexture(screen, variation= i,xOffset= i * 16,yOffset= 24)

def matchType(hexVal):
    match hexVal:
        case 0x1a0: # Return Corners
            return 0
        case 0x0a0:
            return 0
        case 0x2C8:
            return 1
        case 0x288:
            return 1
        case 0x426:
            return 2
        case 0x422:
            return 2
        case 0x60B:
            return 3
        case 0x60a:
            return 3

        case 0x601: # Top Row
            return 5
        case 0x402:
            return 6
        case 0x406:
            return 6
        case 0x603:
            return 7
        case 0x602:
            return 7
        case 0x404:
            return 8

        case 0x240: # Bottom Row
            return 13
        case 0x080:
            return 14
        case 0x180:
            return 14
        case 0x2c0:
            return 15
        case 0x280:
            return 15
        case 0x100:
            return 16

        case 0x248: # Right Row
            return 9
        case 0x208:
            return 9
        case 0x609:
            return 10
        case 0x608:
            return 10

        case 0x20:  # Left Row
            return 11
        case 0x120:
            return 11
        case 0x420:
            return 12
        case 0x424:
            return 12
    print("No Match Found", '{:#05x}'.format(hexVal))
    return -1

def drawMap():
    DEBUG = False
    highlightX = len(map[0]) - 2
    highlightY = len(map) - 2
    tileOffset = 4 * Scale

    # Draw Block
    for y in range(1, len(map) - 1):
        yOffset = y * 8 * Scale - 8 * Scale
        for x in range(1, len(map[0]) - 1):
            xOffset = x * 8 * Scale - 8 * Scale
            if(map[y][x] != 0):
                screen.blit(tiles[map[y][x]].getTile(4, tiles[map[y][x]].getRVar()),(xOffset, yOffset))

            if (DEBUG and x == highlightX and y == highlightY):
                screen.blit(tiles[4].getTile(4, 0),(xOffset, yOffset))


            # Create Bitmap
            selection = 0x7EF

            if (map[y - 1][x - 1] <= map[y][x]): selection &= 0x6FF
            if (map[y - 1][x    ] <= map[y][x]): selection &= 0x77F
            if (map[y - 1][x + 1] <= map[y][x]): selection &= 0x7BF

            if (map[y    ][x - 1] <= map[y][x]): selection &= 0x7DF
            if (map[y    ][x + 1] <= map[y][x]): selection &= 0x7F7

            if (map[y + 1][x - 1] <= map[y][x]): selection &= 0x7FB
            if (map[y + 1][x    ] <= map[y][x]): selection &= 0x7FD
            if (map[y + 1][x + 1] <= map[y][x]): selection &= 0x7FE

            if (DEBUG and x == highlightX and y == highlightY):
                print("Selection"   ,       '{:#05x}'.format(selection))
                print("Top Left"    , x, y, '{:#05x}'.format(selection), '{:#05x}'.format(selection & 0x1B0))
                print("Top Right"   , x, y, '{:#05x}'.format(selection), '{:#05x}'.format(selection & 0x2D8))
                print("Bottom Left" , x, y, '{:#05x}'.format(selection), '{:#05x}'.format(selection & 0x436))
                print("Bottom Right", x, y, '{:#05x}'.format(selection), '{:#05x}'.format(selection & 0x61B))

            if(selection & 0x1FF == 0x0): continue # If no edges found continue

            def drawBorder(material, hexValue, xTileOffset, yTileOffset):
                result = matchType(hexValue)
                screen.blit(tiles[material].getTile(result, tiles[material].getRVar()),(xOffset + xTileOffset, yOffset + yTileOffset))

            def drawCorner(material1, mask1, material2, mask2, material3, mask3, input, xTileOffset, yTileOffset):
                # Get all non-air tiles
                mask1 &= input
                mask2 &= input
                mask3 &= input
                # Sort materials
                if (material1 > material3):
                    material1, material3 = material3, material1
                    mask1, mask3 = mask3, mask1
                if (material1 > material2):
                    material1, material2 = material2, material1
                    mask1, mask2 = mask2, mask1
                if (material2 > material3):
                    material2, material3 = material3, material2
                    mask2, mask3 = mask3, mask2
                # Create Proper Borders where materials are the same
                if (material1 == material2):
                    mask1 |= mask2
                    mask2 |= mask1
                if (material1 == material3):
                    mask1 |= mask3
                    mask3 |= mask1
                if (material2 == material3):
                    mask2 |= mask3
                    mask3 |= mask2
                # Draw the borders if that block is present
                if (mask1 & 0x1FF != 0x0): drawBorder(material1, mask1, xTileOffset, yTileOffset)
                if (mask2 & 0x1FF != 0x0): drawBorder(material2, mask2, xTileOffset, yTileOffset)
                if (mask3 & 0x1FF != 0x0): drawBorder(material3, mask3, xTileOffset, yTileOffset)

            # Top Left
            temp = selection & 0x1A0
            if(temp != 0x000):
                drawCorner(
                    map[y    ][x - 1], 0x020,
                    map[y - 1][x    ], 0x080,
                    map[y - 1][x - 1], 0x100,
                    temp,
                    0, 0
                )

            # Top Right
            temp = selection & 0x2C8
            if(temp != 0x200):
                drawCorner(
                    map[y    ][x + 1], 0x208,
                    map[y - 1][x    ], 0x280,
                    map[y - 1][x + 1], 0x240,
                    temp,
                    tileOffset, 0
                )

            # Bottom Left
            temp = selection & 0x426
            if(temp != 0x400):
                drawCorner(
                    map[y    ][x - 1], 0x420,
                    map[y + 1][x    ], 0x402,
                    map[y + 1][x - 1], 0x404,
                    temp,
                    0, tileOffset
                )

            # Bottom Right
            temp = selection & 0x60B
            if(temp != 0x600):
                drawCorner(
                    map[y + 1][x    ], 0x602,
                    map[y    ][x + 1], 0x608,
                    map[y + 1][x + 1], 0x601,
                    temp,
                    tileOffset, tileOffset
                )

run = True

# Background
screen.fill((150, 50, 50))
#screen.fill((150, 200, 200))
# Draw Tiles
drawMap()

while run:
    # Keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Puts everything on the display
    pygame.display.update()

pygame.quit()
