from tkinter import messagebox
import pygame
import random
from pygame.locals import *
import popup

# variables
size = width, height = (1200, 700)
road_w = int(width / 1.5)
roadmark_w = int(width / 90)
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4
speed = 1

# game init and setup
pygame.init()

FONT = pygame.font.SysFont('arial', 20)

running = True


def background():
    global screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("YOLO Car Run")
    screen.fill((60, 220, 0))


# loading asset
car = pygame.image.load("asset/player.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.8


def randomizeFun():
    vec = ["asset/police.png", "asset/taxi.png", "asset/truck.png", "asset/truck1.png", "asset/truck2.png"]
    opp_vec = random.choice(vec)
    return opp_vec


def car2load():
    choice_vec = randomizeFun()
    opp2 = pygame.image.load(choice_vec)
    return opp2


def details():
    global speed, score
    text_1 = FONT.render(f'Speed:  {str(speed)}', True, (0, 0, 0))
    text_2 = FONT.render(f'Score:  {score}', True, (0, 0, 0))
    text_3 = FONT.render(f'Race YOLOv5', True, (0, 0, 0))

    screen.blit(text_1, (50, 50))
    screen.blit(text_2, (50, 150))
    screen.blit(text_3, (50, 250))


def display_set():
    # setting up the display
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))
    pygame.draw.rect(screen, (255, 240, 60), (width / 2 - roadmark_w / 2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_w / 2 + roadmark_w * 1, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_w / 2 - roadmark_w * 2, 0, roadmark_w, height))


car2 = pygame.image.load("asset/police.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height * 0.2

counter = 0
score = 0
# run the game with events
while running:
    background()
    details()
    counter += 1

    if counter == 1024:
        speed += 0.25
        counter = 0
        print("Level up", speed)

    # opposite car logic
    car2_loc[1] += speed
    if car2_loc[1] > height:
        score += 1
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    # event handler
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w / 2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w / 2), 0])
    # collapse
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        popup.askMe()

    display_set()

    # display block
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)

    # for random car
    a = 2
    a *= 1.5
    randcar = car2_loc[1] + a
    if randcar > height:
        opp_vec1 = car2load()
        car2 = opp_vec1

    pygame.display.update()

pygame.quit()
