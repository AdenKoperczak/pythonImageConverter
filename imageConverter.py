from PIL import Image
import os, fnmatch
con = True
while con:
    typearray = ["bmp","jpeg","jpg","png","gif","dib","jpe","jfif","tif","tiff","ico","eps","icns","im","msp","pcx","ppm","sgi","xbm"]
    path = input("File: ")
    if path.lower() == "end":
        con = False
    else:
        types = input("Input Type: ")
        if types == "end":
            con = False
        elif types not in typearray:
            print('Type must be one of: '+str(typearray))
        else:
            typeo = input("Output Type: ")
            if typeo == "end":
                con = False
            elif typeo not in typearray:
                print('Type must be one of: '+str(typearray))
            else:
                if "." in path:
                    img = Image.open(path)
                    new_img = img.rotate(360)
                    new_img.save(path[:-len(types)]+typeo, typeo)
                    print("Added the file "+path[:-len(types)]+typeo)
                else:
                    for file in os.listdir(path):
                        if fnmatch.fnmatch(file, "*."+types):
                            print(file)
                            img = Image.open(path+"/"+file)
                            new_img = img.rotate(360)
                            new_img.save(path+"/"+file[:-len(types)]+typeo, typeo)
                print("Done")
