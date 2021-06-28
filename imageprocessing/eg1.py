import cv2
imageData=cv2.imread("image_1.jpg")
print(imageData)
print(type(imageData))
print(imageData.shape)
print(imageData[0][0])