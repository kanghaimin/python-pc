import tkinter
from PIL import Image
from tkinter import filedialog
import os

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        val = "%s" % tempdir
    return val

folder = search_for_file_path ()
folder_content = os.listdir(folder)
canvas = Image.new('RGB', (1010,1510), "white")

for i in range(12):
    tb = Image.open(folder+"\\"+folder_content[i])
    name = i+1
    if i >= 6:
        tb1 = tb.resize((279, 370), Image.ANTIALIAS)        
        new = Image.new('RGB', (370, 279), "white")
        mask = Image.new('L', tb1.size, 255)
        front = tb1.rotate(90, expand=True)
        mask = mask.rotate(90, expand=True)
        new.paste(front, (0,0), mask)
    else:
        new = tb.resize((279, 370), Image.ANTIALIAS)

#    new.save("temp\\"+str(name)+".png","PNG")
    new.save("temp\\"+str(name)+".jpg","JPEG", quality=100)

im1 = Image.open("temp\\1.jpg")
im2 = Image.open("temp\\2.jpg")
im3 = Image.open("temp\\3.jpg")
im4 = Image.open("temp\\4.jpg")
im5 = Image.open("temp\\5.jpg")
im6 = Image.open("temp\\6.jpg")
im7 = Image.open("temp\\7.jpg")
im8 = Image.open("temp\\8.jpg")
im9 = Image.open("temp\\9.jpg")
im10 = Image.open("temp\\10.jpg")
im11 = Image.open("temp\\11.jpg")
im12 = Image.open("temp\\12.jpg")
canvas.paste(im1, (16,17))
canvas.paste(im2, (317,17))
canvas.paste(im3, (16,413))
canvas.paste(im4, (317,413))
canvas.paste(im5, (16,806))
canvas.paste(im6, (317,806))
canvas.paste(im7, (619,18))
canvas.paste(im8, (619,317))
canvas.paste(im9, (619,616))
canvas.paste(im10, (619,915))
canvas.paste(im11, (619,1214))
canvas.paste(im12, (225,1214))
#canvas.save('A.png', "PNG")
canvas.save('ImageResult\\PythonDrawing1.jpg', "JPEG", quality=100, dpi=(300, 300))
print ("Selesai")
