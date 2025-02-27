import pygame
import sys
import math
import time

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Enhanced Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)  # Normal player color
DARK_BLUE = (0, 0, 150)  # Dark effect during dash
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Player setup
player_size = 50
player_speed = 5
dash_speed = 10
dash_duration = 0.5
dash_cooldown = 1
player_rect = pygame.Rect(100, 100, player_size, player_size)

# Dash variables
is_dashing = False
dash_start_time = 0
last_dash_time = -dash_cooldown

# Walls (edges of the screen)
walls = [
    pygame.Rect(0, 0, SCREEN_WIDTH, 30),  # Top
    pygame.Rect(0, SCREEN_HEIGHT - 30, SCREEN_WIDTH, 30),  # Bottom
    pygame.Rect(0, 0, 30, SCREEN_HEIGHT),  # Left
    pygame.Rect(SCREEN_WIDTH - 30, 0, 30, SCREEN_HEIGHT)  # Right
]

def circle_rect_collision(circle_center, circle_radius, rect):
    closest_x = max(rect.left, min(circle_center[0], rect.right))
    closest_y = max(rect.top, min(circle_center[1], rect.bottom))
    dx = circle_center[0] - closest_x
    dy = circle_center[1] - closest_y
    return (dx * dx + dy * dy) < (circle_radius * circle_radius)

class Enemy:
    def __init__(self, path, speed, radius=25, color=RED):
        self.path = path
        self.speed = speed
        self.radius = radius
        self.color = color
        self.x, self.y = path[0]
        self.target_index = 1

    def update(self):
        target = self.path[self.target_index]
        dx, dy = target[0] - self.x, target[1] - self.y
        dist = math.hypot(dx, dy)
        dx_norm, dy_norm = (dx / dist, dy / dist) if dist else (0, 0)

        self.x += dx_norm * self.speed
        self.y += dy_norm * self.speed

        if abs(self.x - target[0]) < self.speed and abs(self.y - target[1]) < self.speed:
            self.x, self.y = target
            self.target_index = (self.target_index + 1) % len(self.path)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

class HomingEnemy:
    def __init__(self, x, y, speed=3.5, radius=30, color=PURPLE):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.color = color

    def update(self, player_x, player_y):
        dx, dy = player_x - self.x, player_y - self.y
        dist = math.hypot(dx, dy)
        dx, dy = (dx / dist, dy / dist) if dist else (0, 0)

        self.x += dx * self.speed
        self.y += dy * self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# Enemy paths
enemy1 = Enemy([(500, 500), (1500, 500), (1500, 900), (500, 900)], speed=4)
enemy2 = Enemy([(1200, 300), (1600, 300), (1600, 700), (1200, 700)], speed=3)
homing_enemy = HomingEnemy(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2, speed=3.5)

clock = pygame.time.Clock()

def game_loop():
    global player_rect, is_dashing, dash_start_time, last_dash_time

    player_rect = pygame.Rect(100, 100, player_size, player_size)  # Reset player position

    while True:
        current_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Dash logic
        if keys[pygame.K_SPACE] and not is_dashing and (current_time - last_dash_time > dash_cooldown):
            is_dashing = True
            dash_start_time = current_time
            last_dash_time = current_time

        # Stop dash after duration
        if is_dashing and current_time - dash_start_time > dash_duration:
            is_dashing = False

        # Determine player color
        player_color = DARK_BLUE if is_dashing else BLUE

        # Movement
        player_speed_current = dash_speed if is_dashing else player_speed
        move_x = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])
        move_y = (keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_w])

        # Normalize diagonal movement
        if move_x != 0 or move_y != 0:
            length = math.sqrt(move_x ** 2 + move_y ** 2)
            move_x /= length
            move_y /= length

        player_rect.x += move_x * player_speed_current
        player_rect.y += move_y * player_speed_current

        # Update enemies
        enemy1.update()
        enemy2.update()
        homing_enemy.update(player_rect.centerx, player_rect.centery)

        # Check collision
        if not is_dashing and (
            circle_rect_collision((enemy1.x, enemy1.y), enemy1.radius, player_rect) or
            circle_rect_collision((enemy2.x, enemy2.y), enemy2.radius, player_rect) or
            circle_rect_collision((homing_enemy.x, homing_enemy.y), homing_enemy.radius, player_rect)
        ):
            title_screen()

        # Draw everything
        screen.fill(WHITE)
        for wall in walls:
            pygame.draw.rect(screen, BLACK, wall)
        pygame.draw.rect(screen, player_color, player_rect)
        enemy1.draw(screen)
        enemy2.draw(screen)
        homing_enemy.draw(screen)

        pygame.display.flip()
        clock.tick(60)

def title_screen():
    while True:
        screen.fill(WHITE)
        title_text = font.render("Press Button to Start", True, BLACK)
        start_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 80)
        exit_button = pygame.Rect(SCREEN_WIDTH - 160, 20, 140, 60)

        pygame.draw.rect(screen, BLUE, start_button)
        pygame.draw.rect(screen, RED, exit_button)

        start_text = small_font.render("Start", True, WHITE)
        exit_text = small_font.render("Exit", True, WHITE)

        screen.blit(title_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 100))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2 + 20))
        screen.blit(exit_text, (SCREEN_WIDTH - 120, 35))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game_loop()
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

title_screen()
