# -*- coding: utf-8 -*-
#请学会读取一张图像，然后请将图像进行缩小（2倍，4倍，8倍等），或者进行放大（只要求2倍），改变后的图像请保存为JPEG文件
#Huang Weihao
#2018/3/29

import numpy as np
import matplotlib.pylab as plt

def plti(im, **kwargs):
    plt.imshow(im, interpolation="none", **kwargs)
    plt.savefig("lena_.jpg")#保存图片为lena_.jpg
    plt.show()# 弹窗显示图像


fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(15,5))
im = plt.imread("d:\\lena.tiff")# 加载当前文件夹中名为lena512color1.png的图片
for i,ax in zip(range(3),axs):
    im1=im[::2**(i+1),::2**(i+1),:]

    ax.imshow(im1)

b=np.array(im.shape)
b[0:2]*=2
tmp_im=np.zeros(tuple(b))
# tmp_im[::2,::2,:]=im[::,::,:]
# tmp_im[::2,1:-1:2,:]=im[::,:-1:,:]/2+im[::,1::,:]/2
# tmp_im[1:-1:2,::2,:]=im[:-1:,::,:]/2+im[1::,::,:]/2
# tmp_im[1:-1:2,1:-1:2,:]=im[:-1:,:-1:,:]/2+im[1::,1::,:]/2

# tmp_im[::2,::2,:]=im[::,::,:]
# tmp_im[::2,1:-1:2,:]=im[::,:-1:,:]/2+im[::,1::,:]/2
# tmp_im[1:-1:2,::2,:]=im[:-1:,::,:]/2+im[1::,::,:]/2
# tmp_im[1:-1:2,1:-1:2,:]=im[:-1:,:-1:,:]/2+im[1::,1::,:]/2

plti(tmp_im)
print(tmp_im.shape)