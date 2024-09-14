from PIL import Image
import os
from imgprocess import imgpre
#导入所需module及自定义函数

#检测文件工作路径
workingdir = os.path.abspath('.')
#载入图片名
img1name ='Volvosuv'
img2name ='volkswagan'
img3name ='suv2'
img4name ='bus1'
imgfolder_name ='img'
savefolder_name ="img-processed"
#生成图片读取及保存的绝对路径
imgfolder_abspath = os.path.join(workingdir,imgfolder_name)
savefolder_abspath = os.path.join(workingdir,savefolder_name)


#进行图像处理
imgpre(img1name,imgfolder_abspath,savefolder_abspath)
imgpre(img2name,imgfolder_abspath,savefolder_abspath)
imgpre(img3name,imgfolder_abspath,savefolder_abspath)
imgpre(img4name,imgfolder_abspath,savefolder_abspath)

