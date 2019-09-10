#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
 while True:
  if not wall_is_above():
   move_up
   break
  if not wall_is_on_the_right():
   move_right
   break
  if not wall_is_on_the_left():
   move_left
   break
  if not wall_is_beneath():
   move_down
   break	 


if __name__ == '__main__':
    run_tasks()
