import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 50
height = 50
vel = 10
acceleration = 0.3
friction = 0.1
max_speed = 15
dx = 0
dy = 0
score = 0
clock = pygame.time.Clock()

run = True

while run:
    pygame.time.delay(10)
    clock.tick(60) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Apply acceleration in the x and y directions based on user input
    if keys[pygame.K_LEFT]:
        dx -= acceleration
    if keys[pygame.K_RIGHT]:
        dx += acceleration
    if keys[pygame.K_UP]:
        dy -= acceleration
    if keys[pygame.K_DOWN]:
        dy += acceleration
    
    # Apply friction to slow down the player gradually
    dx = dx * (1 - friction)
    dy = dy * (1 - friction)

    # Limit the speed of the player to prevent it from moving too fast
    speed = (dx ** 2 + dy ** 2) ** 0.5
    if speed > max_speed:
        dx = dx * max_speed / speed
        dy = dy * max_speed / speed

    # Update the position of the player
    x += dx
    y += dy

    # Update the score based on the time that has elapsed
    score += clock.get_time() / 1000

    # Draw the score on the top-left corner of the screen
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: {:.0f}".format(score), True, (255, 255, 255))
    
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height)) 
    win.blit(score_text, (10, 10))  
    pygame.display.update() 
    
pygame.quit()
