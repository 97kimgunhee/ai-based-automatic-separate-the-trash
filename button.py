from pickle import TRUE
import Jetson.GPIO as GPIO
import time
import motor
from cv2 import BFMatcher
def Start_Botton():
    GPIO.setmode(GPIO.BOARD)
    inPin=15
    GPIO.setup(inPin,GPIO.IN)

    while TRUE:
        x=GPIO.input(inPin)
        if x==0:
            print("!!button!!")
            time.sleep(1)
            motor.Start_Separate("YOLO")
            print("end")
    GPIO.cleanup()