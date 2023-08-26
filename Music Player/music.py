from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer
co1 = "#ffffff"
co2 = "#3C1DC6"
co3 = "#333333"
co4 = "#CFC7F8"
window = Tk()
window.title("")
window.geometry('352x255')
window.configure(background=co1)
window.resizable(width=FALSE,height=FALSE)
right = Frame(window, width=250,height=150,bg = co3)
right.grid(row=0,column=1,padx=0)
left = Frame(window,width=150,height=150,bg=co1)
left.grid(row=0,column=0,padx=1,pady=1)

down = Frame(window,width=400,height=100,bg=co4)
down.grid(row=1,column=0,columnspan=3,padx=0,pady=1)

listbox = Listbox(right,selectmode=SINGLE,font=("Arial 9 bold"),width=22,bg=co3,fg=co1)
listbox.grid(row=0,column=0)

os.chdir(r'/Users/blessykancharla/Desktop/music')
songs = os.listdir()

def show():
    for i in songs:
        listbox.insert(END, i)
show()
def playm():
    running = listbox.get(ACTIVE)
    run['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pausem():
    mixer.music.pause()

def continuem():
    mixer.music.unpause()

def stopm():
    mixer.music.stop()

def nextm():
    playing = run['text']
    if playing == 'Choose a Song':
        return
    index = songs.index(playing)
    new_index = index + 1
    if new_index >= len(songs):
        new_index = 0
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)
    show()
    listbox.select_set(new_index)
    run['text'] = playing

def prevm():
    playing = run['text']
    index = songs.index(playing)
    new_index = index - 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()
    listbox.delete(0,END)
    show()
    listbox.select_set(new_index)
    run['text'] = playing

w = Scrollbar(right)
w.grid(row=0,column=1,sticky=N+S)

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)

img1 = Image.open('/Users/blessykancharla/Desktop/Codeclause(py)/icon1.png')
img1 = img1.resize((130, 130))
img1 = ImageTk.PhotoImage(img1)
app = Label(left,height=130,image=img1,padx=10)
app.place(x=24,y=15)

img2 = Image.open('/Users/blessykancharla/Desktop/Codeclause(py)/playy.png')
img2 = img2.resize((30, 30))
img2 = ImageTk.PhotoImage(img2)
prev = Button(down,width=40,height=40,image=img2,padx=10,bg=co1,font=("Ivy 10"),command=playm)
prev.place(x=56+28,y=35)

img3 = Image.open('/Users/blessykancharla/Desktop/Codeclause(py)/prev.png')
img3 = img3.resize((30, 30))
img3 = ImageTk.PhotoImage(img3)
play = Button(down,width=40,height=40,image=img3,padx=10,bg=co1,font=("Ivy 10"),command=prevm)
play.place(x=10+28,y=35)

img4 = Image.open('/Users/blessykancharla/Desktop/Codeclause(py)/f.png')
img4 = img4.resize((30, 30))
img4 = ImageTk.PhotoImage(img4)
forw = Button(down,width=40,height=40,image=img4,padx=10,bg=co1,font=('Ivy 10'),command=nextm)
forw.place(x=102+28,y=35)

img5 = Image.open('/Users/blessykancharla/Desktop/Codeclause(py)/pause.png')
img5 = img5.resize((30, 30))
img5 = ImageTk.PhotoImage(img5)
pause = Button(down,width=40,height=40,image=img5,padx=10,bg=co1,font=("Ivy 10"),command=pausem)
pause.place(x=148+28,y=35)

img6 = Image.open('/Users/blessykancharla/Desktop/Codeclause(py)/cont.png')
img6 = img6.resize((30, 30))
img6 = ImageTk.PhotoImage(img6)
continue_ = Button(down,width=40,height=40,image=img6,padx=10,bg=co1,font=("Ivy 10"),command=continuem)
continue_.place(x=194+28,y=35)

img7 = Image.open('/Users/blessykancharla/Desktop/Codeclause(py)/stop.png')
img7 = img7.resize((30, 30))
img7 = ImageTk.PhotoImage(img7)
stop = Button(down,width=40,height=40,image=img7,padx=10,bg=co1,font=('Ivy 10'),command=stopm)
stop.place(x=240+28,y=35)

line = Label(left,width=300,height=1,padx=10,bg=co3)
line.place(x=0,y=1)

line = Label(left,width=200,height=1,padx=10,bg=co1)
line.place(x=0,y=3)

run = Label(down,text="Choose a Song",font={"Ivy 10"}, width=44,height=1,padx=10,bg=co1,fg=co3,anchor=NW)
run.place(x=0,y=1)

mixer.init()
music_state = StringVar()
music_state.set("Choose one!")

window.mainloop()
