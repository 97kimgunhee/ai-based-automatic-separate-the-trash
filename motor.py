import Jetson.GPIO as GPIO
import time
import yolo
import serial
import cv2
ser = serial.Serial('/dev/ttyACM0', 9600)

def Send_MG(mg):
    if ser.readable():
        if mg == '1':
            mg = mg.encode('utf-8')
            ser.write(mg)
            print("go to dark Room")
            time.sleep(0.5)
        elif mg=='2':
            mg = mg.encode('utf-8')
            ser.write(mg)
            print("go to Can")
            time.sleep(0.5)
        elif mg=='3':
            mg = mg.encode('utf-8')
            ser.write(mg)
            print("go to glass")
            time.sleep(0.5)
        elif mg=='4':
            mg = mg.encode('utf-8')
            ser.write(mg)
            print("go to colored_PT")
            time.sleep(0.5)
        elif mg=='5':
            mg = mg.encode('utf-8')
            ser.write(mg)
            print("go to Transparent_PT")
            time.sleep(0.5)
        elif mg=='6':
            mg = mg.encode('utf-8')
            ser.write(mg)
            print("go to carton")
            time.sleep(0.5)
        elif mg=='7':
            mg = mg.encode('utf-8')
            ser.write(mg)
            time.sleep(0.5)
        elif mg=='8':
            mg = mg.encode('utf-8')
            ser.write(mg)
            time.sleep(0.5)
        elif mg=='0':
            mg = mg.encode('utf-8')
            ser.write(mg)
            print("go to return")
            time.sleep(0.5)
        
def Start_Separate(box):

    if box=="YOLO":
        Send_MG('1')
        time.sleep(13)
        yolo.Start_Detection(1)
        
    elif box=="can":
        Send_MG('2')
    ###################################    
    elif box=="glass":
        Send_MG('3')
    ###################################
    elif box=="colored_PT":
        Send_MG('4')
    ###################################
    elif box=="Transparent_PT":
        Send_MG('5')
    ###################################
    elif box=="carton":
        Send_MG('6')
    ###################################
    elif box=="label_PT" or box=="return":
        Send_MG('0')
    ###################################
   