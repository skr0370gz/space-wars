import pygame
import sys
import traceback
import playerPlane
import enemyPlane
import weapon 
import supply
from pygame.locals import *
from random import*

pygame.init()
pygame.mixer.init()

# setting up the background and the title
screen_size = width,height = 480, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Space Wars")

background = pygame.image.load("images/background.png").convert()

# color
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

# loading music into the game
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(.2)
bulletSound = pygame.mixer.Sound("sound/bullet.wav")
bulletSound.set_volume(.2)
bombSound = pygame.mixer.Sound("sound/use_bomb.wav")
bombSound.set_volume(.2)
supplySound = pygame.mixer.Sound("sound/supply.wav")
supplySound.set_volume(.2)
getBombSound = pygame.mixer.Sound("sound/get_bomb.wav")
getBombSound.set_volume(.2)
getBulletSound = pygame.mixer.Sound("sound/get_bullet.wav")
getBulletSound.set_volume(.2)
upgradeSound = pygame.mixer.Sound("sound/upgrade.wav")
upgradeSound.set_volume(.2)
enemy3FlySound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3FlySound.set_volume(.2)
enemy1DownSound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1DownSound.set_volume(.1)
enemy2DownSound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2DownSound.set_volume(.2)
enemy3DownSound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3DownSound.set_volume(.5)
playerDownSound = pygame.mixer.Sound("sound/me_down.wav")
playerDownSound.set_volume(.2)


def addSmallClass(g1, g2, n):
    for i in range(n):
        smallClassEnemy = enemyPlane.LowClassEnemy(screen_size)
        g1.add(smallClassEnemy)
        g2.add(smallClassEnemy)


def addMiddleClass(g1, g2, n):
    for i in range(n):
        midClassEnemy = enemyPlane.MiddleClassEnemy(screen_size)
        g1.add(midClassEnemy)
        g2.add(midClassEnemy)


def addHighClass(g1, g2, n):
    for i in range(n):
        highClassEnemy = enemyPlane.HighClassEnemy(screen_size)
        g1.add(highClassEnemy)
        g2.add(highClassEnemy)

def increaseSpeed(objective, amount):
    for each in objective:
        each.speed += amount

def main():
    pygame.mixer.music.play(-1)

    # create player plane object
    player = playerPlane.MyPlane(screen_size)

    enemies = pygame.sprite.Group()

    # generating small class enemy plane
    smallClassEnemies = pygame.sprite.Group()
    addSmallClass(smallClassEnemies, enemies, 15)

    # generating middle class enemy plane
    middleClassEnemies = pygame.sprite.Group()
    addMiddleClass(middleClassEnemies, enemies, 4)

    # generating high class enemy plane
    highClassEnemies = pygame.sprite.Group()
    addHighClass(highClassEnemies, enemies, 2)

    # generate advance bullet
    advanceBullets = []
    advanceBulletIndex = 0
    advanceBulletNum = 4
    for count in range(advanceBulletNum):
        advanceBullets.append(weapon.AdvancedBullet(player.rect.midtop))
    # generate basic bullet
    basicBullets = []
    basicBulletIndex = 0
    basicBulletNum = 4
    for count in range(basicBulletNum):
        basicBullets.append(weapon.BasicBullet(player.rect.midtop))
    clock = pygame.time.Clock()

    # hit image
    smallEnemyDestroyIndex = 0
    midEnemyDestroyIndex = 0
    highEnemyDestroyIndex = 0
    playerDestroyIndex = 0

    run = True
    #score
    score = 0;
    scoreFont = pygame.font.Font("font/font.ttf", 36)

    #pausing feature
    pause = False
    pauseNorImage = pygame.image.load("images/pause_nor.png").convert_alpha()
    pausePressImage = pygame.image.load("images/pause_pressed.png").convert_alpha()
    resumeNorImage = pygame.image.load("images/resume_nor.png").convert_alpha()
    resumePressImage = pygame.image.load("images/resume_pressed.png").convert_alpha()
    pauseRect = pauseNorImage.get_rect()
    pauseRect.left, pauseRect.top = width-pauseRect.width - 10, 10
    pauseImage = pauseNorImage

    #level of difficulty
    level = 1

    #bomb weapon
    bombImage = pygame.image.load("images/bomb.png").convert_alpha()
    bombRect = bombImage.get_rect()
    bombFont = pygame.font.Font("font/font.ttf", 48)
    bombNum = 3

    #send a supply every 30s
    bulletSupply = supply.BulletSupply(screen_size)
    bombSupply = supply.BombSupply(screen_size)
    timeSupply = USEREVENT
    pygame.time.set_timer(timeSupply, 30*1000)

    #advancebullet timer
    advanceBulletTime = USEREVENT+1

    #able to use advancebullet 
    useAdvanceBullet = False

    #life
    lifeImage = pygame.image.load("images/life.png").convert_alpha()
    lifeRect = lifeImage.get_rect()
    lifeNum = 3

    #cancel the invincible mode
    invincibleTime = USEREVENT +2

    #restrict repeated opening of file
    recorded =False

    #game over screen
    gameoverFont = pygame.font.Font("font/font.ttf", 48)
    againImage = pygame.image.load("images/again.png").convert_alpha()
    againRect = againImage.get_rect()
    gameoverImage = pygame.image.load("images/gameover.png").convert_alpha()
    gameoverRect = gameoverImage.get_rect()

    # switch between two player plane image to show exhausion
    switchImage = True

    # delay the movement of exhausion
    delay = 100
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and pauseRect.collidepoint(event.pos):
                    pause = not pause 
                    if pause:
                        pygame.time.set_timer(timeSupply,0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(timeSupply,30*1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
            elif event.type == MOUSEMOTION:
                if pauseRect.collidepoint(event.pos):
                    if pause:
                        pauseImage = resumePressImage
                    else:
                        pauseImage = pausePressImage
                else: 
                    if pause:
                        pauseImage = resumeNorImage
                    else:
                        pauseImage = pauseNorImage
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bombNum:
                        bombNum -=1
                        bombSound.play()
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False
            elif event.type == timeSupply:
                supplySound.play()
                if choice([True,False]):
                    bombSupply.reset()
                else: 
                    bulletSupply.reset()
            elif event.type == advanceBulletTime:
                useAdvanceBullet = False
                pygame.time.set_timer(advanceBulletTime,0)
            elif event.type == invincibleTime:
                player.invincible = False
                pygame.time.set_timer(invincibleTime,0)
        # level increases based on the score
        if level == 1 and score > 50000:
            level = 2
            upgradeSound.play()
            #increase 3 low level plane, 2 mid level, 1 high level
            addSmallClass(smallClassEnemies,enemies,3)
            addMiddleClass(middleClassEnemies,enemies,2)
            addHighClass(highClassEnemies,enemies,1)
            increaseSpeed(smallClassEnemies, 1)
        elif level == 2 and score > 300000:
            level = 3
            upgradeSound.play()
            #increase 5 low level plane, 3 mid level, 2 high level
            addSmallClass(smallClassEnemies,enemies,5)
            addMiddleClass(middleClassEnemies,enemies,3)
            addHighClass(highClassEnemies,enemies,2)
            increaseSpeed(smallClassEnemies, 1)
            increaseSpeed(middleClassEnemies,1)
        elif level == 3 and score > 600000:
            level = 4
            upgradeSound.play()
            #increase 5 low level plane, 3 mid level, 2 high level
            addSmallClass(smallClassEnemies,enemies,5)
            addMiddleClass(middleClassEnemies,enemies,3)
            addHighClass(highClassEnemies,enemies,2)
            increaseSpeed(smallClassEnemies, 1)
            increaseSpeed(middleClassEnemies,1)
        elif level == 4 and score > 1000000:
            level = 5
            upgradeSound.play()
            #increase 5 low level plane, 3 mid level, 2 high level
            addSmallClass(smallClassEnemies,enemies,5)
            addMiddleClass(middleClassEnemies,enemies,3)
            addHighClass(highClassEnemies,enemies,2)
            increaseSpeed(smallClassEnemies, 1)
            increaseSpeed(middleClassEnemies,1)


        screen.blit(background, (0, 0))

        if  lifeNum and not pause:             
            # check for user keyboard pressed or not
            keyPressed = pygame.key.get_pressed()

            if keyPressed[K_w] or keyPressed[K_UP]:
                player.up()

            if keyPressed[K_s] or keyPressed[K_DOWN]:
                player.down()

            if keyPressed[K_a] or keyPressed[K_LEFT]:
                player.left()

            if keyPressed[K_d] or keyPressed[K_RIGHT]:
                player.right()

            #draw bomb supply and check for contact
            if bombSupply.active:
                bombSupply.move()
                screen.blit(bombSupply.image, bombSupply.rect)
                if pygame.sprite.collide_mask(bombSupply, player):
                    getBombSound.play()
                    if bombNum < 3:
                        bombNum +=1
                    bombSupply.active = False
            
            #draw bomb supply and check for contact
            if bulletSupply.active:
                bulletSupply.move()
                screen.blit(bulletSupply.image, bulletSupply.rect)
                if pygame.sprite.collide_mask(bulletSupply, player):
                    getBulletSound.play()
                    useAdvanceBullet = True
                    pygame.time.set_timer(advanceBulletTime, 18*1000)
                    bulletSupply.active = False

            #shooting/drawing bullet
            if not(delay% 10):
                bulletSound.play()
                if useAdvanceBullet:
                        bullet = advanceBullets
                        bullet[advanceBulletIndex].resetBullet(player.rect.midtop)
                        advanceBulletIndex = (advanceBulletIndex+1) % advanceBulletNum
                else:
                    bullet = basicBullets
                    bullet[basicBulletIndex].resetBullet(player.rect.midtop)
                    basicBulletIndex = (basicBulletIndex+1) % basicBulletNum

            # check if bullet hit enemy plane
            for b in bullet:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enenmyHit = pygame.sprite.spritecollide(b,enemies,False,pygame.sprite.collide_mask)
                    if enenmyHit:
                        b.active = False
                        for e in enenmyHit:
                            if e in middleClassEnemies or e in highClassEnemies:
                                e.hit = True
                                e.health -= 1
                                if e.health == 0:
                                    e.active = False
                            else:
                                e.active = False

            # draw large class enemy plane
            for plane in highClassEnemies:
                if plane.active:
                    plane.move()
                    if plane.hit:
                        screen.blit(plane.imageHit, plane.rect)
                        plane.hit = False
                    else: 
                        if switchImage:
                            screen.blit(plane.image1, plane.rect)
                        else:
                            screen.blit(plane.image2, plane.rect)

                    # drawing health bar 
                    pygame.draw.line(screen, BLACK, \
                        (plane.rect.left,plane.rect.top-5),\
                        (plane.rect.right,plane.rect.top-5),2 )
                    # if health is above 20 percent show green else show red
                    healthProportion = plane.health / enemyPlane.HighClassEnemy.health
                    if healthProportion > 0.2:
                        healthColor = GREEN
                    else:
                        healthColor = RED
                    pygame.draw.line(screen, healthColor, \
                        (plane.rect.left,plane.rect.top-5),\
                        (int(plane.rect.left +plane.rect.width*healthProportion),\
                            plane.rect.top-5),2)

                    # when appearing play music
                    if plane.rect.bottom == -50:
                        enemy3FlySound.play(-1)
                else:
                    if not(delay%3):
                        if highEnemyDestroyIndex == 0:
                            #destroy
                            enemy3DownSound.play()
                        screen.blit(plane.destroyImages[highEnemyDestroyIndex], plane.rect)
                        highEnemyDestroyIndex = (highEnemyDestroyIndex+1)%6
                        if highEnemyDestroyIndex == 0:
                            enemy3FlySound.stop()
                            score+= 10000
                            plane.resetPlane()

            # draw mid class enemy plane
            for plane in middleClassEnemies:
                if plane.active:
                    plane.move()

                    if plane.hit:
                        screen.blit(plane.imageHit, plane.rect)
                        plane.hit = False
                    else:
                        screen.blit(plane.image, plane.rect)
                    # drawing health bar 
                    pygame.draw.line(screen, BLACK, \
                        (plane.rect.left,plane.rect.top-5),\
                        (plane.rect.right,plane.rect.top-5),2 )
                    # if health is above 20 percent show green else show red
                    healthProportion = plane.health / enemyPlane.MiddleClassEnemy.health
                    if healthProportion > 0.2:
                        healthColor = GREEN
                    else:
                        healthColor = RED
                    pygame.draw.line(screen, healthColor, \
                        (plane.rect.left,plane.rect.top-5),\
                        (int(plane.rect.left +plane.rect.width*healthProportion),\
                            plane.rect.top-5),2)
                else:
                    if not(delay%3):
                        if midEnemyDestroyIndex == 0:
                            enemy2DownSound.play()
                        screen.blit(plane.destroyImages[midEnemyDestroyIndex], plane.rect)
                        midEnemyDestroyIndex = (midEnemyDestroyIndex+1)%4
                        if midEnemyDestroyIndex == 0:
                            score += 5000
                            plane.resetPlane()

            # draw small class enemy plane
            for plane in smallClassEnemies:
                if plane.active:
                    plane.move()
                    screen.blit(plane.image, plane.rect)
                else:
                    if not(delay%3):
                        if smallEnemyDestroyIndex ==0:
                            enemy1DownSound.play()
                        screen.blit(plane.destroyImages[smallEnemyDestroyIndex], plane.rect)
                        smallEnemyDestroyIndex = (smallEnemyDestroyIndex+1)%4
                        if smallEnemyDestroyIndex == 0:
                            score += 1000
                            plane.resetPlane()

            # checking for any damage done to player 
            hit = pygame.sprite.spritecollide(player,enemies,False,pygame.sprite.collide_mask)
            if hit and not player.invincible:
                player.active = False
                for enemy in hit:
                    enemy.active = False
            # draw player plane
            if player.active:
                if switchImage:
                    screen.blit(player.image1, player.rect)
                else:
                    screen.blit(player.image2, player.rect)
            else:
                if not(delay%3):
                    if playerDestroyIndex ==0:
                        playerDownSound.play()
                    screen.blit(plane.destroyImages[playerDestroyIndex], player.rect)
                    playerDestroyIndex = (playerDestroyIndex+1)%4
                    if playerDestroyIndex == 0:
                        lifeNum -= 1
                        player.reset()
                        pygame.time.set_timer(invincibleTime, 3*1000)
            # drawing the bomb
            bombText = bombFont.render("x %d" % bombNum, True, WHITE)
            textRect = bombText.get_rect()
            screen.blit(bombImage, (10, height-10-bombRect.height))
            screen.blit(bombText, (20+bombRect.width, height - 5- textRect.height))

            #drawing remaining life
            if lifeNum:
                for i in range(lifeNum):
                    screen.blit(lifeImage,\
                         (width-10-(i+1)*lifeRect.width, \
                             height-10-lifeRect.height))
            
            #showing the score
            scoreText = scoreFont.render("Score : %s" % str(score), True, WHITE)
            screen.blit(scoreText, (10,5))
            #pause sign graphics
            screen.blit(pauseImage,pauseRect)
            
        elif lifeNum == 0:
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            pygame.time.set_timer(timeSupply,0)

            if  not recorded: 
                recorded = True
                #get high score
                with open("record.txt","r") as file:
                    record = int(file.read())
                if score > record: 
                    with open("record.txt","w") as file:
                        file.write(str(score))
                        record = score
            
            # game end interface
            recordText = scoreFont.render("Best : %d" % record, True, (255, 255, 255))
            screen.blit(recordText, (50, 50))
            gameover_text1 = gameoverFont.render("Your Score", True, (255, 255, 255))
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = (width - gameover_text1_rect.width) // 2, height // 3
            screen.blit(gameover_text1, gameover_text1_rect)
            gameover_text2 = gameoverFont.render(str(score), True, (255, 255, 255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = (width - gameover_text2_rect.width) // 2, gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)
            againRect.left, againRect.top = (width - againRect.width) // 2, gameover_text2_rect.bottom + 50
            screen.blit(againImage, againRect)
            gameoverRect.left, gameoverRect.top = (width - againRect.width) // 2, againRect.bottom + 10
            screen.blit(gameoverImage, gameoverRect)
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if againRect.left < pos[0] < againRect.right and againRect.top < pos[1] < againRect.bottom:
                    main()        
                elif gameoverRect.left < pos[0] < gameoverRect.right and gameoverRect.top < pos[1] < gameoverRect.bottom:
                    pygame.quit()
                    sys.exit()

        # switch the images to show exhasion
        if not(delay % 5):
            switchImage = not switchImage

        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except SystemError:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
