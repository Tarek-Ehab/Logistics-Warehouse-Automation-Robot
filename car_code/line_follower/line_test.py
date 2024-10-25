import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))
from hardware.line_flower_config import *
from move.move_v6 import *


def reading_line_follower():
    # Read sensor inputs
    # Read sensor inputs
    leftmost = GPIO.input(front_leftmost_pin)
    left = GPIO.input(front_left_pin)
    center = GPIO.input(front_center_pin)
    right = GPIO.input(front_right_pin)
    rightmost = GPIO.input(front_rightmost_pin)
    line_list=[leftmost, left, center, right, rightmost]
    print(line_list)
    R=False
    R_value=0
    L_value=0
    if leftmost !=0 and center !=0 :
        L_value = 1.5
    if rightmost !=0 and center!=0 :
        R_value = 1.5
    else :
        right_reading = abs(right*0.5-rightmost*1.5)
        if right_reading > 0 :
            R_value = right_reading-center*0.25
        l_reading = abs(left*0.5-leftmost*1.5)
        if l_reading >0:
            L_value = l_reading-center*0.25
    print(L_value,R_value)
    error= L_value -R_value
    force_stop = sum(line_list)==5
    stop_point = (leftmost+left+right+rightmost) == 4
    return (error, stop_point,force_stop)
#R is negive -> move left 
#l is postive -> move right 
def move(error:int):
        error=error/6
        if error>1:
            error=1
        elif error<-1:
            error = -1
        if error < 0:
            error = abs(error)
            forward_right_half(1-error)
            forward_left_half(1)
        elif error > 0 :
            forward_right_half(1)
            forward_left_half(1-error)
        elif error == 0:
            forward_right_half(1)
            forward_left_half(1)
    
if __name__ == "__main__":
   # Start the robot
  while True:
        # error,stop_point,force_sotp=reading_line_follower()
        # print('error : ',error,'stop_point : ',stop_point,' ',force_sotp)
        # time.sleep(1)
        print('f',read_front_line())
        print('b',read_back_line())

        time.sleep(1)



  

