# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
#screen = pygame.display.set_mode((1920, 1080))
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
#w, h = pygame.display.get_surface().get_size()
w = screen.get_width()
h = screen.get_height()

dt = 0


blockSize = 20 

#====================================================================================
class Snake:
    def __init__(self, name, xHeadStartPosition, yHeadStartPosition, xHeadDirection, yHeadDirection, length):
        self.name = name
        self.xHeadNextPosition = xHeadStartPosition
        self.yHeadNextPosition = yHeadStartPosition
        #Could do position/directions in tuples instead
        #self.headPosition = headPosition
        #self.headDirection = headDirection
        self.xHeadDirection = xHeadDirection
        self.yHeadDirection = yHeadDirection
        self.length = length
        self.body = [(xHeadStartPosition, yHeadStartPosition)]
        self.bodyWidth = 20

    def drawSnake(self):

        self.body.insert(0, (self.xHeadNextPosition, self.yHeadNextPosition))
        del self.body[-1]

        for piece in self.body:
            print(piece[0], piece[1])

            #width = self.bodyWidth*(self.xHeadDirection ** 2)+self.bodyWidth/2*(self.yHeadDirection ** 2)
            #height = self.bodyWidth/2*(self.xHeadDirection **2)+self.bodyWidth*(self.yHeadDirection ** 2)

            rect = pygame.Rect(piece[0], piece[1], self.bodyWidth, self.bodyWidth)
            #parameters: (surface to draw on, color, rect, width, border radius (all), border radius tl, border radius tr, border radius bl, border radius br)
            #pygame.draw.rect(screen, (50, 200, 100), rect, 0, 0, (-9*self.xHeadDirection)+(-9*self.yHeadDirection), (9*self.xHeadDirection)+(-9*self.yHeadDirection), (-9*self.xHeadDirection)+(9*self.yHeadDirection), (9*self.xHeadDirection)+(9*self.yHeadDirection))
            pygame.draw.rect(screen, (150, 50, 50), rect, 0)

    #def eatFood(self):

#====================================================================================
class Food:
    def __init__(self, xPosition, yPosition, value):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.value = value

    def drawFood(self):
        pygame.draw.circle(screen, (70, 180, 20), (self.xPosition, self.yPosition), 10)

#-------------------------------------------------------------------------------
def main():
    print("main")
    running = True
    foodList = []
    player = Snake("Simon", screen.get_width()/2, screen.get_height()/2, 0, -1, 2)
    #snakeHeadPosX = screen.get_width()/2
    #snakeHeadPosY = screen.get_height()/2
    #player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        drawGrid(w, h, blockSize)

        #player_pos = pygame.Vector2(w / 2, h / 2)
        #pygame.draw.circle(screen, "blue", player_pos, 10)
        #drawSnake(snakeHeadPosX, snakeHeadPosY)

        player.drawSnake()

        for food in foodList:
            food.drawFood()
            print(food.xPosition, food.yPosition)

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False   

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            #player.positions[0][1] -=(blockSize)
            player.yHeadNextPosition -=(blockSize)
            player.yHeadDirection = -1
            player.xHeadDirection = 0
            #player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            #player.positions[0][1] +=(blockSize)
            player.yHeadNextPosition +=(blockSize)
            player.yHeadDirection = 1
            player.xHeadDirection = 0
            #player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            #player.positions[0][0] -=(blockSize)
            player.xHeadNextPosition -=(blockSize)
            player.xHeadDirection = -1
            player.yHeadDirection = 0
            #player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            #player.positions[0][0] +=(blockSize)
            player.xHeadNextPosition +=(blockSize)
            player.xHeadDirection = 1
            player.yHeadDirection = 0
            #player_pos.x += 300 * dt
        if keys[pygame.K_n]:
            xRan = random.randint(0, w)
            yRan = random.randint(0, h)
            xFoodPos = (int(xRan)-int(xRan)%blockSize)+blockSize/2
            yFoodPos = (int(yRan)-int(yRan)%blockSize)+blockSize/2
            foodItem = Food(xFoodPos, yFoodPos, 10)
            
            foodList.insert(0, foodItem)
            print("Food item added!")
        if keys[pygame.K_ESCAPE]:
            running = False

        # if user hasn't pressed a key, the snake should still keep moving forward
        if not (keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]):
            player.xHeadNextPosition += (blockSize * player.xHeadDirection)
            #player.positions[0][0] += (blockSize * player.xHeadDirection)
            player.yHeadNextPosition += (blockSize * player.yHeadDirection)
            #player.positions[0][1] += (blockSize * player.yHeadDirection)


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(4) / 1000

    pygame.quit()
#=======================================================================================

def drawGrid(width, height, blockSize):
    print("Drawing Grid")
    


    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)

#========================================================================================

main()