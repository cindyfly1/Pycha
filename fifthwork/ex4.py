import cv2
import numpy as np

im = cv2.imread("d:\\lena.tiff")
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) #creat gray picture
# cv2.imshow("grayImage", GrayImage)
# cv2.waitKey(0)
b=np.array(gray.shape)
b*=2 # 2 bigger
tmp=np.zeros(tuple(b))
#the 3 out circle
tmp[::2,::2]=gray[:,:]
tmp[::2,1023]=gray[:,511]
tmp[1023,::2]=gray[511,:]
for i in range(1,1022,2):
    j = 0,1,2,3,4,1020,1021,1022,1021,1023
    tmp[i,j]=tmp[i-1,j]/2+tmp[i+1,j]/2
for j in range(1,1022,2):
    i = 0,1,2,3,4,1020,1021,1022,1021,1023
    tmp[i,j]=tmp[i,j-1]/2+tmp[i,j+1]/2

#in the line
w=2
for a in range(3,511):
    q=0
    w=w+2
    for b in range(0,506):
        f0=gray[a,b]
        f1=gray[a,b+1]
        f2=gray[a,b+2]
        f3=gray[a,b+3]
        f4=gray[a,b+4]
        f5=gray[a,b+5]
        f11=(f0/4+f1/4+f2/4+f3/4)
        f22=(f1/4+f2/4+f3/4+f4/4)
        f33=(f2/4+f3/4+f4/4+f5/4)
        s1=(f0**2+f1**2)-4*f11
        s2=(f1**2+f4**2)-4*f22
        s3=(f4**2+f5**2)-4*f33
        s=min(s1,s2,s3)
        x=2+w
        if s==s1:
            now=(-1/6*x**3+x**2-11/6*x+1)*f0+(1/2*x**3-5/2*x**2+3*x)*f1+(-1/2*x**3+2*x**2-3/2*x)*f2+(1/6*x**3-1/2*x**2+1/3*x)*f3
        if s==s2:
            now=(-1/6*x**3+x**2-11/6*x+1)*f1+(1/2*x**3-5/2*x**2+3*x)*f2+(-1/2*x**3+2*x**2-3/2*x)*f3+(1/6*x**3-1/2*x**2+1/3*x)*f4
        if s==s3:
            now=(-1/6*x**3+x**2-11/6*x+1)*f2+(1/2*x**3-5/2*x**2+3*x)*f3+(-1/2*x**3+2*x**2-3/2*x)*f4+(1/6*x**3-1/2*x**2+1/3*x)*f5
        #tmp[6:1018:2,5:1019:2]=now
        tmp[2+w,5+q]=now
        q=q+2

# in the column
w=2
for b in range(3,511):
    q=0
    w=w+2
    for a in range(0,506):
        f0=gray[a,b]
        f1=gray[a+1,b]
        f2=gray[a+2,b]
        f3=gray[a+3,b]
        f4=gray[a+4,b]
        f5=gray[a+5,b]
        f11=(f0/4+f1/4+f2/4+f3/4)
        f22=(f1/4+f2/4+f3/4+f4/4)
        f33=(f2/4+f3/4+f4/4+f5/4)
        s1=(f0**2+f1**2)-4*f11
        s2=(f1**2+f4**2)-4*f22
        s3=(f4**2+f5**2)-4*f33
        s=min(s1,s2,s3)
        x=b
        if s==s1:
            now=(-1/6*x**3+x**2-11/6*x+1)*f0+(1/2*x**3-5/2*x**2+3*x)*f1+(-1/2*x**3+2*x**2-3/2*x)*f2+(1/6*x**3-1/2*x**2+1/3*x)*f3
        if s==s2:
            now=(-1/6*x**3+x**2-11/6*x+1)*f1+(1/2*x**3-5/2*x**2+3*x)*f2+(-1/2*x**3+2*x**2-3/2*x)*f3+(1/6*x**3-1/2*x**2+1/3*x)*f4
        if s==s3:
            now=(-1/6*x**3+x**2-11/6*x+1)*f2+(1/2*x**3-5/2*x**2+3*x)*f3+(-1/2*x**3+2*x**2-3/2*x)*f4+(1/6*x**3-1/2*x**2+1/3*x)*f5
        #tmp[6:1018:2,5:1019:2]=now
        tmp[5+q,2+w]=now
        q=q+2

#the diagonal
tmp[5:1019:2,5:1019:2]=tmp[5:1019:2,4:1018:2]/2+tmp[5:1019:2,6:1020:2]/2

print(tmp.shape)
print(tmp)

res=cv2.resize(tmp,(512,512),interpolation=cv2.INTER_CUBIC)
cv2.imshow('iker',res)
cv2.imshow('image',tmp)

# cv2.imshow("grayImage", tmp)
cv2.waitKey(0)
