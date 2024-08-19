import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

player = Player()

cars = []
car_timer = 0
car_count = 1
for i in range(1000):
    car = CarManager()
    cars.append(car)

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_timer += 1
    for i in range(car_count):
        cars[i].move_left()
        if player.distance(cars[i]) < 25:
            game_is_on = False
            game_over = GameOver()
            break

    if car_timer == 6 and car_count <= 1000:
        car_count += 1
        car_timer = 0

    if player.finish():
        player.reset_position()
        scoreboard.level_up()
        car_count = 1
        for i in range(len(cars)):
            cars[i].level_up()


screen.exitonclick()