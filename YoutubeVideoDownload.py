from tkinter import *
from tkinter import messagebox
import pytube

def download():
    getext = box.get()
    if len(getext) != 0:
        try:
            tube = pytube.YouTube(getext)
            tube.streams.first().download()
            messagebox.showinfo("Video Download", "Downloaded SuccessFully")
        except:
            messagebox.showerror("Video", "Sorry!, This video is not doenloded. please try again....")
    else:
        messagebox.showinfo("Video Download", "Please, Enter The YouTube Link In Link Box.")


win = Tk()
win.title("YouTube Video Downloader")
win.geometry("500x300")


link = Label(win, text="Youtube Link", font="20")

box = Entry(win, width=35, font="20")

submit = Button(win, text="Download", font="20", width=35, command=download)


link.place(x=40, y=50)
box.place(x=150, y=50)
submit.place(x=100, y=130)


win.mainloop()

