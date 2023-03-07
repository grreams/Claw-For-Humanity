import cv2
import numpy as np
import math
import struct
import serial
import serial.tools.list_ports





                        # camera work
# global variables for contour ***DO NOT CHANGE***
resolution = 1280,720
actual_purplebox = None
actual_purplebox = None
frontCamPort = 0
topCamPort = 1
cameraAngle = 130
frontVid = None
topVid = None



def __initializeCam__():
    global frontCamPort
    global topCamPort
    global frontVid
    global topVid
    global centerXY
    global resolution

    #catch Camera
    frontVid = cv2.VideoCapture(frontCamPort)
    topVid = cv2.VideoCapture(topCamPort)
    if frontVid.isOpened() and topVid.isOpened():
        print("[LOG] " + f'front vid // selected port is "{frontCamPort}"')
        print("[LOG] " + f'top vid // selected port is "{topCamPort}"')
        
    
    # set camera resolution
    # 640 * 380 or 1280 * 720
    frontVid.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    frontVid.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    topVid.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    topVid.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # camera size
    resolution = (frontVid.get(3),frontVid.get(4))
    
    # find center // x 590, x+w 690, y 410, y+h 310 (width and height is 50 pixels. Therefore, add and subtract 50)
    centerXY = resolution[0]/2-50, resolution[1]/2+50, 50, 50
    # calculated values
    # center x y x+w y+h
    # 590, 410, 690, 310 








                        # com work

# global variables for serial com
serialComPort = 3
serialInst = None # dont touch this

def __startPort__():
    print('entered startport')
    global serialComPort
    global serialInst

    serialInst = serial.Serial()
    serialInst.port = "/dev/ttyTHS1"
    serialInst.open()
    if not serialInst.is_open:
        print('no serial com detected. change port')
        return
    else:
        pass
    print('finished startport without problem')



def sender(speed, desiredAngle, whetherinRange):
    array = speed + desiredAngle + whetherinRange
    print(array)
    global serialInst
    packed = struct.pack('>' + 'i'*len(array), *array)
    serialInst.write(packed)








                        # detection work

# global variables for detections
centerPurple = None
centerGreen = None
centerYellow = None
purple1 = (0,0,0,0)
green1 = (0,0,0,0)
yellow1 = (0,0,0,0)
centerXY = (0,0,0,0)
desiredDistance = 300
greenerReturn = None
yellowerReturn = None
purplerReturn = None

# colour range
purple_lower_colour = np.array([123,150,100])
purple_upper_colour = np.array([139,255,255])

yellow_lower_colour = np.array([15,150,100])
yellow_upper_colour = np.array([30,255,255])

green_lower_colour = np.array([33,50,50])
green_upper_colour = np.array([40,255,255])

# actual sizes of things in mm
actual_purplebox = 243,243
actual_yellowcone = 210,330
actual_greenlight = 100,100



# xywh
def check_location(centerval, colour): 
    x1, y1, w1, h1 = centerXY
    x2, y2, w2, h2 = centerval

    if x1 <= x2 and x2 + w2 <= x1 + w1 and y1 <= y2 and y2 + h2 <= y1 + h1:
        print(f'in Range, colour is {colour}')
        return '69'
    else:
        print(f'not in Range, colour is {colour}')
        return '-69'



def _detect_(camera):  
    # video input
    read, standard = camera.read()

    bottomHsv = cv2.cvtColor(standard, cv2.COLOR_BGR2HSV)

    # make mask
    bottom_purple_mask = cv2.inRange(bottomHsv, purple_lower_colour, purple_upper_colour)
    bottom_yellow_mask = cv2.inRange(bottomHsv, yellow_lower_colour, yellow_upper_colour)
    bottom_green_mask = cv2.inRange(bottomHsv, green_lower_colour, green_upper_colour)

    # combine masks
    combined_mask = cv2.bitwise_or(bottom_purple_mask,cv2.bitwise_or(bottom_yellow_mask,bottom_green_mask))

    # create result
    result = cv2.bitwise_and(standard, standard, mask= combined_mask)

    # create videos dictionary
    videos = [result, combined_mask]    

    # draw boxes
    contours1, _1 = cv2.findContours(bottom_purple_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours1:
        global purple1
        global purplerReturn
        purple1 = cv2.boundingRect(contour)
        
        if purple1[2]>90 and purple1[3]>90:          
            centerPurple = (2*purple1[0]+purple1[2])//2, (2*purple1[1]+purple1[3])//2
            purpler1 = check_location(purple1, 'purple')
            purpler2 = detector(purple1,actual_purplebox)
            # purplerReturn.extend(purpler2)
            # purplerReturn.extend(purpler1)

            for purpleVid in videos:
                cv2.rectangle(purpleVid,(purple1[0],purple1[1]),(purple1[0]+purple1[2],purple1[1]+purple1[3]),(172,0,179),2)
                cv2.circle(purpleVid, centerPurple, 1, (255,0,0) ,thickness=3)
                
    contours2, _2 = cv2.findContours(bottom_yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours2:
        global yellow1
        global yellowerReturn
        yellow1 = cv2.boundingRect(contour)
        if yellow1[2]>90 and yellow1[3]>90:
            centerYellow = (2*yellow1[0]+yellow1[2])//2, (2*yellow1[1]+yellow1[3])//2
            yellower1 = check_location(yellow1, 'yellow')
            yellower2 = detector(yellow1,actual_yellowcone)
            # yellowerReturn.extend(yellower1)
            # yellowerReturn.extend(yellower1)
            
            for yellowVid in videos:
                cv2.rectangle(yellowVid,(yellow1[0],yellow1[1]),(yellow1[0]+yellow1[2],yellow1[1] + yellow1[3]),(0,255,255),2)
                cv2.circle(yellowVid, centerYellow, 1, (255,0,0) ,thickness=3)
        

    contours3, _3 = cv2.findContours(bottom_green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours3:
        global green1
        global greenerReturn
        green1 = cv2.boundingRect(contour)
        if green1[2]>90 and green1[3]>90:
            centerGreen = (2*green1[0]+green1[2])//2, (2*green1[1]+green1[3])//2
            greener1 = check_location(green1, 'green')
            xg,yg = detector(green1,actual_greenlight)
            
            sender(xg, yg,greener1)

            for greenVid in videos:
                cv2.rectangle(greenVid, (green1[0], green1[1]), (green1[0] + green1[2], green1[1] + green1[3]), (0, 255, 0), 2)
                cv2.circle(greenVid, centerGreen, 1, (255, 0, 0), thickness=3)
        else:
            greenerReturn = None

    # make a box at center
    for boxes in videos:
        cv2.rectangle(boxes,(590,410), (690,310), (0,0,255), 2) 
    
    # center pixel hsv value
    centerBottomHsv = bottomHsv[360,640]
    colour = centerBottomHsv[0]
    # make a circle
    cv2.circle(result, (360,640) , 5, (255,0,0), 3)
    #print(colour)

    # show video // result displays with colour // combined mask displays white and black
    cv2.imshow('result', result)
    cv2.imshow('combined mask', combined_mask)



def detector(array,actual):
    x,y,w,h = array
    actualWidth, actualHeight = actual    
    # speed, distance
    distanceX = (4.4 * (actualWidth))/(w*0.002953125)
    distanceY = (4.4 * (actualHeight))/(h*0.003912364)
    distance = (distanceX + distanceY) /2
    deltaDistance = distance - desiredDistance
    speed = 2*(1/(1+math.e**(-deltaDistance+desiredDistance))-0.5)
    print(f'speed {speed}')

    # right left
    if x < resolution[0] / 2:
        # left
        x +=640
        if x != 640:
            x = x%640
        else:
            pass
        print(x)
        theta = math.degrees(math.atan((x * 0.002953125)/4.4))
        k = math.degrees(math.atan(0.002953125*(x+w)/4.4))
        moveAngle = (k-theta)/2 + theta
        moveAngle = 360 - moveAngle

    elif x > resolution[0] / 2:
        # left 
        theta = math.degrees(math.atan((x * 0.002953125)/4.4))
        k = math.degrees(math.atan((0.002953125*(x+w))/4.4))
        moveAngle = (k-theta)/2 + theta
        print(f'k is {k} theta is {theta}')
    else:
        moveAngle = 0

    
    print(f'moveAngle {moveAngle}')

    array1 = moveAngle, speed
    return array1









                        # initialize / work
def __initialize__():
    # print('cam port')
    # __startPort__()
    # print('startport done')
       
    
    print('initialize')
    __initializeCam__()
    print('initialize camera done')
    
    
    print('start working')
    __work__()
    print('work done')

    #release camera
    frontVid.release()
    topVid.release()

    #destroy window
    cv2.destroyAllWindows()



def __work__():
    i = 0
    global frontVid
    global topVid
    global purple_upper_colour
    global purple_lower_colour
    global yellow_upper_colour
    global yellow_lower_colour
    global green_upper_colour
    global green_lower_colour
    global purple1
    global green1
    global yellow1
    global greenerReturn
    
    print('about to enter while loop')
    while(True):
        if(frontVid.isOpened()):
            _detect_(frontVid)
        if(topVid.isOpened()):
            _detect_(topVid)
       # print(greenerReturn)
        #sender(purplerReturn)
        #sender(yellowerReturn)
        

        # stop loop when q is pressed
        if cv2.waitKey(1) == ord('q'):
            print(f'loop happened {i} times')
            break
        i+=1






# start from here
__initialize__()