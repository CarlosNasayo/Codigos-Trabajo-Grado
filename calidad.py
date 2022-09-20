
import cv2 as cv
import numpy as np
from osgeo import gdal, osr
import netCDF4 as nc



import os,glob 
ruta=r"C:\ProyectoDeGrado\prueba"
os.chdir(ruta)
os.getcwd()
a=[]
path_to_logFile='C:\\ProyectoDeGrado\\prueba\\log.txt'
lista=glob.glob("*.nc")
print(len(lista))
for imagen in lista:
    print(imagen)
    path=ruta+'\\'+imagen
    print(path)
    dSet= nc.Dataset(path)
    print(dSet)
    a.append(path)
with open(path_to_logFile, 'w') as output:
    for row in a:
        output.write(' Cargada correctamente '+str(row) + '\n')

