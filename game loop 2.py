# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
w = screen.get_width()
h = screen.get_height()
blockSize = 50 

#====================================================================================
class Snake:
    def __init__(self, name, initPosition, initDirection, length):
        self.name = name
        self.body = [(initPosition)]
        self.direction = initDirection
        self.length = length
        self.bodyWidth = 50
        self.digesting = 0
        self.collision = False

        for i in range(1, length):
            xAhead, yAhead = self.body[i-1]
            xHere = xAhead - (self.bodyWidth * self.direction[0])
            yHere = yAhead - (self.bodyWidth * self.direction[1])
            self.body.insert(i, (xHere, yHere))


    def draw(self):

        if (not self.collision):
            self.body.insert(0, (self.body[0][0]+(self.direction[0]*blockSize), self.body[0][1]+(self.direction[1]*blockSize)))
        
            if(self.digesting <= 0):
                del self.body[-1]
                self.digesting = 0  
            else:
                print("Snake currently digesting: "+str(self.digesting))
                self.digesting-=1      

            rect = pygame.Rect(self.body[0][0], self.body[0][1], self.bodyWidth, self.bodyWidth)
            pygame.draw.rect(screen, (50, 100, 200), rect, 0, 0, ((-10)*self.direction[0]+(-10)*self.direction[1]), ((10)*self.direction[0]+(-10)*self.direction[1]), ((-10)*self.direction[0]+(10)*self.direction[1]), ((10)*self.direction[0]+(10)*self.direction[1]))
        
        for piece in self.body[1:]:
                #width = self.bodyWidth*(self.xHeadDirection ** 2)+self.bodyWidth/2*(self.yHeadDirection ** 2)
                #height = self.bodyWidth/2*(self.xHeadDirection **2)+self.bodyWidth*(self.yHeadDirection ** 2)
                rect = pygame.Rect(piece[0], piece[1], self.bodyWidth, self.bodyWidth)

                #parameters: (surface to draw on, color, rect, width, border radius (all), border radius tl, border radius tr, border radius bl, border radius br)
                #pygame.draw.rect(screen, (50, 200, 100), rect, 0, 0, (-9*self.xHeadDirection)+(-9*self.yHeadDirection), (9*self.xHeadDirection)+(-9*self.yHeadDirection), (-9*self.xHeadDirection)+(9*self.yHeadDirection), (9*self.xHeadDirection)+(9*self.yHeadDirection))
                
                pygame.draw.rect(screen, (50, 50, 200), rect, 0)

        if(self.collision):
            rect = pygame.Rect(self.body[1][0], self.body[1][1], self.bodyWidth, self.bodyWidth)
            pygame.draw.rect(screen, (200, 50, 50), rect, 0)

        self.eaten = False


#====================================================================================
class Food:
    def __init__(self, position, nutrition):
        self.position = position
        self.nutrition = nutrition

    def draw(self):
        foodSize = ((self.nutrition)*5)
        pygame.draw.circle(screen, (70, 180, 20), (self.position[0]+(blockSize/2), self.position[1]+(blockSize/2)), foodSize)

#-------------------------------------------------------------------------------
def main():
    running = True
    foodList = []
    playerStartPosition = w/2, h/2
    player = Snake("Simon", playerStartPosition, (0,-1), 5)
    score = 0

    while running:

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        drawGrid(w, h, blockSize)

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_w):
                    player.direction = (0, -1) 
                elif (event.key == pygame.K_s):
                    player.direction = (0, 1)
                elif (event.key == pygame.K_a):
                    player.direction = (-1, 0)
                elif (event.key == pygame.K_d):
                    player.direction = (1, 0)
                #If user has pressed a key but not a direction...
                else:
                    print("Other key pressed")
                    break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            foodPos = ()
            nutrition = 0;
            while True:
                nutrition = random.randint(0, int(blockSize/10))
                xRan = random.randint(0, w)
                yRan = random.randint(0, h)
                xPos = (int(xRan)-int(xRan)%blockSize)
                yPos = (int(yRan)-int(yRan)%blockSize)
                foodPos = xPos, yPos

                if(not foodPos in player.body):
                    break

            #print(xFoodPos, yFoodPos)
            #For now, value parameter for is blocksize but this should be change mid game
            foodItem = Food(foodPos, nutrition)
                
            foodList.insert(0, foodItem)
            print("Food item added at: ("+str(foodPos)+") with nutrition: "+str(nutrition))
        
        if keys[pygame.K_ESCAPE]:
            running = False

        for food in foodList:
            if(player.body[0][0] == food.position[0] and player.body[0][1] == food.position[1]):
                print("Snake has eaten food with nutrition: "+str(food.nutrition))
                player.digesting+=food.nutrition
                score+=food.nutrition
                foodList.remove(food)
            else:
                food.draw()

        player.draw()
        if player.body.count(player.body[0]) > 1:
            player.collision = True

        if (player.body[0][0] < 0) or (player.body[0][0] > w) or (player.body[0][1] < 0) or (player.body[0][1] > h):
            player.collision = True


        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(5)

    pygame.quit()
    print("GAME OVER: Score ["+str(score)+"]")

#=======================================================================================

def drawGrid(width, height, blockSize):
    #print("Drawing Grid")

    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)

#========================================================================================

main()