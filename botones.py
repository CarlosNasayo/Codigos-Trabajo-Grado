from os import system
import os
from fileinput import filename
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
import re


path_to_mappedImageFolder=""
dir_seadas=""
path_to_rawdatafolder=""
path_to_xmlMosaicFile=""
path_to_logFile=""

listacarpetas=""
def browse_button():
    
    # Allow user to select a directory and store it in global var
    # called folder_path
    
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    global path_to_rawdatafolder
    path_to_rawdatafolder=filename;
    path_to_rawdatafolder= path_to_rawdatafolder.replace("/","\\")
    print(path_to_rawdatafolder)
   
    
def browse_button_two():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    global path_to_mappedImageFolder
    folder_path.set(filename)
    #print(filename)
    path_to_mappedImageFolder= filename;
    path_to_mappedImageFolder= path_to_mappedImageFolder.replace("/","\\")
    print(path_to_mappedImageFolder)

def browse_button_three():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    global dir_seadas
    dir_seadas= filename;
    dir_seadas= dir_seadas.replace("/","\\")
    print(dir_seadas)
        
   
   
    
def browseFiles():
    filename2 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    folder_path.set(filename2)
    global path_to_xmlMosaicFile
    path_to_xmlMosaicFile= filename2
    path_to_xmlMosaicFile = path_to_xmlMosaicFile.replace("/","\\")
    print(path_to_xmlMosaicFile)
    
def browseFiles_two():
    filename3 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    folder_path.set(filename3)
    global path_to_logFile
    path_to_logFile= filename3
    path_to_logFile = path_to_logFile.replace("/","\\")
    print(path_to_logFile)
    
def correr():
    global path_to_rawdatafolder
    global path_to_mappedImageFolder
    global path_to_xmlMosaicFile
    global dir_seadas
    global path_to_logFile
    #print("prueba" +path_to_rawdatafolder)
    datos=os.listdir(path_to_rawdatafolder)
    a=[]
    datos_vf=[]

    for fichero in datos:
        if os.path.isfile(os.path.join(path_to_rawdatafolder, fichero)) and fichero.endswith('.nc'):
            datos_vf.append(fichero)

    os.chdir(dir_seadas)

    for nombre in range(datos_vf.__len__()):
        b = 'gpt.bat -e '+path_to_xmlMosaicFile+' -Ssource='+path_to_rawdatafolder+'\\'+datos_vf[nombre]+' -t '+path_to_mappedImageFolder+'\\0'+str(nombre)+'_mapped_'+datos_vf[nombre]
        os.system(b)
        print(b)
        a.insert(nombre,b)
    
    with open(path_to_logFile, 'w') as output:
        for row in a:
            output.write(str(row) + '\n')
def salir():
    root.destroy()
root = Tk()

root.title("Corregistro")
root.resizable(1,1)

folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)

label=Label(root,text="Imagenes a corregistrar" )
label.grid(row=1,column=0,padx=5,pady=5)
button2 = Button(text="Buscar carpeta", command=browse_button)
button2.grid(row=1, column=1,padx=5,pady=5)
#print(filename)
label2=Label(root,text="Archivo mosaico XML" )
label2.grid(row=2,column=0,padx=5,pady=5)
button3 = Button(text="Buscar archivo", command=browseFiles)
button3.grid(row=2, column=1,padx=5,pady=5)

label3=Label(root,text="carpeta a guardar las imagenes" )
label3.grid(row=3,column=0,padx=5,pady=5)
button4 = Button(text="Buscar carpeta", command=browse_button_two)
button4.grid(row=3, column=1,padx=5,pady=5)

label4=Label(root,text="Directorio Seadas" )
label4.grid(row=4,column=0,padx=5,pady=5)
button5 = Button(text="Buscar carpeta", command=browse_button_three)
button5.grid(row=4, column=1,padx=5,pady=5)

label5=Label(root,text="Archivo texto" )
label5.grid(row=5,column=0,padx=5,pady=5)
button6 = Button(text="Buscar archivo", command=browseFiles_two)
button6.grid(row=5, column=1,padx=5,pady=5)

myButton = Button(root, text="EJECUTE", command=correr)

myButton.grid(row=6, column=0, sticky="w", padx=100, pady=5 )

myButton2 = Button(root, text="Cerrar programa", command=salir)

myButton2.grid(row=7, column=0, sticky="w", padx=100, pady=5 )


root.mainloop()