#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    while True:
        if wall_is_on_the_right() and wall_is_above():
            move_down(n=9)
            move_left(n=9)
            break
        if wall_is_on_the_left() and wall_is_above():
            move_right(n=9)
            move_down(n=9)
            break
        if wall_is_on_the_left() and wall_is_beneath():
            move_up(n=9)
            move_right(n=9)
            break
        if wall_is_on_the_right() and wall_is_beneath():
            move_up(n=9)
            move_left(n=9)
            break
            
if __name__ == '__main__':
    run_tasks()
