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
#folderu = "E:\\a smp37"
if(os.path.isdir(folderu+" Cetak") == 0):
    os.mkdir(folderu+" Cetak")
if(os.path.isdir(os.path.dirname(folderu)+"temp") == 0):
    os.mkdir(os.path.dirname(folderu)+"temp")
    
for fu in os.listdir(folderu) :
    folder = folderu+'\\'+fu
    folder_content = os.listdir(folder)
    canvas = Image.new('RGB', (1010,1510), "white")

    #JIKA JUMLAH FOTO GENAP KELIPATAN 12
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

            canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 1X Cetak 12lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
            print ("Selesai")
            time.sleep(3)

        for x in os.listdir("..\\temp\\"):
            os.remove("..\\temp\\"+x)
        print ("Folder sementara berhasil dihapus")

    #JIKA JUMLAH FOTO SISA 1
    elif(len(folder_content)%12 == 1) :
        for n in range(int(len(folder_content)/12)+1) :
            if n == int(len(folder_content)/12):
                tb = Image.open(folder+"\\"+folder_content[len(folder_content)-1])
                name = len(folder_content)+1
                #gambar diputar
                tb1 = tb.resize((279, 370), Image.ANTIALIAS)        
                new = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb1.size, 255)
                front = tb1.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new.paste(front, (0,0), mask)
                #gambar normal
                new1 = tb.resize((279, 370), Image.ANTIALIAS)

                new.save("..\\temp\\"+str(name).zfill(2)+".jpg","JPEG", quality=100)
                new1.save("..\\temp\\"+str(name+1).zfill(2)+".jpg","JPEG", quality=100)

                no = 0
                for i in range(12) :
                    if i >= 6:
                        im = Image.open("..\\temp\\"+str(name).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+1).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 12X Cetak 1lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

            else:
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
#                for i in os.listdir("..\\temp\\") :
                for i in range((n*12)+1, ((n*12)+12)+1) :
                    if no > 11:
                        no = 0
                    im = Image.open("..\\temp\\"+str(i).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 1X Cetak 12lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

        for x in os.listdir("..\\temp\\"):
            os.remove("..\\temp\\"+x)
        print ("Folder sementara berhasil dihapus")

    #JIKA JUMLAH FOTO SISA 2
    elif(len(folder_content)%12 == 2) :
        for n in range(int(len(folder_content)/12)+1) :
            if n == int(len(folder_content)/12):
                tb = Image.open(folder+"\\"+folder_content[len(folder_content)-1])
                tb2 = Image.open(folder+"\\"+folder_content[len(folder_content)-2])
                name = len(folder_content)+1
                #gambar diputar
                tb1 = tb.resize((279, 370), Image.ANTIALIAS)        
                new = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb1.size, 255)
                front = tb1.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new.paste(front, (0,0), mask)
                #gambar normal
                new1 = tb2.resize((279, 370), Image.ANTIALIAS)

                new.save("..\\temp\\"+str(name+1).zfill(2)+".jpg","JPEG", quality=100)
                new1.save("..\\temp\\"+str(name).zfill(2)+".jpg","JPEG", quality=100)

                no = 0
                for i in range(12) :
                    if i >= 6:
                        im = Image.open("..\\temp\\"+str(name+1).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 6X Cetak 2lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

            else:
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
                for i in range((n*12)+1, ((n*12)+12)+1) :
                    if no > 11:
                        no = 0
                    im = Image.open("..\\temp\\"+str(i).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 1X Cetak 12lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

        for x in os.listdir("..\\temp\\"):
            os.remove("..\\temp\\"+x)
        print ("Folder sementara berhasil dihapus")

    #JIKA JUMLAH FOTO SISA 3
    elif(len(folder_content)%12 == 3) :
        for n in range(int(len(folder_content)/12)+1) :
            if n == int(len(folder_content)/12):
                tb = Image.open(folder+"\\"+folder_content[len(folder_content)-1])
                tb2 = Image.open(folder+"\\"+folder_content[len(folder_content)-2])
                tb3 = Image.open(folder+"\\"+folder_content[len(folder_content)-3])
                name = len(folder_content)+1
                #gambar diputar1
                tb1 = tb2.resize((279, 370), Image.ANTIALIAS)        
                new = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb1.size, 255)
                front = tb1.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new.paste(front, (0,0), mask)
                #gambar diputar2
                tb1 = tb.resize((279, 370), Image.ANTIALIAS)        
                new2 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb1.size, 255)
                front = tb1.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new2.paste(front, (0,0), mask)
                #gambar normal
                new3 = tb3.resize((279, 370), Image.ANTIALIAS)
                new1 = tb2.resize((279, 370), Image.ANTIALIAS)

                new.save("..\\temp\\"+str(name+2).zfill(2)+".jpg","JPEG", quality=100)
                new1.save("..\\temp\\"+str(name+1).zfill(2)+".jpg","JPEG", quality=100)
                new2.save("..\\temp\\"+str(name+3).zfill(2)+".jpg","JPEG", quality=100)
                new3.save("..\\temp\\"+str(name).zfill(2)+".jpg","JPEG", quality=100)

                no = 0
                for i in range(12) :
                    if i < 4 :
                        im = Image.open("..\\temp\\"+str(name).zfill(2)+".jpg")
                    elif i >= 4 and i < 6:
                        im = Image.open("..\\temp\\"+str(name+1).zfill(2)+".jpg")
                    elif i >= 6 and i < 8:
                        im = Image.open("..\\temp\\"+str(name+2).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+3).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 4X Cetak 3lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

            else:
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
                for i in range((n*12)+1, ((n*12)+12)+1) :
                    if no > 11:
                        no = 0
                    im = Image.open("..\\temp\\"+str(i).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 1X Cetak 12lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

        for x in os.listdir("..\\temp\\"):
            os.remove("..\\temp\\"+x)
        print ("Folder sementara berhasil dihapus")

    #JIKA JUMLAH FOTO SISA 4
    elif(len(folder_content)%12 == 4) :
        for n in range(int(len(folder_content)/12)+1) :
            if n == int(len(folder_content)/12):
                tb = Image.open(folder+"\\"+folder_content[len(folder_content)-4])
                tb2 = Image.open(folder+"\\"+folder_content[len(folder_content)-3])
                tb3 = Image.open(folder+"\\"+folder_content[len(folder_content)-2])
                tb4 = Image.open(folder+"\\"+folder_content[len(folder_content)-1])
                name = len(folder_content)+1
                #gambar diputar1
                tb = tb3.resize((279, 370), Image.ANTIALIAS)        
                new3 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new3.paste(front, (0,0), mask)
                #gambar diputar2
                tb = tb4.resize((279, 370), Image.ANTIALIAS)        
                new4 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new4.paste(front, (0,0), mask)
                #gambar normal
                new = tb.resize((279, 370), Image.ANTIALIAS)
                new2 = tb2.resize((279, 370), Image.ANTIALIAS)

                new.save("..\\temp\\"+str(name).zfill(2)+".jpg","JPEG", quality=100)
                new2.save("..\\temp\\"+str(name+1).zfill(2)+".jpg","JPEG", quality=100)
                new3.save("..\\temp\\"+str(name+2).zfill(2)+".jpg","JPEG", quality=100)
                new4.save("..\\temp\\"+str(name+3).zfill(2)+".jpg","JPEG", quality=100)

                no = 0
                for i in range(12) :
                    if i < 3 :
                        im = Image.open("..\\temp\\"+str(name).zfill(2)+".jpg")
                    elif i >= 3 and i < 6:
                        im = Image.open("..\\temp\\"+str(name+1).zfill(2)+".jpg")
                    elif i >= 6 and i < 9:
                        im = Image.open("..\\temp\\"+str(name+2).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+3).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 3X Cetak 4lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

            else:
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
                for i in range((n*12)+1, ((n*12)+12)+1) :
                    if no > 11:
                        no = 0
                    im = Image.open("..\\temp\\"+str(i).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 1X Cetak 12lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

        for x in os.listdir("..\\temp\\"):
            os.remove("..\\temp\\"+x)
        print ("Folder sementara berhasil dihapus")

    #JIKA JUMLAH FOTO SISA 5
    elif(len(folder_content)%12 == 5) :
        for n in range(int(len(folder_content)/12)+1) :
            if n == int(len(folder_content)/12):
                tb1 = Image.open(folder+"\\"+folder_content[len(folder_content)-5])
                tb2 = Image.open(folder+"\\"+folder_content[len(folder_content)-4])
                tb3 = Image.open(folder+"\\"+folder_content[len(folder_content)-3])
                tb4 = Image.open(folder+"\\"+folder_content[len(folder_content)-2])
                tb5 = Image.open(folder+"\\"+folder_content[len(folder_content)-1])
                name = len(folder_content)+1
                canvas2 = Image.new('RGB', (1010,1510), "white")
                #gambar diputar1
                tb = tb2.resize((279, 370), Image.ANTIALIAS)        
                new3 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new3.paste(front, (0,0), mask)
                #gambar diputar2
                tb = tb3.resize((279, 370), Image.ANTIALIAS)        
                new4 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new4.paste(front, (0,0), mask)
                #gambar diputar2
                tb = tb5.resize((279, 370), Image.ANTIALIAS)        
                new6 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new6.paste(front, (0,0), mask)
                #gambar normal
                new = tb1.resize((279, 370), Image.ANTIALIAS)
                new2 = tb2.resize((279, 370), Image.ANTIALIAS)
                new5 = tb4.resize((279, 370), Image.ANTIALIAS)

                new.save("..\\temp\\"+str(name).zfill(2)+".jpg","JPEG", quality=100)
                new2.save("..\\temp\\"+str(name+1).zfill(2)+".jpg","JPEG", quality=100)
                new3.save("..\\temp\\"+str(name+2).zfill(2)+".jpg","JPEG", quality=100)
                new4.save("..\\temp\\"+str(name+3).zfill(2)+".jpg","JPEG", quality=100)
                new5.save("..\\temp\\"+str(name+4).zfill(2)+".jpg","JPEG", quality=100)
                new6.save("..\\temp\\"+str(name+5).zfill(2)+".jpg","JPEG", quality=100)

                no = 0
                for i in range(12) :
                    if i < 4 :
                        im = Image.open("..\\temp\\"+str(name).zfill(2)+".jpg")
                    elif i >= 4 and i < 6:
                        im = Image.open("..\\temp\\"+str(name+1).zfill(2)+".jpg")
                    elif i >= 6 and i < 8:
                        im = Image.open("..\\temp\\"+str(name+2).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+3).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                no = 0
                for c in range(12) :
                    if c >= 6 :
                        im = Image.open("..\\temp\\"+str(name+5).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+4).zfill(2)+".jpg")
                    canvas2.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 4X Cetak 3lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                canvas2.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 6X Cetak 2lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

            else:
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
                for i in range((n*12)+1, ((n*12)+12)+1) :
                    if no > 11:
                        no = 0
                    im = Image.open("..\\temp\\"+str(i).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 1X Cetak 12lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

        for x in os.listdir("..\\temp\\"):
            os.remove("..\\temp\\"+x)
        print ("Folder sementara berhasil dihapus")

    #JIKA JUMLAH FOTO SISA 6
    elif(len(folder_content)%12 == 6) :
        for n in range(int(len(folder_content)/12)+1) :
            if n == int(len(folder_content)/12):
                tb1 = Image.open(folder+"\\"+folder_content[len(folder_content)-6])
                tb2 = Image.open(folder+"\\"+folder_content[len(folder_content)-5])
                tb3 = Image.open(folder+"\\"+folder_content[len(folder_content)-4])
                tb4 = Image.open(folder+"\\"+folder_content[len(folder_content)-3])
                tb5 = Image.open(folder+"\\"+folder_content[len(folder_content)-2])
                tb6 = Image.open(folder+"\\"+folder_content[len(folder_content)-1])
                name = len(folder_content)+1
                #gambar diputar1
                tb = tb4.resize((279, 370), Image.ANTIALIAS)        
                new4 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new4.paste(front, (0,0), mask)
                #gambar diputar2
                tb = tb5.resize((279, 370), Image.ANTIALIAS)        
                new5 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new5.paste(front, (0,0), mask)
                #gambar diputar2
                tb = tb6.resize((279, 370), Image.ANTIALIAS)        
                new6 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new6.paste(front, (0,0), mask)
                #gambar normal
                new = tb1.resize((279, 370), Image.ANTIALIAS)
                new2 = tb2.resize((279, 370), Image.ANTIALIAS)
                new3 = tb3.resize((279, 370), Image.ANTIALIAS)

                new.save("..\\temp\\"+str(name).zfill(2)+".jpg","JPEG", quality=100)
                new2.save("..\\temp\\"+str(name+1).zfill(2)+".jpg","JPEG", quality=100)
                new3.save("..\\temp\\"+str(name+2).zfill(2)+".jpg","JPEG", quality=100)
                new4.save("..\\temp\\"+str(name+3).zfill(2)+".jpg","JPEG", quality=100)
                new5.save("..\\temp\\"+str(name+4).zfill(2)+".jpg","JPEG", quality=100)
                new6.save("..\\temp\\"+str(name+5).zfill(2)+".jpg","JPEG", quality=100)

                no = 0
                for i in range(12) :
                    if i < 2 :
                        im = Image.open("..\\temp\\"+str(name).zfill(2)+".jpg")
                    elif i >= 2 and i < 4:
                        im = Image.open("..\\temp\\"+str(name+1).zfill(2)+".jpg")
                    elif i >= 4 and i < 6:
                        im = Image.open("..\\temp\\"+str(name+2).zfill(2)+".jpg")
                    elif i >= 6 and i < 8:
                        im = Image.open("..\\temp\\"+str(name+3).zfill(2)+".jpg")
                    elif i >= 8 and i < 10:
                        im = Image.open("..\\temp\\"+str(name+4).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+5).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 2X Cetak 6lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

            else:
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
                for i in range((n*12)+1, ((n*12)+12)+1) :
                    if no > 11:
                        no = 0
                    im = Image.open("..\\temp\\"+str(i).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 1X Cetak 12lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

        for x in os.listdir("..\\temp\\"):
            os.remove("..\\temp\\"+x)
        print ("Folder sementara berhasil dihapus")

    #JIKA JUMLAH FOTO SISA 7
    elif(len(folder_content)%12 == 7) :
        for n in range(int(len(folder_content)/12)+1) :
            if n == int(len(folder_content)/12):
                tb = Image.open(folder+"\\"+folder_content[len(folder_content)-7])
                tb2 = Image.open(folder+"\\"+folder_content[len(folder_content)-6])
                tb3 = Image.open(folder+"\\"+folder_content[len(folder_content)-5])
                tb4 = Image.open(folder+"\\"+folder_content[len(folder_content)-4])
                tb5 = Image.open(folder+"\\"+folder_content[len(folder_content)-3])
                tb6 = Image.open(folder+"\\"+folder_content[len(folder_content)-2])
                tb7 = Image.open(folder+"\\"+folder_content[len(folder_content)-1])
                name = len(folder_content)+1
                canvas2 = Image.new('RGB', (1010,1510), "white")
                #gambar diputar1
                tb = tb4.resize((279, 370), Image.ANTIALIAS)        
                new4 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new4.paste(front, (0,0), mask)
                #gambar diputar2
                tb = tb5.resize((279, 370), Image.ANTIALIAS)        
                new5 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new5.paste(front, (0,0), mask)
                #gambar diputar3
                tb = tb6.resize((279, 370), Image.ANTIALIAS)        
                new6 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new6.paste(front, (0,0), mask)
                #gambar diputar4
                tb = tb7.resize((279, 370), Image.ANTIALIAS)        
                new8 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new8.paste(front, (0,0), mask)
                #gambar normal
                new = tb1.resize((279, 370), Image.ANTIALIAS)
                new2 = tb2.resize((279, 370), Image.ANTIALIAS)
                new3 = tb3.resize((279, 370), Image.ANTIALIAS)
                new7 = tb7.resize((279, 370), Image.ANTIALIAS)

                new.save("..\\temp\\"+str(name).zfill(2)+".jpg","JPEG", quality=100)
                new2.save("..\\temp\\"+str(name+1).zfill(2)+".jpg","JPEG", quality=100)
                new3.save("..\\temp\\"+str(name+2).zfill(2)+".jpg","JPEG", quality=100)
                new4.save("..\\temp\\"+str(name+3).zfill(2)+".jpg","JPEG", quality=100)
                new5.save("..\\temp\\"+str(name+4).zfill(2)+".jpg","JPEG", quality=100)
                new6.save("..\\temp\\"+str(name+5).zfill(2)+".jpg","JPEG", quality=100)
                new7.save("..\\temp\\"+str(name+6).zfill(2)+".jpg","JPEG", quality=100)
                new8.save("..\\temp\\"+str(name+7).zfill(2)+".jpg","JPEG", quality=100)

                no = 0
                for i in range(12) :
                    if i < 2 :
                        im = Image.open("..\\temp\\"+str(name).zfill(2)+".jpg")
                    elif i >= 2 and i < 4:
                        im = Image.open("..\\temp\\"+str(name+1).zfill(2)+".jpg")
                    elif i >= 4 and i < 6:
                        im = Image.open("..\\temp\\"+str(name+2).zfill(2)+".jpg")
                    elif i >= 6 and i < 8:
                        im = Image.open("..\\temp\\"+str(name+3).zfill(2)+".jpg")
                    elif i >= 8 and i < 10:
                        im = Image.open("..\\temp\\"+str(name+4).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+5).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                no = 0
                for i in range(12) :
                    if i >= 6:
                        im = Image.open("..\\temp\\"+str(name+7).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+6).zfill(2)+".jpg")
                    canvas2.paste(im, pos[no])
                    no+=1


                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 2X Cetak 6lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                canvas2.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+2)+' 12X Cetak 1lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

            else:
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
                for i in range((n*12)+1, ((n*12)+12)+1) :
                    if no > 11:
                        no = 0
                    im = Image.open("..\\temp\\"+str(i).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 1X Cetak 12lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

        for x in os.listdir("..\\temp\\"):
            os.remove("..\\temp\\"+x)
        print ("Folder sementara berhasil dihapus")

    #JIKA JUMLAH FOTO SISA 8
    elif(len(folder_content)%12 == 8) :
        for n in range(int(len(folder_content)/12)+1) :
            if n == int(len(folder_content)/12):
                tb = Image.open(folder+"\\"+folder_content[len(folder_content)-8])
                tb2 = Image.open(folder+"\\"+folder_content[len(folder_content)-7])
                tb3 = Image.open(folder+"\\"+folder_content[len(folder_content)-6])
                tb4 = Image.open(folder+"\\"+folder_content[len(folder_content)-5])
                tb5 = Image.open(folder+"\\"+folder_content[len(folder_content)-4])
                tb6 = Image.open(folder+"\\"+folder_content[len(folder_content)-3])
                tb7 = Image.open(folder+"\\"+folder_content[len(folder_content)-2])
                tb8 = Image.open(folder+"\\"+folder_content[len(folder_content)-1])
                name = len(folder_content)+1
                canvas2 = Image.new('RGB', (1010,1510), "white")
                #gambar diputar1
                tb = tb4.resize((279, 370), Image.ANTIALIAS)        
                new4 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new4.paste(front, (0,0), mask)
                #gambar diputar2
                tb = tb5.resize((279, 370), Image.ANTIALIAS)        
                new5 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new5.paste(front, (0,0), mask)
                #gambar diputar3
                tb = tb6.resize((279, 370), Image.ANTIALIAS)        
                new6 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new6.paste(front, (0,0), mask)
                #gambar diputar4
                tb = tb8.resize((279, 370), Image.ANTIALIAS)        
                new8 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new8.paste(front, (0,0), mask)
                #gambar normal
                new = tb1.resize((279, 370), Image.ANTIALIAS)
                new2 = tb2.resize((279, 370), Image.ANTIALIAS)
                new3 = tb3.resize((279, 370), Image.ANTIALIAS)
                new7 = tb7.resize((279, 370), Image.ANTIALIAS)

                new.save("..\\temp\\"+str(name).zfill(2)+".jpg","JPEG", quality=100)
                new2.save("..\\temp\\"+str(name+1).zfill(2)+".jpg","JPEG", quality=100)
                new3.save("..\\temp\\"+str(name+2).zfill(2)+".jpg","JPEG", quality=100)
                new4.save("..\\temp\\"+str(name+3).zfill(2)+".jpg","JPEG", quality=100)
                new5.save("..\\temp\\"+str(name+4).zfill(2)+".jpg","JPEG", quality=100)
                new6.save("..\\temp\\"+str(name+5).zfill(2)+".jpg","JPEG", quality=100)
                new7.save("..\\temp\\"+str(name+6).zfill(2)+".jpg","JPEG", quality=100)
                new8.save("..\\temp\\"+str(name+7).zfill(2)+".jpg","JPEG", quality=100)

                no = 0
                for i in range(12) :
                    if i < 2 :
                        im = Image.open("..\\temp\\"+str(name).zfill(2)+".jpg")
                    elif i >= 2 and i < 4:
                        im = Image.open("..\\temp\\"+str(name+1).zfill(2)+".jpg")
                    elif i >= 4 and i < 6:
                        im = Image.open("..\\temp\\"+str(name+2).zfill(2)+".jpg")
                    elif i >= 6 and i < 8:
                        im = Image.open("..\\temp\\"+str(name+3).zfill(2)+".jpg")
                    elif i >= 8 and i < 10:
                        im = Image.open("..\\temp\\"+str(name+4).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+5).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                no = 0
                for i in range(12) :
                    if i >= 6:
                        im = Image.open("..\\temp\\"+str(name+7).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+6).zfill(2)+".jpg")
                    canvas2.paste(im, pos[no])
                    no+=1


                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 2X Cetak 6lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                canvas2.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+2)+' 6X Cetak 2lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

            else:
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
                for i in range((n*12)+1, ((n*12)+12)+1) :
                    if no > 11:
                        no = 0
                    im = Image.open("..\\temp\\"+str(i).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 1X Cetak 12lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

        for x in os.listdir("..\\temp\\"):
            os.remove("..\\temp\\"+x)
        print ("Folder sementara berhasil dihapus")

    #JIKA JUMLAH FOTO SISA 9
    elif(len(folder_content)%12 == 9) :
        for n in range(int(len(folder_content)/12)+1) :
            if n == int(len(folder_content)/12):
                tb = Image.open(folder+"\\"+folder_content[len(folder_content)-9])
                tb2 = Image.open(folder+"\\"+folder_content[len(folder_content)-8])
                tb3 = Image.open(folder+"\\"+folder_content[len(folder_content)-7])
                tb4 = Image.open(folder+"\\"+folder_content[len(folder_content)-6])
                tb5 = Image.open(folder+"\\"+folder_content[len(folder_content)-5])
                tb6 = Image.open(folder+"\\"+folder_content[len(folder_content)-4])
                tb7 = Image.open(folder+"\\"+folder_content[len(folder_content)-3])
                tb8 = Image.open(folder+"\\"+folder_content[len(folder_content)-2])
                tb9 = Image.open(folder+"\\"+folder_content[len(folder_content)-1])
                name = len(folder_content)+1
                canvas2 = Image.new('RGB', (1010,1510), "white")
                #gambar diputar1
                tb = tb4.resize((279, 370), Image.ANTIALIAS)        
                new4 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new4.paste(front, (0,0), mask)
                #gambar diputar2
                tb = tb5.resize((279, 370), Image.ANTIALIAS)        
                new5 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new5.paste(front, (0,0), mask)
                #gambar diputar3
                tb = tb6.resize((279, 370), Image.ANTIALIAS)        
                new6 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new6.paste(front, (0,0), mask)
                #gambar diputar4
                tb = tb8.resize((279, 370), Image.ANTIALIAS)        
                new9 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new9.paste(front, (0,0), mask)
                #gambar diputar5
                tb = tb9.resize((279, 370), Image.ANTIALIAS)        
                new10 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new10.paste(front, (0,0), mask)
                #gambar normal
                new = tb1.resize((279, 370), Image.ANTIALIAS)
                new2 = tb2.resize((279, 370), Image.ANTIALIAS)
                new3 = tb3.resize((279, 370), Image.ANTIALIAS)
                new7 = tb7.resize((279, 370), Image.ANTIALIAS)
                new8 = tb8.resize((279, 370), Image.ANTIALIAS)

                new.save("..\\temp\\"+str(name).zfill(2)+".jpg","JPEG", quality=100)
                new2.save("..\\temp\\"+str(name+1).zfill(2)+".jpg","JPEG", quality=100)
                new3.save("..\\temp\\"+str(name+2).zfill(2)+".jpg","JPEG", quality=100)
                new4.save("..\\temp\\"+str(name+3).zfill(2)+".jpg","JPEG", quality=100)
                new5.save("..\\temp\\"+str(name+4).zfill(2)+".jpg","JPEG", quality=100)
                new6.save("..\\temp\\"+str(name+5).zfill(2)+".jpg","JPEG", quality=100)
                new7.save("..\\temp\\"+str(name+6).zfill(2)+".jpg","JPEG", quality=100)
                new8.save("..\\temp\\"+str(name+7).zfill(2)+".jpg","JPEG", quality=100)
                new9.save("..\\temp\\"+str(name+8).zfill(2)+".jpg","JPEG", quality=100)
                new10.save("..\\temp\\"+str(name+9).zfill(2)+".jpg","JPEG", quality=100)

                no = 0
                for i in range(12) :
                    if i < 2 :
                        im = Image.open("..\\temp\\"+str(name).zfill(2)+".jpg")
                    elif i >= 2 and i < 4:
                        im = Image.open("..\\temp\\"+str(name+1).zfill(2)+".jpg")
                    elif i >= 4 and i < 6:
                        im = Image.open("..\\temp\\"+str(name+2).zfill(2)+".jpg")
                    elif i >= 6 and i < 8:
                        im = Image.open("..\\temp\\"+str(name+3).zfill(2)+".jpg")
                    elif i >= 8 and i < 10:
                        im = Image.open("..\\temp\\"+str(name+4).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+5).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                no = 0
                for i in range(12) :
                    if i < 4 :
                        im = Image.open("..\\temp\\"+str(name+6).zfill(2)+".jpg")
                    elif i >= 4 and i < 6:
                        im = Image.open("..\\temp\\"+str(name+7).zfill(2)+".jpg")
                    elif i >= 6 and i < 8:
                        im = Image.open("..\\temp\\"+str(name+8).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+9).zfill(2)+".jpg")
                    canvas2.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 2X Cetak 6lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                canvas2.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+2)+' 4X Cetak 3lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

            else:
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
                for i in range((n*12)+1, ((n*12)+12)+1) :
                    if no > 11:
                        no = 0
                    im = Image.open("..\\temp\\"+str(i).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 1X Cetak 12lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

        for x in os.listdir("..\\temp\\"):
            os.remove("..\\temp\\"+x)
        print ("Folder sementara berhasil dihapus")

    #JIKA JUMLAH FOTO SISA 10
    elif(len(folder_content)%12 == 10) :
        for n in range(int(len(folder_content)/12)+1) :
            if n == int(len(folder_content)/12):
                tb = Image.open(folder+"\\"+folder_content[len(folder_content)-10])
                tb2 = Image.open(folder+"\\"+folder_content[len(folder_content)-9])
                tb3 = Image.open(folder+"\\"+folder_content[len(folder_content)-8])
                tb4 = Image.open(folder+"\\"+folder_content[len(folder_content)-7])
                tb5 = Image.open(folder+"\\"+folder_content[len(folder_content)-6])
                tb6 = Image.open(folder+"\\"+folder_content[len(folder_content)-5])
                #part2
                tb7 = Image.open(folder+"\\"+folder_content[len(folder_content)-4])
                tb8 = Image.open(folder+"\\"+folder_content[len(folder_content)-3])
                tb9 = Image.open(folder+"\\"+folder_content[len(folder_content)-2])
                tb10 = Image.open(folder+"\\"+folder_content[len(folder_content)-1])
                name = len(folder_content)+1
                canvas2 = Image.new('RGB', (1010,1510), "white")
                #gambar diputar1
                tb = tb4.resize((279, 370), Image.ANTIALIAS)        
                new4 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new4.paste(front, (0,0), mask)
                #gambar diputar2
                tb = tb5.resize((279, 370), Image.ANTIALIAS)        
                new5 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new5.paste(front, (0,0), mask)
                #gambar diputar3
                tb = tb6.resize((279, 370), Image.ANTIALIAS)        
                new6 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new6.paste(front, (0,0), mask)
                #part2
                #gambar diputar4
                tb = tb9.resize((279, 370), Image.ANTIALIAS)        
                new9 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new9.paste(front, (0,0), mask)
                #gambar diputar5
                tb = tb10.resize((279, 370), Image.ANTIALIAS)        
                new10 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new10.paste(front, (0,0), mask)
                #gambar normal
                new = tb1.resize((279, 370), Image.ANTIALIAS)
                new2 = tb2.resize((279, 370), Image.ANTIALIAS)
                new3 = tb3.resize((279, 370), Image.ANTIALIAS)
                new7 = tb7.resize((279, 370), Image.ANTIALIAS)
                new8 = tb8.resize((279, 370), Image.ANTIALIAS)

                new.save("..\\temp\\"+str(name).zfill(2)+".jpg","JPEG", quality=100)
                new2.save("..\\temp\\"+str(name+1).zfill(2)+".jpg","JPEG", quality=100)
                new3.save("..\\temp\\"+str(name+2).zfill(2)+".jpg","JPEG", quality=100)
                new4.save("..\\temp\\"+str(name+3).zfill(2)+".jpg","JPEG", quality=100)
                new5.save("..\\temp\\"+str(name+4).zfill(2)+".jpg","JPEG", quality=100)
                new6.save("..\\temp\\"+str(name+5).zfill(2)+".jpg","JPEG", quality=100)
                #part2
                new7.save("..\\temp\\"+str(name+6).zfill(2)+".jpg","JPEG", quality=100)
                new8.save("..\\temp\\"+str(name+7).zfill(2)+".jpg","JPEG", quality=100)
                new9.save("..\\temp\\"+str(name+8).zfill(2)+".jpg","JPEG", quality=100)
                new10.save("..\\temp\\"+str(name+9).zfill(2)+".jpg","JPEG", quality=100)

                no = 0
                for i in range(12) :
                    if i < 2 :
                        im = Image.open("..\\temp\\"+str(name).zfill(2)+".jpg")
                    elif i >= 2 and i < 4:
                        im = Image.open("..\\temp\\"+str(name+1).zfill(2)+".jpg")
                    elif i >= 4 and i < 6:
                        im = Image.open("..\\temp\\"+str(name+2).zfill(2)+".jpg")
                    elif i >= 6 and i < 8:
                        im = Image.open("..\\temp\\"+str(name+3).zfill(2)+".jpg")
                    elif i >= 8 and i < 10:
                        im = Image.open("..\\temp\\"+str(name+4).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+5).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                no = 0
                for i in range(12) :
                    if i < 3 :
                        im = Image.open("..\\temp\\"+str(name+6).zfill(2)+".jpg")
                    elif i >= 3 and i < 6:
                        im = Image.open("..\\temp\\"+str(name+7).zfill(2)+".jpg")
                    elif i >= 6 and i < 9:
                        im = Image.open("..\\temp\\"+str(name+8).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+9).zfill(2)+".jpg")
                    canvas2.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 2X Cetak 6lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                canvas2.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+2)+' 3X Cetak 4lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

            else:
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
                for i in range((n*12)+1, ((n*12)+12)+1) :
                    if no > 11:
                        no = 0
                    im = Image.open("..\\temp\\"+str(i).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 1X Cetak 12lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

        for x in os.listdir("..\\temp\\"):
            os.remove("..\\temp\\"+x)
        print ("Folder sementara berhasil dihapus")

    #JIKA JUMLAH FOTO SISA 11
    elif(len(folder_content)%12 == 11) :
        for n in range(int(len(folder_content)/12)+1) :
            if n == int(len(folder_content)/12):
                tb = Image.open(folder+"\\"+folder_content[len(folder_content)-11])
                tb2 = Image.open(folder+"\\"+folder_content[len(folder_content)-10])
                tb3 = Image.open(folder+"\\"+folder_content[len(folder_content)-9])
                tb4 = Image.open(folder+"\\"+folder_content[len(folder_content)-8])
                tb5 = Image.open(folder+"\\"+folder_content[len(folder_content)-7])
                tb6 = Image.open(folder+"\\"+folder_content[len(folder_content)-6])
                #part2
                tb7 = Image.open(folder+"\\"+folder_content[len(folder_content)-5])
                tb8 = Image.open(folder+"\\"+folder_content[len(folder_content)-4])
                tb9 = Image.open(folder+"\\"+folder_content[len(folder_content)-3])
                tb10 = Image.open(folder+"\\"+folder_content[len(folder_content)-2])
                tb11 = Image.open(folder+"\\"+folder_content[len(folder_content)-1])
                name = len(folder_content)+1
                canvas2 = Image.new('RGB', (1010,1510), "white")
                canvas3 = Image.new('RGB', (1010,1510), "white")
                #gambar diputar1
                tb = tb4.resize((279, 370), Image.ANTIALIAS)        
                new4 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new4.paste(front, (0,0), mask)
                #gambar diputar2
                tb = tb5.resize((279, 370), Image.ANTIALIAS)        
                new5 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new5.paste(front, (0,0), mask)
                #gambar diputar3
                tb = tb6.resize((279, 370), Image.ANTIALIAS)        
                new6 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new6.paste(front, (0,0), mask)
                #part2
                #gambar diputar4
                tb = tb8.resize((279, 370), Image.ANTIALIAS)        
                new9 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new9.paste(front, (0,0), mask)
                #gambar diputar5
                tb = tb9.resize((279, 370), Image.ANTIALIAS)        
                new10 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new10.paste(front, (0,0), mask)
                #gambar diputar6
                tb = tb11.resize((279, 370), Image.ANTIALIAS)        
                new12 = Image.new('RGB', (370, 279), "white")
                mask = Image.new('L', tb.size, 255)
                front = tb.rotate(90, expand=True)
                mask = mask.rotate(90, expand=True)
                new12.paste(front, (0,0), mask)
                #gambar normal
                new = tb1.resize((279, 370), Image.ANTIALIAS)
                new2 = tb2.resize((279, 370), Image.ANTIALIAS)
                new3 = tb3.resize((279, 370), Image.ANTIALIAS)
                
                new7 = tb7.resize((279, 370), Image.ANTIALIAS)
                new8 = tb8.resize((279, 370), Image.ANTIALIAS)
                new11 = tb10.resize((279, 370), Image.ANTIALIAS)

                new.save("..\\temp\\"+str(name).zfill(2)+".jpg","JPEG", quality=100)
                new2.save("..\\temp\\"+str(name+1).zfill(2)+".jpg","JPEG", quality=100)
                new3.save("..\\temp\\"+str(name+2).zfill(2)+".jpg","JPEG", quality=100)
                new4.save("..\\temp\\"+str(name+3).zfill(2)+".jpg","JPEG", quality=100)
                new5.save("..\\temp\\"+str(name+4).zfill(2)+".jpg","JPEG", quality=100)
                new6.save("..\\temp\\"+str(name+5).zfill(2)+".jpg","JPEG", quality=100)
                #part2
                new7.save("..\\temp\\"+str(name+6).zfill(2)+".jpg","JPEG", quality=100)
                new8.save("..\\temp\\"+str(name+7).zfill(2)+".jpg","JPEG", quality=100)
                new9.save("..\\temp\\"+str(name+8).zfill(2)+".jpg","JPEG", quality=100)
                new10.save("..\\temp\\"+str(name+9).zfill(2)+".jpg","JPEG", quality=100)
                new11.save("..\\temp\\"+str(name+10).zfill(2)+".jpg","JPEG", quality=100)
                new12.save("..\\temp\\"+str(name+11).zfill(2)+".jpg","JPEG", quality=100)

                no = 0
                for i in range(12) :
                    if i < 2 :
                        im = Image.open("..\\temp\\"+str(name).zfill(2)+".jpg")
                    elif i >= 2 and i < 4:
                        im = Image.open("..\\temp\\"+str(name+1).zfill(2)+".jpg")
                    elif i >= 4 and i < 6:
                        im = Image.open("..\\temp\\"+str(name+2).zfill(2)+".jpg")
                    elif i >= 6 and i < 8:
                        im = Image.open("..\\temp\\"+str(name+3).zfill(2)+".jpg")
                    elif i >= 8 and i < 10:
                        im = Image.open("..\\temp\\"+str(name+4).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+5).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                no = 0
                for i in range(12) :
                    if i < 4 :
                        im = Image.open("..\\temp\\"+str(name+6).zfill(2)+".jpg")
                    elif i >= 4 and i < 6:
                        im = Image.open("..\\temp\\"+str(name+7).zfill(2)+".jpg")
                    elif i >= 6 and i < 8:
                        im = Image.open("..\\temp\\"+str(name+8).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+9).zfill(2)+".jpg")
                    canvas2.paste(im, pos[no])
                    no+=1

                no = 0
                for c in range(12) :
                    if c >= 6 :
                        im = Image.open("..\\temp\\"+str(name+11).zfill(2)+".jpg")
                    else:   
                        im = Image.open("..\\temp\\"+str(name+10).zfill(2)+".jpg")
                    canvas3.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 2X Cetak 6lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                canvas2.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+2)+' 4X Cetak 3lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                canvas3.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+3)+' 6X Cetak 2lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

            else:
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
                for i in range((n*12)+1, ((n*12)+12)+1) :
                    if no > 11:
                        no = 0
                    im = Image.open("..\\temp\\"+str(i).zfill(2)+".jpg")
                    canvas.paste(im, pos[no])
                    no+=1

                canvas.save('..\\'+os.path.basename(folderu)+' Cetak\\'+str(fu)+str(n+1)+' 1X Cetak 12lbr.jpg', "JPEG", quality=100, dpi=(300, 300))
                print ("Selesai")
                time.sleep(3)

        for x in os.listdir("..\\temp\\"):
            os.remove("..\\temp\\"+x)
        print ("Folder sementara berhasil dihapus")

