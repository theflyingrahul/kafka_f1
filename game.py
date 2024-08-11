import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Car dimensions
car_width = 50
car_height = 60

# Load car image
car_img = pygame.image.load('car.png')
car_img = pygame.transform.scale(car_img, (car_width, car_height))

# Game variables
clock = pygame.time.Clock()
car_x = (screen_width * 0.45)
car_y = (screen_height * 0.8)
car_speed = 5
obstacle_speed = 7
obstacle_width = 50
obstacle_height = 50
num_obstacles = 3
obstacles = []

lap_distance = 2000  # meters
laps_to_finish = 5
meters_per_frame = 5
lap_count = 0
distance_covered = 0
start_time = time.time()
lap_times = []

# Font
font = pygame.font.SysFont(None, 25)

def display_message(text, position):
    screen_text = font.render(text, True, white)
    screen.blit(screen_text, position)

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, red, [obstacle['x'], obstacle['y'], obstacle_width, obstacle_height])

def generate_obstacles(num):
    return [{'x': random.randrange(0, screen_width - obstacle_width), 'y': -600 * i} for i in range(num)]

def game_loop():
    global car_x, car_y, car_speed, lap_count, distance_covered, obstacles, start_time, lap_times

    game_exit = False
    game_over = False

    obstacles = generate_obstacles(num_obstacles)

    while not game_exit:

        while game_over:
            display_message("You crashed! Press R to Restart or Q to Quit", [screen_width / 2 - 150, screen_height / 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_r:
                        car_x = (screen_width * 0.45)
                        car_y = (screen_height * 0.8)
                        distance_covered = 0
                        # lap_count = 0
                        obstacles = generate_obstacles(num_obstacles)

                        start_time = start_time - 5
                        game_over = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x -= 30
                if event.key == pygame.K_RIGHT:
                    car_x += 30
                if event.key == pygame.K_UP:
                    car_speed += 1
                if event.key == pygame.K_DOWN:
                    car_speed = max(1, car_speed - 1)  # Ensure speed doesn't go below 1

        if car_x > screen_width - car_width or car_x < 0:
            game_over = True

        screen.fill(black)

        for obstacle in obstacles:
            draw_obstacles(obstacles)
            obstacle['y'] += obstacle_speed + car_speed

            if obstacle['y'] > screen_height:
                obstacle['y'] = -obstacle_height
                obstacle['x'] = random.randrange(0, screen_width - obstacle_width)

            if car_y < obstacle['y'] + obstacle_height:
                if car_x > obstacle['x'] and car_x < obstacle['x'] + obstacle_width or car_x + car_width > obstacle['x'] and car_x + car_width < obstacle['x'] + obstacle_width:
                    game_over = True

        if not game_over:
            distance_covered += meters_per_frame + car_speed

            if distance_covered >= lap_distance:
                lap_count += 1
                distance_covered = 0

                # Clock the lap time
                lap_time = time.time() - start_time
                lap_times.append(lap_time)
                start_time = time.time()

            # Draw finish line for lap
            if distance_covered >= lap_distance - 100:
                pygame.draw.line(screen, green, (0, car_y - 50), (screen_width, car_y - 50), 5)

            screen.blit(car_img, (car_x, car_y))

        if lap_count >= laps_to_finish:
            screen.fill(black)
            display_message("You Finished the Game!", [screen_width / 2 - 100, screen_height / 2])
            pygame.display.update()
            pygame.time.wait(20000)
            game_exit = True

        # Display the overall time and lap times
        elapsed_time = sum(lap_times) + (time.time() - start_time if not game_over else 0)
        display_message(f"Total Time: {int(elapsed_time)}s", [10, 10])

        for i, lap_time in enumerate(lap_times):
            display_message(f"Lap {i + 1}: {int(lap_time)}s", [10, 40 + i * 30])

        display_message(f"Laps: {lap_count}/{laps_to_finish}", [screen_width - 150, 10])
        display_message(f"Speed: {car_speed}", [screen_width - 150, 40])

        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    quit()

game_loop()
