import sys , os
import time 
# setting path
sys.path.append(os.path.dirname(sys.path[0]))
from hardware.arm_servo_config import *


def open_gripper():
    gripper.angle = 120

def close_gripper():
    gripper.angle = 160

class RobotConfigration():
    def __init__(self , base_angel=90 , shoulder_angle=48,eblow_1_angle=176,elbow_2_angle =170 ,wrist_angle = 0 , gripper_angle = 125) -> None:
        self.base_angle = base_angel
        self.shoulder_angle = shoulder_angle
        self.eblow_1_angle = eblow_1_angle
        self.elbow_2_angle = elbow_2_angle
        self.wrist_angle = wrist_angle
        self.gripper_angle = gripper_angle
    
home_config = RobotConfigration()
red_qr_config = RobotConfigration(base_angel=0,elbow_2_angle =162)
medel_config = RobotConfigration(base_angel= 0 ,elbow_2_angle=115)
grib_config = RobotConfigration(0,80,176,95,0,125)

def get_deg(orentation):
    if 'R' == orentation:
        return 0
    return 180

def get_red_qr_config(orentation):
    return RobotConfigration(base_angel=get_deg(orentation),elbow_2_angle =162)

def get_mid_config(orentation):
    return  RobotConfigration(get_deg(orentation),elbow_2_angle=115)

def get_grib_config (orentation):
    return RobotConfigration(get_deg(orentation),80,176,95,0,125)

def get_relse_config(orentation):
    return RobotConfigration(get_deg(orentation),85,176,110,0,125)


def set_robot_postion(config:RobotConfigration):

    elbow_1.angle = config.eblow_1_angle
    elbow_2.angle = config.elbow_2_angle
    wrist.angle = config.wrist_angle
    shoulder.angle = config.shoulder_angle
    base.angle = config.base_angle


def flow_path(postions=[]):
    for postion in postions:
        set_robot_postion(postion)
        time.sleep(2.5)

def grib_object ():
    open_gripper()
    flow_path( [red_qr_config,medel_config,grib_config])
    close_gripper()
    time.sleep(2)
    flow_path( [medel_config,home_config])

def set_object ():
    flow_path( [red_qr_config,medel_config,grib_config])
    open_gripper()
    time.sleep(2)
    flow_path( [medel_config,red_qr_config])

if __name__ == '__main__' : 
    # set_robot_postion(get_relse_config(180))
    # time.sleep(0.1)
    # open_gripper()
    # flow_path()
    flow_path([get_mid_config(180),home_config])