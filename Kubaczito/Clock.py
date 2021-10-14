from vpython import *
from datetime import datetime
import time


def make_big_box():
    return box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.4, 0.1, 0.1), color=color.black)


def make_small_box():
    return box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)


def make_rotation(hour_box, i):
    hour_box.rotate(angle=radians(-(360 / 12) * i), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))


def make_small_rotation(small_box, i, j):
    small_box.rotate(angle=radians(-(360 / 12) * i - (360 / 12) / 5 * j), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))


def rotate_boxes(boxes, x):
    for i in range(1, 5):
        make_small_rotation(boxes[i-1], x, i)


class Clock:
    def __init__(self):
        scene.center = vector(0, 0, 0)
        scene.forward = vector(-1, 0, 0)
        scene.up = vector(0, 1, 0)
        scene.width = 1920
        scene.height = 1080

        self.clock = cylinder(pos=vector(0, 0, 0), axis=vector(1, 0, 0), radius=5)
        self.middle_box = box(pos=vector(1.1, 0, 0), axis=vector(1, 0, 0), size=vector(0.5, 0.25, 0.25), color=color.black)
        self.pointers = [box(pos=vector(1.1, 2, 0), axis=vector(0, 1, 0), size=vector(4.25, 0.1, 0.1), color=color.red),
                         box(pos=vector(1.15, 1.5, 0), axis=vector(0, 1, 0), size=vector(3.5, 0.1, 0.2), color=color.green),
                         box(pos=vector(1.2, 1, 0), axis=vector(0, 1, 0), size=vector(2.75, 0.1, 0.25), color=color.blue)]

        self.hours = [make_big_box() for i in range(12)]
        [make_rotation(self.hours[i], i) for i in range(1, 12)]

        self.small_boxes = [[make_small_box() for j in range(4)] for i in range(12)]
        [rotate_boxes(self.small_boxes[i], i) for i in range(0, 12)]

    def set_actual_hour(self):
        now = datetime.now()

        self.pointers[0].rotate(angle=radians(-(360 / 60) * now.second), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
        self.pointers[1].rotate(angle=radians(-(360 / 3600) * (now.second + 60 * now.minute)), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
        self.pointers[2].rotate(angle=radians(-(360 / 86400 * 2) * (now.second + 60 * now.minute + 3600 * now.hour)), axis=vector(1, 0, 0),
                        origin=vector(1.2, 0, 0))

    def make_second(self):
        time.sleep(1)
        self.pointers[0].rotate(angle=radians(-(360 / 60)), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
        self.pointers[1].rotate(angle=radians(-(360 / 3600)), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
        self.pointers[2].rotate(angle=radians(-(360 / 86400)), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))


if __name__ == "__main__":
    clock = Clock()
    clock.set_actual_hour()
    while 1:
        clock.make_second()
