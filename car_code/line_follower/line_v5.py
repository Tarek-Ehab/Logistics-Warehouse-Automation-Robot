import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))
from hardware.line_flower_config import *
from move.move_v6 import *
P = 0
I = 0
D = 0
last_error = 0 
prev_error = 0

def reading_line_follower():
    # Read sensor inputs
    # Read sensor inputs
    leftmost,left,center,right,rightmost = read_front_line()
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
            L_value = l_reading+center*0.25
    print(L_value,R_value)
    error= L_value -R_value
    force_stop = sum(line_list)==5
    stop_point = (leftmost+left+right+rightmost) == 4
    return (error, stop_point,force_stop)
#R is negive -> move left 
#l is postive -> move right 
def move(error):
        global last_error ,prev_error
        if error == -1.5:
            forward_left_half(0.9)  
            forward_right_half(0.5)
        elif error ==-1 :
            forward_left_half(0.9)  
            forward_right_half(0.7)
        elif error == -0.5 : 
            forward_left_half(0.9)
            forward_right_half(0.8)
        elif error == -0.25 and prev_error == -0.5 :
            forward_left_half(0.7)
            forward_right_half(0.9)
        elif error == -0.25 :
            forward_left_half(0.9)
            forward_right_half(0.8)
        elif error == 0.25 :
            forward_left_half(0.8)
            forward_right_half(0.9)
        elif error == 0.25 and prev_error ==0.5:
            forward_left_half(0.9)
            forward_right_half(0.7)
        elif error == 0.5 :
            forward_left_half(0.8)  
            forward_right_half(0.9)   
        elif error == 1 :
            forward_left_half(0.7)  
            forward_right_half(0.9)
        elif error == 1.5:
            forward_left_half(0.5)
            forward_right_half(0.9)
        else:
            forward_left_half(0.9)
            forward_right_half(0.9)
        print('error',error , 'prev_error' ,prev_error)
        if last_error != error: 
            prev_error = last_error
            last_error = error


def line_forward():
    print("*****************************************************")
    reding , stop_point = read_line()
    print('stop piont ', stop_point)
    go_forward(0.5)
    while stop_point:
        reding , stop_point = read_line()
    print('line-folower')
    while True:
        error,stop_point,force_sotp=reading_line_follower()
        print('error : ',error,'stop_point : ',stop_point,' ',force_sotp)
        if  force_sotp or stop_point ==True:
            print('stop')
            go_forward(0.8)
            time.sleep(.3)
            stop()
            return
        move(error)

def line_follower_code(directions):
    
    for i in directions:
        if i == 'F':
            line_forward()
        elif i == 'TR':
            turn_right()
            line_forward()
        elif i == 'TL':
            turn_left()
            line_forward()
        elif i == 'TRR':
            turn_right()
            line_forward()
        else:
            stop()
            print ("Error in knowing the direction")
            return
    return "Done"

def turn_right():
    ls,stop_point= read_front_line()
    print(ls)
    turn_right_cw(0.8)
    r_flag = 0
    l_flag = 0
    time.sleep(3)
    turn_right_cw(0)
def turn_left():
    turn_left_ccw(0.8)
    r_flag = 0
    l_flag = 0
    # while not (r_flag ==2 and l_flag==2):
    #     ls,stop_point= read_line()
    #     if (ls[0] == 0 and r_flag == 0)or(ls[0] == 1 and r_flag ==1 ):
    #         r_flag +=1
    #     if (ls[-1] == 0 and l_flag == 0)or(ls[-1] == 1 and l_flag ==1 ):
    #         l_flag +=1
    #     print(ls , r_flag, l_flag)
    time.sleep(3)
    turn_left_ccw(0)
if __name__ == "__main__":
    try : 
        line_follower_code(['TR','F','TL','F','TR'])
        print(read_front_line())
        stop()
    except :
        stop()