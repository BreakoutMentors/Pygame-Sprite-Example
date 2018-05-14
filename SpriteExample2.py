import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
white = [255, 255, 255]



#FROM Joust example: https://github.com/StevePaget/PythonJoust ###############
def load_sliced_sprites(w, h, filename):
     #returns a list of image frames sliced from file
     images = []
     master_image = pygame.image.load( filename )
     master_image = master_image.convert_alpha()
     master_width, master_height = master_image.get_size()
     for i in range(int(master_width/w)):
          images.append(master_image.subsurface((i*w, 0, w, h)))
     return images

class JoustBird(pygame.sprite.Sprite):
     def __init__(self):
          pygame.sprite.Sprite.__init__(self) #call Sprite initializer

          #load in the images (will do it for every instance, which isn't efficient if you have many)
          self.images = load_sliced_sprites(60, 60, "playerMounted.png")
          self.frameNum = 0
          self.image = self.images[self.frameNum]
          self.x = 415
          self.y = 350
          self.rect = self.image.get_rect() #sets the image size
          self.rect.topleft = (self.x,self.y) #sets the image location
          self.nextFrameCounter = 0 #only going to redraw sometimes
          self.facingRight = True

     def faceLeft(self):
          self.facingRight = False
          #set to the right image
          self.image = self.images[self.frameNum]
          #flip the image
          self.image = pygame.transform.flip(self.image, True, False)

     def faceRight(self):
          self.facingRight = True
          #set to the right image
          self.image = self.images[self.frameNum]

     def update(self):
          #count how many times has been called
          self.nextFrameCounter += 1

          #if this is the third time we will change the bird's image
          if self.nextFrameCounter == 3:
              self.nextFrameCounter = 0
              self.frameNum += 1
              if self.frameNum == 4: #just use the walking images, not the flying ones
                  self.frameNum = 0
              self.image = self.images[self.frameNum]
              
              #flip the image if necessary
              if not self.facingRight:
                  self.image = pygame.transform.flip(self.image, True, False)

         
##############################################################################

bird = JoustBird()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #check if you pressed a key
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:
               bird.faceLeft()
           if event.key == pygame.K_RIGHT:
               bird.faceRight()

    pygame.time.delay(20)  #pause for 20 milliseconds  

    screen.fill(white)  #make the screen completely white

    bird.update()
    screen.blit(bird.image, bird.rect)

    #update the entire display
    pygame.display.update()

pygame.quit()
