from tkinter import Tk, Frame, Menu, Label

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.window = parent
        self.initUI()
        self.membuatMenu()

    def initUI(self):
        self.window.title("Auto Organize Photo")
        self.window.geometry("250x150")

        Label(root,
        text="Digital Multimedia™",
        fg = "black",
        font = "Times").pack()
        Label(root,
        text=" ",
        fg = "black",
        font = "Times").pack()


    def membuatMenu(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="4R Cetak 12Lembar", command=self.perintahKeluar)
        menubar.add_cascade(label="Mulai", menu=fileMenu)

    def perintahKeluar(self):
        Label(root,
        text="Sedang memproses foto..",
        fg = "yellow",
        bg = "blue",
        font = "Times").pack()

        import autodraw

        Label(root,
        text="Foto telah selesai diproses!",
        fg = "red",
        bg = "yellow",
        font = "Times").pack()

        Label(root,
        text=" ",
        fg = "red",
        font = "Times").pack()
        root.mainloop()
        
if __name__ == '__main__':
    root = Tk()
    app = Example(root)
    root.mainloop()
