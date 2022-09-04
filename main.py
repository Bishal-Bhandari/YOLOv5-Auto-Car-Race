import selectCar
import cv2
import numpy as np
import pygame
import random
import torch
from pygame.locals import *
import popup
import DataFeedCap

# variables
size = width, height = (800, 800)
road_w = int(width / 1.5)
roadmark_w = int(width / 90)
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4 + 1
speed = 2
divider = [-720, -600, -480, -360, -240, -120, 0, 120, 240, 360, 480, 600, 720]

# load model
model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5\\runs\\train\\exp7\\weights\\last.pt', force_reload=True)

# game init and setup
pygame.init()

FONT = pygame.font.SysFont('freesansbold', 25)
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

car2 = pygame.image.load("asset/police.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height * 0.2


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
    text_3 = FONT.render(f'Race YOLOv5', True, (255, 0, 0))

    screen.blit(text_1, (10, 250))
    screen.blit(text_2, (10, 150))
    screen.blit(text_3, (10, 50))


def display_set():
    # setting up the display
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))


def divider_fun(val):
    for i in range(len(divider)):
        pygame.draw.rect(screen, (255, 255, 255), (width / 2 - roadmark_w / 2, divider[i] + val, roadmark_w, 60))
        pygame.draw.rect(screen, (255, 255, 255),
                         (width / 2 - road_w / 2 + roadmark_w * 1, divider[i] + val, roadmark_w, 60))
        pygame.draw.rect(screen, (255, 255, 255),
                         (width / 2 + road_w / 2 - roadmark_w * 2, divider[i] + val, roadmark_w, 60))


counter = 0
score = 0
div_move = 0
frame_count = 0
# run the game with events
while running:
    background()
    details()
    counter += 1

    if counter == 1024:
        speed += 0.25
        counter = 0

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
            if event.key in [K_a, K_LEFT] and car_loc[0] > 142:
                car_loc = car_loc.move([-int(road_w / 2), 0])
            if event.key in [K_d, K_RIGHT] and car_loc[0] < 408:
                car_loc = car_loc.move([int(road_w / 2), 0])

    # collapse
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        popup.askMe()

    display_set()

    # for divider in mid UI
    if counter == 1024:
        div_move += 1.25
    else:
        div_move += 1
    divider_fun(div_move)
    if div_move == 800:
        div_move = 1

    # display block
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)

    # for random car
    # a = 2
    # a *= 1.5
    # rand_car = car2_loc[1] + a
    # if rand_car > height:
    #     opp_vec1 = car2load()
    #     car2 = opp_vec1

    #  Capture screen for detection
    screen_grab = DataFeedCap.capture_dynamic()
    result = model(screen_grab)
    from_selectCar = selectCar.carSelect(result, car_loc, car2_loc)
    if screen_grab is None:
        print("No Window Found! Please Try Again")
        continue
    cv2.imshow('YOLO', np.squeeze(result.render()))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

    pygame.display.update()

pygame.quit()


# python train.py --img 640 --batch 10 --epochs 50 --data datasrc.yaml --weights yolov5s6.pt --cache
# python detect.py --weights D:\Project\YOLOgame\yolov5\runs\train\exp7\weights\last.pt --img 640 --conf 0.25 --source image-path
