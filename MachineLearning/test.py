
# Import opencv
import cv2 

# Import uuid
import uuid

# Import Operating System
import os

# Import time
import time

# Import Keyboard
import keyboard

# Import Threading
import threading

labels = ['thumbsup', 'thumbsdown', 'thankyou', 'livelong']
number_imgs = 5

IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')

# os.path.exists(IMAGES_PATH)

# if not os.path.exists(IMAGES_PATH):
#     if os.name == 'nt':
#          !mkdir {IMAGES_PATH}
# for label in labels:
#     path = os.path.join(IMAGES_PATH, label)
#     if not os.path.exists(path):
#         !mkdir {path}


def output():
    global frame
    print('entered output')
    if cap.isOpened():
        print("[LOG] " + f'front vid // selected port is "0"')
    while True:
        global frame
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord('q'):
            print('q pressed, breaking')
            exit()
            break
        else:
            continue
    cap.release()
    cv2.destroyAllWindows()
    
        

def threader():
    global cap
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    th = threading.Thread(target= output)
    th.start()
    print('thread initialized')
    print(cap.isOpened())
    if cap.isOpened():
        th1 = threading.Thread(target= __capture__)
        th1.start()

    if keyboard.is_pressed('q'):
        th.join() # maybe use th.terminate()
        th1.join()


def __capture__():    
    print('entered capture function')
    
    frame1 = frame.copy()
    i = 0
    y = 0
    print('[LOG] : entered for in loop -- label')
    while i <= number_imgs and y<= (len(labels)-1):
        print(f'Collecting images for {labels[y]}')
        if keyboard.is_pressed('c'):
                print('Collecting image {}'.format(i))
                imgname = os.path.join(IMAGES_PATH,labels[y],labels[y]+'.'+'{}.jpg'.format(str(uuid.uuid1())))
                cv2.imwrite(imgname, frame)
                cv2.putText(frame1, 'Captured', (640, 360), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 255, 0), 2)
                i +=1
                time.sleep(2)
                if i == number_imgs:
                    y+=1
                if keyboard.is_pressed('q'):
                    cv2.release
                    exit()
        else:
            continue
                


threader()


        


