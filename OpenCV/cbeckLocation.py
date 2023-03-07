
def check_location(desired_location, location_box):
    x1, y1, w1, h1 = desired_location
    x2, y2, w2, h2 = location_box


    if x1 <= x2 and x2 + w2 <= x1 + w1 and y1 <= y2 and y2 + h2 <= y1 + h1:
        return '69'
    else:
        return '-69'
