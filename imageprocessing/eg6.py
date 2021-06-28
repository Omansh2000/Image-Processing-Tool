import cv2
imageData=cv2.imread("image_1.jpg")
cropFrom=(100,200)
cropSize=(40000,300000)
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
r=r1
while r<=r2:
    imageData[r][c1]=(0,0,255)
    imageData[r][c2]=(0,0,255)
    r+=1
c=c1
while c<=c2:
    imageData[r1][c]=(0,0,255)
    imageData[r2][c]=(0,0,255)
    c+=1
cv2.imwrite("tmp.jpg",imageData)
print("Done")