from .hardware_config import pca
from adafruit_motor import servo

base     = servo.Servo(pca.channels[0],min_pulse=500, max_pulse=2500)
shoulder = servo.Servo(pca.channels[1],min_pulse=500, max_pulse=2500)
elbow_1  = servo.Servo(pca.channels[2],min_pulse=500, max_pulse=2500)
elbow_2  = servo.Servo(pca.channels[3],min_pulse=500, max_pulse=2500)
wrist    = servo.Servo(pca.channels[4],min_pulse=500, max_pulse=2500)
gripper  = servo.Servo(pca.channels[5],min_pulse=500, max_pulse=2500)