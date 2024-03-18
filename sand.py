import pygame 
import random 

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('sand sim')
clock = pygame .time.Clock()
mouseDown = False 
mousepos = (0,0)
color = (200,0,0)

#i dont like pythons way of doing 2d arrays :(
grid = [[0 for i in range(100)] for j in range(100)]

#initialize grid to 0 
for i in range(100):
    for j in range(100):
        grid[i][j] = 0

grid[20][j] = 1 #test case (comment out later)

while True: # main game loop++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    clock.tick(60)
    #input section------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        #grab mouse position 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True

        if event.type == pygame.MOUSEBUTTONUP:
             mouseDown = False

        if event.type == pygame.MOUSEMOTION:
            mousepos = event.pos 

    #update section----------------------------------------------------------------------
    #print(mouseDown)
    if mouseDown == True:

        #check where mouse is, set grid location to 1 
        grid[int(mousepos[0]/10)][int(mousepos[1]/10)]=1
        
    #move sand down
    for k in range(99): #start from the bottom, move up 
            for i in range(99):
                if grid[i][98-k]==1 and grid[i][99-k]==0:
                                      
                    #set the square you're looking at to 0
                    grid[i][98-k]=0
                    #set the square below the one you're looking at to 1
                    grid[i][99-k]=1
                    
                
        # render section+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    screen.fill((100,100,100))
    
    for i in range(100):
            for j in range(100):

                if grid[i][j]==1:
                    pygame.draw.rect(screen, (color), (i*10, j*10, 10, 10)) #1 is red 
                else:
                    pygame.draw.rect(screen, (255,255,255), (i*10, j*10, 10, 10)) #0 is white

                    #pygame.draw.rect(screen, (0,0,0,), (i*10, j*10, 10, 10), 1)#grid for testing 
                    
    pygame.display.flip()

pygame.quit()
