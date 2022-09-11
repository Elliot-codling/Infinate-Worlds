#CREATED BY ELLIOT CODLING
import pygame, os, random

file_dir = os.getcwd() + "/InfinateWorld_data" # get the current directory    
pygame.font.init()

from engine import game_engine_000 as game_engine


# create window ---------------------------------
w, h = 1280, 720
window = game_engine.update.define("Infinate World", w, h)
frames = 0

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
texture_size = 80


#background
display = []

print("DEBUG...")
print(f"{file_dir}/textures/background/background.webp")
print("")
background_texture = pygame.image.load("{}/textures/background/background.webp".format(file_dir))
background = game_engine.properties_object("background", background_texture, 0, 0, 1280, 720, False)

display += [background]

#display sprites
display_sprite = []
jimmy_texture = pygame.image.load("{}/textures/jimmy/jimmy_normal.png".format(file_dir))
jimmy_texture = pygame.transform.scale(jimmy_texture, [texture_size, texture_size])

jimmy_blink_texture = pygame.image.load("{}/textures/jimmy/jimmy_blink.png".format(file_dir))
jimmy_blink_texture = pygame.transform.scale(jimmy_blink_texture, [texture_size, texture_size])

jimmy_left_texture = pygame.image.load("{}/textures/jimmy/jimmy_left.png".format(file_dir))
jimmy_left_texture = pygame.transform.scale(jimmy_left_texture, [texture_size, texture_size])

jimmy_right_texture = pygame.image.load("{}/textures/jimmy/jimmy_right.png".format(file_dir))
jimmy_right_texture = pygame.transform.scale(jimmy_right_texture, [texture_size, texture_size])

jimmy = game_engine.properties_object("jimmy", jimmy_texture, 640, 360, texture_size, texture_size, False)

display_sprite += [jimmy]
#foreground
foreground = []

#text_foreground
score = 10
text_foreground = []
font = pygame.font.SysFont(None, 30)
score_texture = font.render("Score: {}".format(score), True, pygame.Color("RED"))
score_text = game_engine.properties_text("Score", score_texture, 10, 10)
text_foreground += [score_text]

# main game function --------------------------------------------------------------

def blink(jimmy):
    randomTime = random.randint(0, 250)         #randomise chance of blinking
    if randomTime == 0 and jimmy.animationStage == 0:           #make sure that jimmy isnt currently blinking
        jimmy.texture = jimmy_blink_texture             #change texture
        jimmy.animationStage = 1                #change so that blinking state is 1         
        jimmy.animationTime = frames + 8                #time to blink

    elif jimmy.animationStage == 1 and frames >= jimmy.animationTime:           #ensure that animation is currently blinking and that frames >= animationTime
        jimmy.texture = jimmy_texture                   #change texture
        jimmy.animationStage = 0            #change so that blinking is 0
        

def walking(jimmy):
    if jimmy.animationStage == 0 and frames >= jimmy.animationTime:
        jimmy.texture = jimmy_left_texture
        jimmy.animationStage = 1
        jimmy.animationTime = frames + 20

    elif jimmy.animationStage == 1 and frames >= jimmy.animationTime:
        jimmy.texture = jimmy_right_texture
        jimmy.animationStage = 0
        jimmy.animationTime = frames + 20




def main_game(jimmy, vel):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        jimmy = game_engine.player.left(jimmy, vel, left_border)

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        jimmy = game_engine.player.right(jimmy, vel, right_border)

    #ANIMATIONS
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) != True and (keys[pygame.K_RIGHT] or keys[pygame.K_d]) != True:        #prevent blink when walking      
        blink(jimmy)

    else:
        walking(jimmy)


    if frames >= jimmy.animationTime:     #reset to default texture if the time for animation has ran out and current animation is false
        jimmy.texture = jimmy_texture
    #return values to main loop

    
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
        main_game(jimmy, vel)
        frames += 1

    #exit
    if keys[pygame.K_ESCAPE]:
        run = False

    #game_engine.update.list_debug(display, display_sprite, foreground, text_foreground, clock)
    # update screen
    
    game_engine.update.window(window, display, display_sprite, foreground, text_foreground, clock, 0)     #update the window
    clock.tick(60)  #limit to 60 fps

pygame.quit()