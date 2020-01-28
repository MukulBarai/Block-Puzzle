import pygame
import time
import random
import copy

#Declaring Variables
col = 20
row = 40
blockW = 15
width = col * blockW
height = row * blockW
gameOver = False
matrices = []

#Variable for clock
startTime = time.time()
clockTime = 0.5
nTime = 0


#Initializing pygame 
pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.update()

#Declaring Classes
class ShapeO:
    def __init__(self, xCor, yCor):
        self.xCor = xCor
        self.yCor = yCor
    width = 2
    height = 2
    color = (52, 235, 207)
    shape = [
        [1, 1],
        [1, 1]
    ]

class ShapeZ:
    def __init__(self, xCor, yCor):
        self.xCor = xCor
        self.yCor = yCor
    color = (58, 235, 52)
    width = 3
    height = 2
    shape = [
        [1, 1, 0],
        [0, 1, 1]
    ]

class ShapeS:
    def __init__(self, xCor, yCor):
        self.xCor = xCor
        self.yCor = yCor
    width = 3
    height = 2
    color = (58, 235, 52)
    shape = [
        [0, 1, 1],
        [1, 1, 0]
    ]

class ShapeI:
    def __init__(self, xCor, yCor):
        self.xCor = xCor
        self.yCor = yCor
    width = 1
    height = 4
    color = (235, 52, 76)
    shape = [
        [1],
        [1],
        [1],
        [1]
    ]

class ShapeL:
    def __init__(self, xCor, yCor):
        self.xCor = xCor
        self.yCor = yCor
    width = 2
    height = 3
    color = (235, 52, 223)
    shape = [
        [1, 0],
        [1, 0],
        [1, 1]
    ]

class ShapeF:
    def __init__(self, xCor, yCor):
        self.xCor = xCor
        self.yCor = yCor
    width = 2
    height = 3
    color = (235, 52, 223)
    shape = [
        [0, 1],
        [0, 1],
        [1, 1]
    ]

class ShapeT:
    def __init__(self, xCor, yCor):
        self.xCor = xCor
        self.yCor = yCor
    width = 3
    height = 2
    color = (235, 232, 52)
    shape = [
        [1, 1, 1],
        [0, 1, 0]
    ]

shapes = [ShapeZ, ShapeS, ShapeT, ShapeF, ShapeL, ShapeI, ShapeF, ShapeO]

def newShape():
    global shapes
    shape = shapes[random.randrange(len(shapes))]
    return shape(9, 0)

#Global shape variable
shape = newShape()

#Single block
class Block:
    def draw(self, xCor, yCor):
        pygame.draw.rect(window, self.color, 
            (yCor*self.height, xCor*self.width, self.width, self.height)
        )

    width = blockW
    height = blockW
    fill = False
    color = (0, 250, 0)



#Method for rotation
def getRotation(shape):
    col = []
    nShape = copy.deepcopy(shape)
    for i in range(nShape.width):
        row = []
        for j in range(nShape.height):
            row.append(nShape.shape[nShape.height-j-1][i])
        col.append(row)
    nShape.shape = col
    nShape.width = shape.height
    nShape.height = shape.width
    nShape.xCor += round((nShape.height - nShape.width) / 2)
    nShape.yCor -= round((nShape.height - nShape.width) / 2)
    return nShape

def checkCollision(shape):
    if shape.xCor <= -1:
        return False
    if shape.xCor + shape.width >= col:
        return False
    if shape.yCor + shape.height >= row:
        return False
    for i in range(shape.height):
        for j in range(shape.width):
            if shape.shape[i][j] and matrices[shape.yCor+i][shape.xCor+j].fill:
                return False
    return True

def rotate():
    global shape
    nShape = getRotation(shape)
    if checkCollision(nShape):
        shape = nShape
    return


#Method for moving left and right
def checkLeft(shape):
    global col
    if shape.xCor - 1 <= -1:
        return False
    for i in range(shape.height):
        for j in range(shape.width):
            if shape.shape[i][j] and matrices[shape.yCor+i][shape.xCor+j-1].fill:
                return False
    return True


def checkRight(shape):
    global col
    if shape.xCor + shape.width >= col:
        return False
    for i in range(shape.height):
        for j in range(shape.width):
            if shape.shape[i][j] and matrices[shape.yCor+i][shape.xCor+j+1].fill:
                return False
    return True

def moveLeft(shape):
    if checkLeft(shape):
        shape.xCor -= 1
    return

def moveRight(shape):
    if checkRight(shape):
        shape.xCor += 1
    return

def checkBottom(shape):
    global row
    if shape.yCor + shape.height >= row:
        return False
    for i in range(shape.height):
        for j in range(shape.width):
            if shape.shape[i][j] and matrices[shape.yCor+i+1][shape.xCor+j].fill:
                return False
    return True

def goDown(shape):
    shape.yCor += 1
    return

def fillMatrices():
    global shape
    for i in range(shape.height):
        for j in range(shape.width):
            if shape.shape[i][j]:
                matrices[shape.yCor+i][shape.xCor+j].color = shape.color 
                matrices[shape.yCor+i][shape.xCor+j].fill = True
    shape = newShape()

def clearRow(row):
    global matrices
    for i in range(row, 0, -1):
        for j in range(col):
            matrices[i][j] = matrices[i-1][j]
    return

def checkPoint():
    for i in range(row):
        for j in range(col):
            if matrices[i][j].fill is False:
                break
            if j + 1 == col:
                clearRow(i)
    return

#Fillig matrices with initial block
def initialize():
    for i in range(row):
        nRow = []
        for j in range(col):
            nRow.append(Block())
        matrices.append(nRow)

def drawShape(shape):
    for i in range(shape.height):
        for j in range(shape.width):
            if shape.shape[i][j]:
                pygame.draw.rect(window, shape.color, 
                    (shape.xCor*blockW + j*blockW, 
                    shape.yCor*blockW + i*blockW, blockW, blockW)
                )

def draw():
    #Drawing Background
    pygame.draw.rect(window, (0, 0, 0), (0, 0, width, height))
    global row, col
    for i in range(row):
        for j in range(col):
            block = matrices[i][j]
            if block.fill:
                block.draw(i, j)
    drawShape(shape)
    for i in range(row):
        pygame.draw.line(window, (17, 17, 18), (0, i*blockW), (col*blockW, i*blockW))
    for i in range(col):
        pygame.draw.line(window, (17, 17, 18), (i*blockW, 0), (i*blockW, row*blockW))
    pygame.display.update()

def update():
    global shape, clockTime
    if checkBottom(shape):
        goDown(shape)
    else:
        fillMatrices()
        checkPoint()
        clockTime = 0.5
    return


def run():
    global gameOver, nTime, startTime, clockTime
    while gameOver is False:
        startTime = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moveLeft(shape)
                elif event.key == pygame.K_DOWN:
                    clockTime = 0.025
                elif event.key == pygame.K_RIGHT:
                    moveRight(shape)
                elif event.key == pygame.K_UP:
                    rotate()
            #endif

        draw()
        timeNow = time.time()
        nTime += timeNow - startTime
        if nTime > clockTime:
            update()
            nTime = 0
    pygame.quit()
    quit()


#Running the game
initialize()
run()