#CREATED BY ELLIOT CODLING
import pygame, os, random

file_dir = os.getcwd() # get the current directory    
pygame.font.init()

from engine import game_engine_004 as game_engine

# create window ---------------------------------
w, h = 1280, 720
window = game_engine.update.define("Infinate World", w, h)

#borders to stop moving off screen
left_border = 20
right_border = w - 20
top_border = 20
bottom_border = h - 20
# -----------------------------------------------
#create variable stuff
clock = pygame.time.Clock()
gameplay = True
vel = 5

blinked = False  #check if blinked
frameTimes = 60     #number of frames to be passed
#background
display = []
background_texture = pygame.image.load("{}/textures/background/background.webp".format(file_dir))
background = game_engine.properties_object("background", background_texture, 0, 0, 1280, 720, False)

display += [background]

#display sprites
display_sprite = []
jimmy_texture = pygame.image.load("{}/textures/jimmy/jimmy_normal.png".format(file_dir))
jimmy_texture = pygame.transform.scale(jimmy_texture, [40, 40])

jimmy_blink_texture = pygame.image.load("{}/textures/jimmy/jimmy_blink.png".format(file_dir))
jimmy_blink_texture = pygame.transform.scale(jimmy_blink_texture, [40, 40])

jimmy_left_texture = pygame.image.load("{}/textures/jimmy/jimmy_left.png".format(file_dir))
jimmy_left_texture = pygame.transform.scale(jimmy_left_texture, [40, 40])

jimmy_right_texture = pygame.image.load("{}/textures/jimmy/jimmy_right.png".format(file_dir))
jimmy_right_texture = pygame.transform.scale(jimmy_right_texture, [40, 40])

jimmy = game_engine.properties_object("jimmy", jimmy_texture, 640, 360, 40, 40, False)

display_sprite += [jimmy]
#foreground
foreground = []

#text_foreground
text_foreground = []


# main game function --------------------------------------------------------------
def blink(self, blinked, frameTimes):
    frameTimes -= 1
    if blinked == True and frameTimes == 0:
        self.texture = jimmy_texture
        blinked = False

    elif blinked == False:
        blinkVar = random.randint(0, 500)
        
        if blinkVar == 0:
            self.texture = jimmy_blink_texture
            blinked = True
            frameTimes = 6

    return blinked, frameTimes







def main_game(jimmy, blinked, frameTimes, vel):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        jimmy = game_engine.player.left(jimmy, vel, left_border)
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        jimmy = game_engine.player.right(jimmy, vel, right_border)

    #sometimes blink
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) != True and (keys[pygame.K_RIGHT] or keys[pygame.K_d]) != True:        #prevent blink when walking
        blinked, frameTimes = blink(jimmy, blinked, frameTimes)
    


    #return values to main code
    return blinked, frameTimes
    
# ---------------------------------------------------------------------------------

# main game loop ------------------------------------------------------------------
run = True
while run:
    # keyboard and exit button, main code -----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if not gameplay:
        run = False
    else:
        blinked, frameTimes = main_game(jimmy, blinked, frameTimes, vel)

    #exit
    if keys[pygame.K_ESCAPE]:
        run = False

    #game_engine.update.list_debug(display, display_sprite, foreground, text_foreground, clock)
    # update screen
    
    game_engine.update.window(window, display, display_sprite, foreground, text_foreground, clock, 0)     #update the window
    clock.tick(60)  #limit to 60 fps

pygame.quit()