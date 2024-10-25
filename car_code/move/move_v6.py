import sys , os
import time 
# setting path
sys.path.append(os.path.dirname(sys.path[0]))
from hardware.motors_config import *
# Speed functions
def positive_pwm(speed):
    speed *=10
    speed = 0.8+(0.02*speed)
    return speed

def negative_pwm(speed):

    speed *=10
    speed = 0.2-(0.02*speed)
    return speed

# Movement functions
def stop():
    right_front.fraction =  0.5
    right_back.fraction =  0.5
    left_front.fraction =  0.5
    left_back .fraction = 0.5

def go_forward(speed):
    forward_right_half(speed*0.96)
    forward_left_half(speed)

def go_backward(speed):
    backward_left_half(speed*0.96)
    backward_right_half(speed)

def turn_left_ccw(speed):
    forward_right_half(speed)
    backward_left_half(speed)

def turn_right_cw(speed):
    backward_right_half(speed)
    forward_left_half(speed)

def left(speed):
    front_half(speed,negative_pwm)
    back_half(speed , positive_pwm)

def right(speed):
    front_half(speed, positive_pwm)
    back_half(speed*0.8, negative_pwm)


def front_half(speed,command):
    right_front.fraction = command(speed)
    left_front.fraction = command(speed)

def back_half(speed,command):
    right_back.fraction = command(speed)
    left_back.fraction = command(speed)

def right_half(speed,command):
    right_front.fraction = command(speed)
    right_back.fraction = command(speed)

def left_half(speed, command):
    left_front.fraction = command(speed)
    left_back.fraction = command(speed)


def forward_right_half(speed):
    right_front.fraction = negative_pwm(speed)
    right_back.fraction  = negative_pwm(speed)
    
def forward_left_half(speed):
    left_front.fraction  =  positive_pwm(speed)
    left_back .fraction  = positive_pwm(speed)

def backward_right_half(speed):
   right_front.fraction =  positive_pwm(speed)
   right_back.fraction  = positive_pwm(speed)

def backward_left_half(speed):
    left_front.fraction  =  negative_pwm(speed)
    left_back .fraction  = negative_pwm(speed)


def acc(limit_speed:int,comand):
    speed = 0.15
    while True:
        speed += 0.05
        if speed <limit_speed:
            comand(speed)
            time.sleep(0.05)
        else :
            comand(limit_speed)
            break

def flow_right():
    is_stop = False
    front_reading ,is_front_stop = read_front_line()
    back_reading , is_back_stop =  read_back_line()
    print('f',front_reading)
    print('b',back_reading)
    if front_reading[-1] ==0 :
        print("font out ")
        front_half(1,positive_pwm)
        back_half(0.6 ,negative_pwm)
    elif back_reading[-1] ==0 :
        print('backout')
        front_half(0.6,positive_pwm)
        back_half(1 ,negative_pwm)
    elif front_reading[2] and is_front_stop and back_reading[2] and is_back_stop :
        stop()
    else:
        right(0.6)
    return is_stop

# def flow_left():
#     is_stop = False
#     front_reading ,is_front_stop = read_front_line()
#     back_reading , is_back_stop =  read_back_line()
#     print('f',front_reading)
#     print('b',back_reading)
#     if front_reading[0] !=0 and not is_back_stop :
#         front_half(0.8,negative_pwm)
#         back_half(1 ,positive_pwm)
#     elif back_reading[-1] !=0 and not is_front_stop:
#         front_half(1,negative_pwm)
#         back_half(0.8 ,positive_pwm)
#     elif front_reading[2] and is_front_stop and back_reading[2] and is_back_stop :
#         stop()
#         is_stop = True
#     else:
#         left(1)
#     return is_stop


# if __name__ == "__main__":
#     try:
#         turn_right()
#     # is_back = False
#     # is_left = True
#     except KeyboardInterrupt:
#         print('key intrupt ')
#         stop()



    