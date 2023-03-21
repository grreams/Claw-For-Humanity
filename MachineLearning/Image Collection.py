#!/usr/bin/env python
# coding: utf-8

# # 1. Import Dependencies

# In[ ]:


get_ipython().run_line_magic('pip', 'install opencv-python')


# In[6]:


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


# # 2. Define Images to Collect

# In[7]:


labels = ['thumbsup', 'thumbsdown', 'thankyou', 'livelong']
number_imgs = 5


# # 3. Setup Folders 

# In[8]:


IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')


# In[9]:


os.path.exists(IMAGES_PATH)


# In[10]:


if not os.path.exists(IMAGES_PATH):
    if os.name == 'nt':
         get_ipython().system('mkdir {IMAGES_PATH}')
for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        get_ipython().system('mkdir {path}')


# # 4. Capture Images

# In[ ]:


z = 0

def output():
    print('entered output')
    if cap.isOpened():
        print("[LOG] " + f'front vid // selected port is "0"')
    while True:
        ret, frame = cap.read()
        frame1 = frame.copy()

        cv2.imshow('frame',frame)
        if z == 1:
            print('captured')
            cv2.putText(frame, 'Captured', (640, 360), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 255, 0), 2)
        else:
            print(f'z is {z}')
        if cv2.waitKey(1) == ord('q'):
            print('q pressed, breaking')
            exit()
            break
        else:
            continue
    cap.release()
    cv2.destroyAllWindows()
    
        


def __capture__():  
    global cap, z
    print('entered capture function')
    read, pictureFrame = cap.read()
    i = 0
    y = 0
    print('[LOG] : entered for in loop -- label')
    while i <= number_imgs and y<= (len(labels)-1):
        # print(f'Collecting images for {labels[y]}')
        if keyboard.is_pressed('c'):
                z = 1
                print('Collecting image {}'.format(i))
                imgname = os.path.join(IMAGES_PATH,labels[y],labels[y]+'.'+'{}.jpg'.format(str(uuid.uuid1())))
                cv2.imwrite(imgname, pictureFrame)
                i +=1
                time.sleep(1)
                if i == number_imgs:
                    y+=1
                if keyboard.is_pressed('q'):
                    cv2.release
                    exit()
        else:
            z = 0
            continue


def threader():
    global cap
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    th = threading.Thread(target= output)
    th1 = threading.Thread(target= __capture__)
    
    th.start()
    print('thread initialized \n')
    print(cap.isOpened())

    th1.start()
    print('thread1 initialized \n')

    if keyboard.is_pressed('q'):
        print('q pressed kill thread')
        th.join() # maybe use th.terminate()
        th1.join()


threader()


# # 5. Image Labelling

# In[ ]:


get_ipython().run_line_magic('pip', 'install --upgrade pyqt5 lxml')


# In[ ]:


LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')


# In[ ]:


if not os.path.exists(LABELIMG_PATH):
    get_ipython().system('mkdir {LABELIMG_PATH}')
    get_ipython().system('git clone https://github.com/tzutalin/labelImg {LABELIMG_PATH}')


# In[ ]:


if os.name == 'posix':
    get_ipython().system('make qt5py3')
if os.name =='nt':
    get_ipython().system('cd {LABELIMG_PATH} && pyrcc5 -o libs/resources.py resources.qrc')


# In[ ]:


get_ipython().system('cd {LABELIMG_PATH} && python labelImg.py')


# # 6. Move them into a Training and Testing Partition

# # OPTIONAL - 7. Compress them for Colab Training

# In[ ]:


TRAIN_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'train')
TEST_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'test')
ARCHIVE_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'archive.tar.gz')


# In[ ]:


get_ipython().system('tar -czf {ARCHIVE_PATH} {TRAIN_PATH} {TEST_PATH}')


# In[ ]:




