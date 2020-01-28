import tkinter
from PIL import Image
from tkinter import filedialog
import os
import time

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Silakan pilih foldernya')
    if len(tempdir) > 0:
        val = "%s" % tempdir
    return val

pos = [(16,17),(317,17),(16,413),(317,413),(16,806),(317,806),(619,18),(619,317),(619,616),(619,915),(619,1214),(225,1214)]
folderu = search_for_file_path ()
#folder = "E:\\python\\a\\"
for fu in os.listdir(folderu) :
    folder = folderu+'\\'+fu
    folder_content = os.listdir(folder)
    canvas = Image.new('RGB', (1010,1510), "white")

    if(len(folder_content)%12 == 0) :
        for n in range(int(len(folder_content)/12)) :
            for i in range(12*n,(12*n)+12):
                tb = Image.open(folder+"\\"+folder_content[i])
                name = i+1
                if i >= (12*n)+6 and i <= (12*n)+12:
                    tb1 = tb.resize((279, 370), Image.ANTIALIAS)        
                    new = Image.new('RGB', (370, 279), "white")
                    mask = Image.new('L', tb1.size, 255)
                    front = tb1.rotate(90, expand=True)
                    mask = mask.rotate(90, expand=True)
                    new.paste(front, (0,0), mask)
                else:
                    new = tb.resize((279, 370), Image.ANTIALIAS)

                new.save("..\\temp\\"+str(name).zfill(2)+".jpg","JPEG", quality=100)

            no = 0
            for i in os.listdir("..\\temp\\") :
                if no > 11:
                    no = 0
                im = Image.open("..\\temp\\"+i)
                canvas.paste(im, pos[no])
                no+=1

            canvas.save('..\\TempRes\\'+os.path.basename(folderu)+'-'+str(fu)+str(n+1)+' 1X.jpg', "JPEG", quality=100, dpi=(300, 300))
            print ("Selesai")
            time.sleep(3)
