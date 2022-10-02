import cv2
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

def rgb_to_hex(r, g, b):
    return ('{:X}{:X}{:X}').format(r,g,b)

def logscreen(image1="image.png",bgcolor="#FFFFFF"):
    global root,canvas1,image_container,bg
    root=Tk()
    root.title('Adaptive Theme')
    root.geometry('900x540')
    bg = PhotoImage(file = image1)
    canvas1 = Canvas( root, width = 900,height = 700)
    canvas1.pack()
    image_container=canvas1.create_image( 0, 0, image = bg,anchor = "nw")
    canvas1.create_text( 200, 250, text = "Adaptive Theme")
    open_button =Button(root,text='Open a File',command=select_file,bg=bgcolor)
    open_button.place(x=400, y=400)
    root.mainloop()
def update_image(filename):
   canvas1.itemconfig(image_container,image=filename)

def select_file():
    global filename,bg
    filetypes = (
        ('Images', '*.png'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Select a Image',
        initialdir='E:\Wallpapers',
        filetypes=filetypes)
    try:
        image = cv2.imread(filename)
    except:
        image = cv2.imread("image.png")

    (B, G, R) = image[100, 100]
    global bgcolor
    bgcolor='#'+rgb_to_hex(R, G, B)
    open_button =Button(root,text='Open a File',command=select_file,bg=bgcolor)
    open_button.place(x=400, y=400)
    bg = PhotoImage(file = filename)
    image_container=canvas1.create_image( 0, 0, image = bg,anchor = "nw")

    
    root.update()

    



try:
    image = cv2.imread(filename)
except:
    image = cv2.imread("image.png")

(B, G, R) = image[100, 100]
bgcolor='#'+rgb_to_hex(R, G, B)

  



if __name__=='__main__':
	logscreen()
