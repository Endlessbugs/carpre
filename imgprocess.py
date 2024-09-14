import cv2
from PIL import Image
from PIL import ImageOps as imgOps
import os
import numpy as npy
import matplotlib.pyplot as plt


def imgprocess(imgobj):
    npy_img_inv = npy.array(imgobj)
    img_bgr = cv2.cvtColor(npy_img_inv, cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)
    ret, img_binary = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
    img_contours,img_hierarchy = cv2.findContours(img_binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    img_cont=cv2.drawContours(img_bgr, img_contours, -1, (0,0,255), thickness=1,lineType=cv2.LINE_AA,hierarchy= img_hierarchy )
    img_cont_PIL = Image.fromarray(cv2.cvtColor(img_cont,cv2.COLOR_BGR2RGB))
    img_gray_PIL = Image.fromarray(img_gray)
    img_bin_PIL = Image.fromarray(img_binary)
    #cv2.imshow("img1",img_binary)
    #key = cv2.waitKey(0) 
    return img_cont_PIL,img_gray_PIL,img_bin_PIL

def imgshow(fig_name,imgobj):
    
    plt.figure(fig_name)
    plt.axis('off') 
    plt.imshow(imgobj)
    plt.show()


def imgsave(imgobj:Image.Image,imgname='img',imgformat='tiff',savefolder_path='C:/Users/Default/Pictures'):

        
    dot='.'
    img_savepath=os.path.join(savefolder_path,imgname+dot+imgformat)
    imgobj.save(img_savepath,imgformat)
    

def imgpre(imgname,imgfolder_abspath,savefolder_abspath):
    
    aftprocess='-processed'
    png_format='png'
    tiff_format='tiff'
    dot='.'
    img_path=os.path.join(imgfolder_abspath,imgname+dot+png_format)
    #print(img_path)

    img = Image.open(img_path)
    img_cont,img_gray,img_bin=imgprocess(img)
    #img_inv = imgOps.invert(img)
    img_bin.show()
    img_cont.show()
    imgsave(img_cont,imgname,'tiff',savefolder_abspath)
    imgsave(img_bin,imgname,'tiff',savefolder_abspath)
    img.close
    return img_cont,img_gray,img_bin
    
