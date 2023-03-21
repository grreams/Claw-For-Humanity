#!/usr/bin/env python

# # 1. Import Dependencies


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

from IPython import get_ipython 


# # 2. Define Images to Collect


labels = ['thumbsup', 'thumbsdown', 'thankyou', 'livelong']
number_imgs = 5


# # 3. Setup Folders 


IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')



os.path.exists(IMAGES_PATH)



if not os.path.exists(IMAGES_PATH):
    if os.name == 'nt':
         get_ipython().system('mkdir {IMAGES_PATH}')
for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        get_ipython().system('mkdir {path}')


# # 4. Capture Images

# In[43]:


def __initialize__():
    print('[LOG] : entered initialize')
    global cap
    camPort = 0
    cap = cv2.VideoCapture(camPort)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    if cap.isOpened():
        print("[LOG] " + f'front vid // selected port is "{camPort}"')
    else:
        print('cap is not open')
        exit()
    
    print('[LOG] : exit initialize')


__initialize__()


for label in labels:
    print('[LOG] : entered for in loop -- label')
    print('Collecting images for {}'.format(label))
    time.sleep(5)

    for imgnum in range(number_imgs):
        print('[LOG] : entered for in loop -- imgnum')
        
        global imgname
        print('Collecting image {}'.format(imgnum))
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        
        while True:
            print('[LOG] : entered while loop')
            global cap
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            if keyboard.is_pressed('c'):
                cv2.imwrite(imgname, frame)
                cv2.putText(frame, 'Captured', (640, 360), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 255, 0), 2)
                time.sleep(2)
            else:
                break


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()


# # # 5. Image Labelling



# get_ipython().system('pip install --upgrade pyqt5 lxml')




# LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')



# if not os.path.exists(LABELIMG_PATH):
#     get_ipython().system('mkdir {LABELIMG_PATH}')
#     get_ipython().system('git clone https://github.com/tzutalin/labelImg {LABELIMG_PATH}')



# if os.name == 'posix':
#     get_ipython().system('make qt5py3')
# if os.name =='nt':
#     get_ipython().system('cd {LABELIMG_PATH} && pyrcc5 -o libs/resources.py resources.qrc')



# get_ipython().system('cd {LABELIMG_PATH} && python labelImg.py')


# # # 6. Move them into a Training and Testing Partition

# # # OPTIONAL - 7. Compress them for Colab Training


# TRAIN_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'train')
# TEST_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'test')
# ARCHIVE_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'archive.tar.gz')



# get_ipython().system('tar -czf {ARCHIVE_PATH} {TRAIN_PATH} {TEST_PATH}')






