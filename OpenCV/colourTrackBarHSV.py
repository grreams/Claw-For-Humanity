# import required libraries
import cv2
import numpy as np

def nothing(x):
   pass
   
# Create a black image, a window
img = np.zeros((300,650,3), np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
window_name = 'HSV Color Palette'
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

# create trackbars for color change
cv2.createTrackbar('H',window_name,0,255,nothing)
cv2.createTrackbar('S',window_name,0,255,nothing)
cv2.createTrackbar('V',window_name,0,255,nothing)
while(True):
   cv2.imshow(window_name,img)
   key = cv2.waitKey(1) & 0xFF
   if key == ord('q'):
      break
      
   # get current positions of four trackbars
   h = cv2.getTrackbarPos('H',window_name)
   s = cv2.getTrackbarPos('S',window_name)
   v = cv2.getTrackbarPos('V',window_name)
   img[:] = [h,s,v]
   img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
cv2.destroyAllWindows()