import sys , os
import time 
# setting path
sys.path.append(os.path.dirname(sys.path[0]))
from hardware.motors_config import *
from hardware.line_flower_config import*
from move.move_v6 import *
def calculate_error(front_ir):
    left = 1-front_ir[1]
    mid = 1-front_ir[2]
    right = 1-front_ir[3]
    print(left , mid, right, )
    if right == 1:
        right= right + mid
    elif left == 1:
        left = left+mid
    print('Error' , right - left)
    return right - left

def flow_line():
    acc(0.3,go_forward)
    front_ir,front_stop = read_front_line()
    back_ir ,back_stop = read_back_line()
    while front_stop :
        print(front_ir,back_ir)
        front_ir,front_stop = read_front_line()
        back_ir ,back_stop = read_back_line()
        time.sleep(0.07)

    while not back_stop or not front_stop:
        front_ir,front_stop = read_front_line()
        back_ir ,back_stop = read_back_line()
        print(front_ir,back_ir)
        error = calculate_error(front_ir)
        speed_right = 0.6 +0.15*error
        speed_left  = 0.6 -0.15*error
        forward_right_half(speed_right)
        forward_left_half(speed_left)
        if speed_right >1 :
            speed_right = 1
        elif speed_right <0 :
            speed_right =0 
        if speed_left >1 :
            speed_left = 1
        elif speed_left <0 :
            speed_left =0 
    stop()
    print(error)

def turn_right():
    acc(0.6,turn_right_cw)
    # front_line_lest, is_stop_front = read_front_line()
    # back_line_lest,  is_stop_back = read_back_line()
    # while is_stop_front or is_stop_back :
    #     front_line_lest, is_stop_front = read_front_line()
    #     back_line_lest,  is_stop_back = read_back_line()
    #     print(front_line_lest, is_stop_front)
    #     print(back_line_lest,  is_stop_back)
    #     time.sleep(0.07)
    # while not is_stop_front or not is_stop_back :
    #     front_line_lest, is_stop_front = read_front_line()
    #     back_line_lest,  is_stop_back = read_back_line()
    #     print(front_line_lest, is_stop_front)
    #     print(back_line_lest,  is_stop_back)
    #     time.sleep(0.07)
    time.sleep(3.5)
    stop()
    time.sleep(0.1)


def turn_left():
    acc(0.6,turn_left_ccw)
    # front_line_lest, is_stop_front = read_front_line()
    # back_line_lest,  is_stop_back = read_back_line()
    # while is_stop_front or is_stop_back :
    #     front_line_lest, is_stop_front = read_front_line()
    #     back_line_lest,  is_stop_back = read_back_line()
    #     print(front_line_lest, is_stop_front)
    #     print(back_line_lest,  is_stop_back)
    #     time.sleep(0.07)
    # while not is_stop_front or not is_stop_back :
    #     front_line_lest, is_stop_front = read_front_line()
    #     back_line_lest,  is_stop_back = read_back_line()
    #     print(front_line_lest, is_stop_front)
    #     print(back_line_lest,  is_stop_back)
    #     time.sleep(0.07)
    time.sleep(3)
    stop()
    time.sleep(0.1)

def line_follower_code(directions):
    
    for i in directions:
        if i == 'F':
            flow_line()
        elif i == 'TR':
            turn_right()
            flow_line()
        elif i == 'TL':
            turn_left()
            flow_line()
        elif i == 'TRR':
            turn_right()
            turn_right()
            flow_line()
        else:
            stop()
            print ("Error in knowing the direction")
            return
    return "Done"

if __name__ == "__main__":
    try:
        line_follower_code(['F'])
    # is_back = False
    # is_left = True
    except KeyboardInterrupt:
        print('key intrupt ')
        stop()
