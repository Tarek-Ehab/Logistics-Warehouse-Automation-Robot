from .hardware_config import pca
from adafruit_motor import servo

right_back = servo.Servo(pca.channels[12],min_pulse=1416-35, max_pulse=1517+35)
right_front = servo.Servo(pca.channels[13],min_pulse=1411-35, max_pulse=1517+34)
left_back  = servo.Servo(pca.channels[14],min_pulse=1416-35, max_pulse=1517+35)
left_front = servo.Servo(pca.channels[15],min_pulse=1416-35, max_pulse=1517+34)
