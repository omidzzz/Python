from random import randint

WIDTH = 800
HEIGHT = 480    

score = 0
game_over = False

demon = Actor("demon")
demon.pos = 100, 100

fox = Actor("fox")
fox.pos = 100, 100

baby = Actor("baby")
baby.pos = 200, 200

def draw():
    screen.fill("black")
    demon.draw()
    baby.draw()
    screen.draw.text("Score: " + str(score), topleft=(10, 10), fontname="creepy", color= "red")

    if game_over:
        screen.fill("black")
        screen.draw.text("Final Score: " + str(score), topleft=(200, 210), fontname="creepy", fontsize = 60, color = "red")

def place_baby():
    baby.x = randint(20, (WIDTH - 20))
    baby.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():

    global score

    if keyboard.left:
        demon.x = demon.x - 8
    elif keyboard.right:
        demon.x = demon.x + 8
    elif keyboard.up:
        demon.y = demon.y - 8
    elif keyboard.down:
        demon.y = demon.y + 8

    baby_collected = demon.colliderect(baby)

    if baby_collected:
        score+=10
        place_baby()


clock.schedule(time_up, 20.0)
place_baby()