import cv2
imageData=cv2.imread("image_1.jpg")
contrast=150
f=(259*(contrast+255))/(255*(259-contrast))
for r in range(imageData.shape[0]):
    for c in range(imageData.shape[1]):
        rgb=imageData[r][c]
        red=rgb[2]
        green=rgb[1]
        blue=rgb[0]
        newRed=(f*(red-128))+128
        newGreen=(f*(green-128))+128
        newBlue=(f*(blue-128))+128
        if newRed>255: newRed=255
        if newRed<0: newRed=0
        if newGreen>255: newGreen=255
        if newGreen<0: newGreen=0
        if newBlue>255: newBlue=255
        if newBlue<0: newBlue=0
        imageData[r][c]=(newRed,newGreen,newBlue)
cv2.imwrite("tmpFile.jpg",imageData)