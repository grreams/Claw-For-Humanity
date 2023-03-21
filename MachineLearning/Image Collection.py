#!/usr/bin/env python
# coding: utf-8

# # 1. Import Dependencies

# In[ ]:


get_ipython().run_line_magic('pip', 'install opencv-python')


# In[1]:


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

# In[2]:


labels = ['thumbsup', 'thumbsdown', 'thankyou', 'livelong']
number_imgs = 5


# # 3. Setup Folders 

# In[3]:


IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')


# In[4]:


os.path.exists(IMAGES_PATH)


# In[5]:


if not os.path.exists(IMAGES_PATH):
    if os.name == 'nt':
         get_ipython().system('mkdir {IMAGES_PATH}')
for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        get_ipython().system('mkdir {path}')


# # 4. Capture Images

# In[6]:


capPort = 0
z = 0

def output():
    
    while True:
        ret, displayFrame = cap.read()

        cv2.imshow('frame',displayFrame)
        if z == 1:
            print('captured')
            cv2.putText(displayFrame, 'Captured', (640, 360), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 255, 0), 2)
            time.sleep(1)
        else:
            continue
        if cv2.waitKey(1) == ord('q'):
            print('q pressed, breaking')
            break
        else:
            print('. \n')

    cap.release()
    cv2.destroyAllWindows()
    
        


def __capture__():  
    global cap, z
    read, pictureFrame = cap.read()
    i = 0
    y = 0
    while i <= number_imgs and y<= (len(labels)-1):
        # print(f'Collecting images for {labels[y]}')
        if keyboard.is_pressed('c'):
                z = 1
                print(f'Collecting image {i} at labels {labels[y]}')

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
    
    cap = cv2.VideoCapture(capPort)
    if not cap.isOpened():
        raise Exception(f'cap -- check port // port {capPort} is not available')
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    th = threading.Thread(target= output)
    th1 = threading.Thread(target= __capture__)
    
    th.start()
    th1.start()
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




