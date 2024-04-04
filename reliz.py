from pygame.sprite import Group
from pygame import * 
clock= time.Clock()

from random import randint 
from pygame.locals import *
#звук 


mixer.init() 
class GameSprite(sprite.Sprite): 
    JUMP_VEL = 8.5

    def __init__(self, player_image , player_x , player_y, size_x, syze_y, player_speed): 
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(player_image),(size_x , syze_y))  
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL

    def reset (self): 
        window.blit(self.image,(self.rect.x , self.rect.y)) 

class Player(GameSprite): 
    def update(self): 
        keys_pressed = key.get_pressed() 
        if keys_pressed [K_LEFT] and self.rect.x > 5 : 
            self.rect.x -= self.speed   
 
            keys_pressed = key.get_pressed() 
        if keys_pressed [K_RIGHT] and self.rect.x < win_width - 80 : 
            self.rect.x += self.speed 
    
 

class Enemy(GameSprite): 
    def update(self): 
        self.rect.x -= 2

        if self.rect.x == 0: 
            self.rect.x = win_width 

background = 'background.jpg'
dino_img = 'dino.png    '
Cactus_img = 'Cactus(1).png'
score = 0
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Dino game") 
background = transform.scale(image.load("background.jpg"), (win_width, win_height)) 
run = True
finish = False
jumping = False
jump_height = 8
jump_count = 8
menu = True
dino = Player(dino_img,60, 335, 70, 70, 20)
cactuses = Enemy(Cactus_img,150,350,50,50,20 )
#шрифти
font.init()
font2 = font.Font(None, 45)
font1 = font.Font(None, 45)

txt_lose_game =  font1.render('Press any button please', True, [255, 0, 0])
txt_win_game =  font1.render('YOU WIN', True, [0, 255, 0])


cactuses = sprite.Group() 
for i in range(1, 6): 
    cactus = Enemy(Cactus_img, 200,353,50,50,20 )
    cactuses.add(cactus) 
    cactus = Enemy(Cactus_img, 410,353,50,50,20 )
    cactuses.add(cactus) 
    cactus = Enemy(Cactus_img, 620,353,50,50,20 )
    cactuses.add(cactus) 
dino_jump_height = 200
dino_jump_speed = 10

clock = time.Clock()

jumping = False
jump_count = 0
hang_time = 130  
hang_start_time = None
while run:
    # подія натискання на кнопку закрити
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == QUIT:
                run = False

    if menu:
        window.blit(background,(0,0))
        dino.reset()
        dino.update()
        window.blit(txt_lose_game, [200, 200])

    if not finish:
        score += 1
        window.blit(background, (0, 0))
        dino.reset()
        dino.update()
        cactuses.draw(window)
        cactuses.update()
        keys = key.get_pressed()
        text = font2.render("Рахунок:" + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        keys = key.get_pressed()
        
        if keys[K_SPACE] and not jumping:
            jumping = True
            hang_start_time = time.get_ticks()

        if jumping:
            if jump_count < dino_jump_height:
                dino.rect.y -= dino_jump_speed
                jump_count += dino_jump_speed
            else:
                if time.get_ticks() - hang_start_time >= hang_time:
                    jumping = False
                    jump_count = 0
        else:
            if dino.rect.y < 335:
                dino.rect.y += dino_jump_speed


    
   


        if sprite.spritecollide(dino, cactuses, False):
            
            # finish  = True
            window.blit(txt_lose_game, [200, 200])
    display.update()
    clock.tick(70)