from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
def every_100(text):
    final_text = ""
    for i in  range(0,len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text +="\n"
    return final_text

root = Tk()
root.title("Avenger News")
root.geometry("1000x800")

texts= []
photos= []
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text =  f.read()
        texts.append(every_100(text))
    image = Image.open(f"{i+1}.jpg")

    #TODO:resize the image
    image=image.resize((225,225),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f1 = Frame(root,width=800,height=70)
Label(f1,text="Avenger News",font="lucida 33 bold").pack()
Label(f1,text=f"Date : {datetime.now().date()}",font="lucida 15 bold").pack()
f1.pack()


f2 =  Frame(root,width=900,height=200)
Label(f2,text=texts[0],font="lucida 10 italic",padx=22,pady=22).pack(side="left")
Label(f2,image=photos[0],anchor="e").pack()

f3 =  Frame(root,width=900,height=200)
Label(f3,text=texts[1],font="lucida 10 italic",padx=33,pady=22).pack(side="right")
Label(f3,image=photos[2],anchor="e").pack(side="left")


f4 =  Frame(root,width=900,height=200)
Label(f4,text=texts[2],font="lucida 10 italic",padx=22,pady=22).pack(side="left")
Label(f4,image=photos[1],anchor="e").pack()

f2.pack(anchor="w")
f3.pack(anchor="w")
f4.pack(anchor="w")
root.mainloop()