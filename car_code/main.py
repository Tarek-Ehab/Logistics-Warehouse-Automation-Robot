from collections.abc import Callable, Iterable, Mapping
from typing import Any
import cv2
from image_detection.cam import    scan_box, get_fram_data ,cap 
import threading
from line_follower.line_flower import *
from arm.arm_v3 import*
from web_connection.client import get_access,Socket_clinet
from a_star.Shelve import get_path_data
host_ip = '192.168.100.24:8000'
delevier_shalf = 'Ten'
start_point = 'A'
'''    
    difference_x = 0
    diffdifference_y = 0
    try  :
        while True :
            frame, difference_x ,difference_y ,objects =get_fram_data()
            print(difference_x , difference_y , "main")
            cv2.imshow('frame', frame)
            if difference_x < 14 and difference_y > -14 and len(objects) > 0:
                stop()
                # break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break
    except:
        stop()
        cap.release()
        cv2.destroyAllWindows()
'''
def captuer_object(orentation):
    print('try to cap')
    open_gripper()
    time.sleep(0.2)
    flow_path([get_mid_config(orentation),get_grib_config(orentation)])
    time.sleep(0.5)
    close_gripper()
    time.sleep(0.2)
    flow_path([get_mid_config(orentation),home_config])
def relase_object(orentation):
    flow_path([get_mid_config(orentation),get_relse_config(orentation)])
    time.sleep(1)
    open_gripper()
    time.sleep(1)
    flow_path([get_mid_config(orentation),home_config])


def main_funciton():
    global delevier_shalf , start_point
    try  :
        while (True):
            try:
                access = get_access(host_ip)
                if access !="" :
                    socket_connnection = Socket_clinet(access , host_ip)
                    break
                time.sleep(0.5)
            except:
                print('error in logging to sever ',Exception)
        while socket_connnection.recive_data():
            try : 
                if 'id' in socket_connnection.order_data:
                    print('recivie order ',socket_connnection.order_data)
                    socket_connnection.set_active()
                    break
                time.sleep(0.5)
            except Exception:
                print('error in creciving data fomr ',Exception)
        pickup_data , delever_data = get_path_data(
            socket_connnection.order_data['product']['shelf']['name'],delevier_shalf,start_point)
        print(pickup_data , delever_data)
        flow_path([home_config])
        line_follower_code(pickup_data[0])
        flow_path([get_red_qr_config(pickup_data[2])])
        is_back = False
        is_force_to_stop = False
        while True:
            print('before the fream')
            frame,difference_x,difference_y ,decodedObjects = get_fram_data()
            print("show video fram ")
            if (pickup_data[2]=='R'):
                if difference_x < -10:
                    print("is_frowared")
                    acc(0.2,go_backward)
                    is_back = True
                elif difference_x >10:
                    print("is_back")
                    acc(0.2,go_forward)
                else :
                    print("stop show")
                    stop()
                    cap.release()
                    cv2.destroyAllWindows()
                    break
            else :
                if difference_x < -10:
                    print("is_frowared")
                    acc(0.2,go_forward)
                    
                elif difference_x >10:
                    print("is_back")
                    acc(0.2,go_backward)
                    is_back = True
                else :
                    print("stop show")
                    stop()
                    cap.release()
                    cv2.destroyAllWindows()
                    break
            
            cv2.imshow('frame', frame)
            print("show video ")
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                is_force_to_stop =True
                stop()
                cap.release()
                cv2.destroyAllWindows()
                break
        print(is_force_to_stop)      
        if not is_force_to_stop :
            captuer_object(pickup_data[2])
            if is_back:
                    flow_line()
                    is_back = False
            line_follower_code(delever_data[0])
            relase_object(delever_data[2])
        socket_connnection.set_ordere_arrrived()
    except : 
        cap.release()
        cv2.destroyAllWindows()
        stop()

main_funciton()