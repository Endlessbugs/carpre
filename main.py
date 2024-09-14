import cv2
from PIL import Image
import os
from imgprocess import imgpre

workingdir = os.path.abspath('.')
img1name ='Volvosuv'
img2name ='volkswagan'
img3name ='suv2'
img4name ='bus1'
imgfolder_name ='img'
savefolder_name ="img-processed"
imgfolder_abspath = os.path.join(workingdir,imgfolder_name)
savefolder_abspath = os.path.join(workingdir,savefolder_name)



imgpre(img1name,imgfolder_abspath,savefolder_abspath)
imgpre(img2name,imgfolder_abspath,savefolder_abspath)
imgpre(img3name,imgfolder_abspath,savefolder_abspath)
imgpre(img4name,imgfolder_abspath,savefolder_abspath)

