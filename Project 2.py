#Pixel Manipulation for Image Encryption 
from tkinter import *
from tkinter import filedialog
root=Tk()
root.geometry("200x160")
def encrypt_image():
    file1=filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg'),('png file','*.png')])
    if file1 is not None:
        print("file",file1)
        file_name=file1.name
        print("Name of the file: ",file_name)
        key=entry1.get(1.0,END)
        print(file_name,key)
        fi=open(file_name,'rb')
        image=fi.read()
        fi.close()
        image=bytearray(image)                
        for index,values in enumerate(image):   #provides index to values
            image[index]=values ^ int(key)
        fi1=open(file_name,'wb')
        fi1.write(image)
        fi1.close()
b1=Button(root,text="encrypt",command=encrypt_image)
b1.place(x=70, y=10)
entry1=Text(root,height=1,width=10)
entry1.place(x=50,y=50)
root.mainloop()

