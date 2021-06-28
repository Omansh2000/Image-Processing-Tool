import cv2
imageData=cv2.imread("image_1.jpg")
#brightness=150
brightness=-150
for r in range(imageData.shape[0]):
    for c in range(imageData.shape[1]):
        rgb=imageData[r][c]
        red=rgb[2]
        green=rgb[1]
        blue=rgb[0]
        red+=brightness
        green+=brightness
        blue+=brightness
        if red>255: red=255
        if red<0: red=0
        if green>255: green=255
        if green<0: green=0
        if blue>255: blue=255
        if blue<0: blue=0
        imageData[r][c]=(blue,green,red)
cv2.imwrite("tmpFile.jpg",imageData)