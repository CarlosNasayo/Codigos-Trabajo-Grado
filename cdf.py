from fnmatch import fnmatch
import cv2 as cv
import netCDF4 as nc
import numpy as np
from os import system
import os
import os,glob 
def contrast(image,minvalue=None,maxvalue=None,method=1):
    I=[]
    I = cv.split(image)
    image = I[0]
    if(method == 1):
        image_tf = convert_8u(image,minvalue,maxvalue)
        return image_tf
    elif(method == 2):
        image_conv = convert_8u(image,minvalue,maxvalue)
        hist,bins = np.histogram(image_conv.flatten(),256,[0,256])
        cdf = hist.cumsum()
        cdf_m = np.ma.masked_equal(cdf,0)
        cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
        cdf = np.ma.filled(cdf_m,0).astype('uint8')
        image_tf = cdf[image_conv]
        return image_tf
    elif(method == 3):
        image_tf = convert_8u(image,minvalue,maxvalue)
        image_tf = cv.equalizeHist(image_tf)
        return image_tf
    elif(method == 4):
        image_tf = convert_8u(image,minvalue,maxvalue)
        clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        image_tf = clahe.apply(image_tf)
        return image_tf
    else:
        print("invalid option")
        return -1

def convert_8u(image,minvalue,maxvalue):
    if(minvalue is None and maxvalue is None):
        minval = image.min()
        maxval = image.max()
    elif(minvalue is None):
        minval = image.min()
        maxval = maxvalue
    elif(maxvalue is None):
        maxval = image.max()
        minval = minvalue
    else:
        maxval = maxvalue
        minval = minvalue
    image = image - minval
    image = image / maxval * 255
    image = np.uint8(image)
    return image

fn = 'C:\\ProyectoDeGrado\\ImaganesMapeadas\\2002mapped'       #mascara de año
os.chdir(fn)
os.getcwd() 
lista=glob.glob("*.nc")
print(len(lista))
flag=0
cont=None
for imagen in lista:
    path=fn+'\\'+imagen
    #print(path)
    ds = nc.Dataset(path)
    #print(ds)

    #print(ds['chlor_a_count'])
    clo  = ds['chlor_a_count'][:]
    if(flag==0):
        cont= clo#[0:4,0:4];
        flag=1
    else:
        #clo= ((clo[0:4,0:4]));
        cont= cont +clo
print(np.amin(clo))
print(np.amax(clo))
print(cont)
print(cont.shape)
#clo8u= contrast(clo,minvalue=None,maxvalue=None,method=1)

    
#cv.imshow('img',clo8u)
#cv.waitKey(0)


#ESTO FUNCIONABA, SI SE JODE TODO VOLVER AQUI
""" fn = 'source/01_mapped_A2002186181500.L2_LAC_OC.x.nc'
ds = nc.Dataset(fn)
print(ds)

print(ds['chlor_a_count'])
clo  = ds['chlor_a_count'][:]
print(clo)
print(clo.shape) """
clo8u= contrast(cont,minvalue=None,maxvalue=None,method=1)

    
cv.imshow('img',clo8u)
cv.waitKey(0)
