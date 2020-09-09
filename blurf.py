import matplotlib.pyplot as plt 
import numpy as np

orig_img=plt.imread('filter.png')
orig_img_arr=np.array(orig_img)
print('Image shape is '+str(orig_img_arr.shape))
box_blur=np.array([
    [1/9,1/9,1/9],
    [1/9,1/9,1/9],
    [1/9,1/9,1/9]
])
sharpen=np.array([
[0,-1,0],
[-1,5,-1],
[0,-1,0]
])
gaussian_blur=np.array([[1,  4,  6,  4, 1],
                         [4, 16, 24, 16, 4],
                         [6, 24, 36, 24, 6],
                         [4, 16, 24, 16, 4],
                         [1,  4,  6,  4, 1]])/256
def filter(ker_mat):
    xk,yk = ker_mat.shape
    x,y,z = orig_img_arr.shape
    fil_img=np.zeros((x+ker_mat.shape[0]-1,y+ker_mat.shape[1]-1,z))
    fil_img[int(xk/2):int(xk/2)+x,int(yk/2):int(yk/2)+y,:]=orig_img_arr
    res=np.zeros_like(orig_img_arr)
    x1=int(xk/2)
    y1=int(yk/2)
    z1=0
    print(fil_img[x1-int(xk/2):x1-int(xk/2)+xk,y1-int(yk/2):y1-int(yk/2)+yk,z1])
    print(fil_img[x1-int(xk/2):x1-int(xk/2)+xk,y1-int(yk/2):y1-int(yk/2)+yk,])
    for x1 in range(int(xk/2),int(xk/2)+x):
        for y1 in range(int(yk/2),int(yk/2)+y):
            for z1 in range(z):
                res[x1-int(xk/2),y1-int(yk/2),z1]=(ker_mat*fil_img[x1-int(xk/2):x1-int(xk/2)+xk,y1-int(yk/2):y1-int(yk/2)+yk,z1]).sum()
    plt.imshow(res)
    plt.text(250,-5,"sharpen")
    plt.show()
filter(sharpen)