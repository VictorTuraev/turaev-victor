#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right(n=1)
    fill_cell()
    n=1
    for i in range(26*6):
        move_right()
        fill_cell()
        n=n+1
        if n>=27:
            n=1
            move_down()
            fill_cell()
            for i in range(26):
                move_left()
                fill_cell()
            move_down()
            fill_cell()


if __name__ == '__main__':
    run_tasks()
