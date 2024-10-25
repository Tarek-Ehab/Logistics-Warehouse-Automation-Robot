import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50

