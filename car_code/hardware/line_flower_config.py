from .hardware_config import GPIO

front_leftmost_pin = 17
front_left_pin = 27
front_center_pin = 18
front_right_pin = 23
front_rightmost_pin = 24
back_leftmost_pin = 21
back_left_pin = 20
back_center_pin = 16
back_right_pin = 19
back_rightmost_pin = 26


# Set up input pins
GPIO.setup(front_leftmost_pin, GPIO.IN)
GPIO.setup(front_left_pin, GPIO.IN)
GPIO.setup(front_center_pin, GPIO.IN)
GPIO.setup(front_right_pin, GPIO.IN)
GPIO.setup(front_rightmost_pin, GPIO.IN)
GPIO.setup(back_leftmost_pin, GPIO.IN)
GPIO.setup(back_left_pin, GPIO.IN)
GPIO.setup(back_center_pin, GPIO.IN)
GPIO.setup(back_right_pin, GPIO.IN)
GPIO.setup(back_rightmost_pin, GPIO.IN)

def read_front_line():
    leftmost = GPIO.input(front_leftmost_pin)
    left = GPIO.input(front_left_pin)
    center = GPIO.input(front_center_pin)
    right = GPIO.input(front_right_pin)
    rightmost = GPIO.input(front_rightmost_pin)
    stop_point = (leftmost+left+right+rightmost) == 4
    line_list=[leftmost, left, center, right, rightmost]
    return line_list ,stop_point

def read_back_line()->tuple[list,bool]:
    leftmost = GPIO.input(back_leftmost_pin)
    left = GPIO.input(back_left_pin)
    center = GPIO.input(back_center_pin)
    right = GPIO.input(back_right_pin)
    rightmost = GPIO.input(back_rightmost_pin)
    stop_point = (leftmost+left+right+rightmost) == 4
    line_list=[leftmost, left, center, right, rightmost]
    return line_list ,stop_point
