import cv2
imageData=cv2.imread("image_1.jpg")
for r in range(imageData.shape[0]):
    for c in range(imageData.shape[1]):
        rgb=imageData[r][c]
        red=(int(rgb[0])*0.11)
        green=(int(rgb[1])*.59)
        blue=(int(rgb[2])*.3)
        total=red+green+blue
        imageData[r][c]=(total,total,total)
cv2.imwrite("tmpFile.jpg",imageData)