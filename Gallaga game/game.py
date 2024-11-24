import pgzrun

WIDTH= 500
HEIGHT= 700

ship = Actor("ship")
ship.x= WIDTH//2
ship.y= HEIGHT-100
ship.dead=False
enemies=[]
bullets=[]
direction=1
score=0
def drawscore():
    screen.draw.text(str(score),(400,25))

for x in range (8):
    for y in range(4):
        enemies.append(Actor("enemy"))
        enemies[-1].x=100+40*x
        enemies[-1].y=0+20*y
def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullets"))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-30

def update():
    global direction
    global score
    if ship.dead==False:
        if keyboard.left:
            ship.x-=2
        if keyboard.right:
            ship.x+=2
    
    for bullet in bullets:
        if bullet.y<-20:
            bullets.remove(bullet)
        else:
            bullet.y-=10
    movedown=False
    if len(enemies)>0 and (enemies[-1].x>WIDTH-20 or enemies[0].x<20):
        movedown=True
        direction=direction*-1

    for enemy in enemies:
        enemy.x+=2*direction
        if movedown==True:
            enemy.y+=30

        for bullet in bullets:
            if enemy.colliderect(bullet):
                score=score+5
                bullets.remove(bullet)
                enemies.remove(enemy)

        if enemy.colliderect(ship):
            ship.dead=True



def draw():
    screen.fill("blue")
    if ship.dead==False:
        ship.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    drawscore()
    screen.draw.text("This is the Gallage game",(200,25))

pgzrun.go()