##import car_cam
import car_motor
import cv2
import sys
import time
from pubnub import Pubnub
from threading import Thread

pubnub = Pubnub(publish_key='pub-c-d1c59d19-6cf9-4dd9-a3ae-2811462c8506',
                    subscribe_key='sub-c-49f8db72-3b97-11e6-85a4-0619f8945a4f')
channel = 'car1'
channel2 = 'v2v'

x = 0
y = 0

def callback(m):
    print(m)
    
def _callback(m, channel):
    x = m['X']
    y = m['Y']
    print(x)
    print(y)
    data = {
        X : x
        Y : y
    }
    pubnub.publish(channel2, data, callback = callback, error = callback) 
def _error(m):
    print(m)

pubnub.subscribe(channels=channel, callback=_callback, error=_error)

img = cv2.imread('v.jpg') # load a dummy image

def shell_listen():
    while(1):
        c = 'r'
        car_motor.stop()
        c = raw_input('Waiting for shell input...')
        if  c=='w':  # UP
            car_motor.forward(0.5)
            print 'foreward'
            continue
        elif c=='s':  # Down
            print 'reverse'
            car_motor.reverse(0.5)
            continue
        elif c=='a':  # Left
            print 'left'
            car_motor.turn_left(0.5)
            continue
        elif c=='d':  # Right
            print 'right'
            car_motor.turn_right(0.5)
            continue
        elif c=='q':  # Right
            car_motor.stop()
            print 'Exit'
            break
            continue
        else:
            car_motor.stop()
        car_motor.stop()

def cv_listen():
    while(1):

        cv2.imshow('img',img)
        k = cv2.waitKey(33)
        if k==27:    # Esc key to stop
            break
        elif k==ord('w'):  # UP
            print 'foreward'
            car_motor.forward(0.001)
            continue
        elif k==ord('s'):  # Down
            print 'reverse'
            car_motor.reverse(0.001)
            continue
        elif k==ord('a'):  # Left
            print 'left'
            car_motor.turn_left(0.001)
            continue
        elif k==ord('d'):  # Right
            print 'right'
            car_motor.turn_right(0.001)
            continue
        elif k==ord('q'):  # Right 
            print 'Exit'
            break
            continue
        else:
            car_motor.stop()
            
    cv2.destroyAllWindows()
        
if __name__ == '__main__':
    Thread(target = shell_listen).start()
##    Thread(target = cv_listen).start()
   



    
##        DownKey : 2621440
##LeftKey : 2424832
##RightKey: 2555904
