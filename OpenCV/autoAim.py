import math

# all in mm
resolution = 1280,720
yellow1 = (0,0,0,0)
purple1 = (0,0,0,0)
green1 = (0,0,0,0)
x = 1280
y = 720
desiredDistance = 100

actual_purplebox = 243, 243
actual_greenReflection = 21, 22

# # inRange means that the boxes are in Range, they are trustworthy that they are boxes

# if inRange



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
        # right
        theta = math.degrees(math.atan((x * 0.002953125)/4.4))
        k = math.degrees(math.atan((0.002953125*(x+w))/4.4))
        moveAngle = (k-theta)/2 + theta
        print(f'k is {k} theta is {theta}')
    else:
        moveAngle = 0
    print(f'moveAngle {moveAngle}')

location = 0,0,100,100
actual1 = 247,247
detector(location,actual1)


# x,y,w,h = array
