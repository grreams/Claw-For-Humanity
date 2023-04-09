import cv2
import numpy as np
def emptyFunction(x): #here x is the int value that trackbar returns
    return
img1 = np.zeros((512, 512, 3), np.uint8)
windowName = 'OpenCV BGR Color Palette'
cv2.namedWindow(windowName)
# BGR Palette in OpenCV
cv2.createTrackbar('B', windowName, 0, 255, emptyFunction)
cv2.createTrackbar('G', windowName, 0, 255, emptyFunction)
cv2.createTrackbar('R', windowName, 0, 255, emptyFunction)
while (True):
    blue = cv2.getTrackbarPos('B', windowName)
    green = cv2.getTrackbarPos('G', windowName)
    red = cv2.getTrackbarPos('R', windowName)
    img1[:] = [blue, green, red]
    cv2.imshow(windowName, img1)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()