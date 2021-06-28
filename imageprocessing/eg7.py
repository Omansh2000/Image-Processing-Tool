import numpy
import cv2
imageData=cv2.imread("image_1.jpg")
cropFrom=(100,200)
cropSize=(900,900)
c1=cropFrom[0]
r1=cropFrom[1]
c2=cropSize[0]-1
r2=cropSize[1]-1
if r2>=imageData.shape[0]: r2=imageData.shape[0]-1
if c2>=imageData.shape[1]: c2=imageData.shape[1]-1
print("Actual size : ",imageData.shape)
print(cropSize)
cropSize=(c2-c1+1,r2-r1+1)
print(cropSize)
newImage=numpy.zeros((cropSize[1],cropSize[0],3))
rr=0
r=r1
while r<=r2:
    cc=0
    c=c1
    while c<=c2:
        newImage[rr][cc]=imageData[r][c]
        cc+=1
        c+=1
    rr+=1
    r+=1
cv2.imwrite("tmp.jpg",newImage)
print("Done")