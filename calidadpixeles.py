from os import system
import os
from fileinput import filename
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
import re
import cv2 as cv
import numpy as np
from osgeo import gdal, osr
import netCDF4 as nc
import os,glob 
path_to_images=""
def browse_button():
    
    # Allow user to select a directory and store it in global var
    # called folder_path
    
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    global path_to_images
    path_to_images=filename;
    path_to_images= path_to_images.replace("/","\\")
    print(path_to_images)

def verificar():
    global path_to_images
    os.chdir(path_to_images)
    os.getcwd() 
    a=[]
    path_to_logFile='C:\\ProyectoDeGrado\\prueba\\log.txt'
    lista=glob.glob("*.nc")
    print(len(lista))
    for imagen in lista:
        print(imagen)
        path=path_to_images+'\\'+imagen
        print(path)
        dSet= nc.Dataset(path)
        print(dSet)
        a.append(path)
    with open(path_to_logFile, 'w') as output:
        for row in a:
            output.write(' Cargada correctamente '+str(row) + '\n')
def salir():
    root.destroy()
root = Tk()

root.title("Verificación")
root.resizable(1,1)

folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)

label=Label(root,text="Ruta imagenes" )
label.grid(row=1,column=0,padx=5,pady=5)
button2 = Button(text="Buscar carpeta", command=browse_button)
button2.grid(row=1, column=1,padx=5,pady=5)

myButton = Button(root, text="EJECUTE", command=verificar)

myButton.grid(row=6, column=0, sticky="w", padx=100, pady=5 )

myButton2 = Button(root, text="Cerrar programa", command=salir)

myButton2.grid(row=7, column=0, sticky="w", padx=100, pady=5 )
root.mainloop()