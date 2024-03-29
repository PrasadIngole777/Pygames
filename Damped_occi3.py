import pygame
from pygame.draw import circle

pygame.init()
window_1 = pygame.display.set_mode((500, 500))
clock_bhai = pygame.time.Clock()
dt = 1
speed = pygame.Vector2(0, 0)  # Set initial speed to zero
player_pos = pygame.Vector2(window_1.get_width() / 2, window_1.get_height() / 2)
running = True
gravity = pygame.Vector2(0, 0.5)  # Gravity force
damping_factor = 0.99  # Damping factor to simulate damping effect

while running:
    window_1.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update speed by adding gravity and apply damping
    speed += gravity
    speed *= damping_factor

    # Update player position using the updated speed
    player_pos += speed * dt

    # Check for collision with window boundaries and reverse the speed if needed
    if player_pos.y < 40:
        player_pos.y = 40  # Set position to avoid getting stuck in boundary
        speed.y *= -1 * damping_factor  # Reverse speed and apply damping
    elif player_pos.y > window_1.get_height() - 40:
        player_pos.y = window_1.get_height() - 40  # Set position to avoid getting stuck in boundary
        speed.y *= -1 * damping_factor  # Reverse speed and apply damping

    # Draw the circle
    gola = pygame.draw.circle(window_1, "Green", (int(player_pos.x), int(player_pos.y)), 40)

    pygame.display.flip()
    dt = clock_bhai.tick(60) / 60

pygame.quit()