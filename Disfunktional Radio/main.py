import tkinter as tk
import fnmatch
import os
from turtle import width
from pygame import mixer

canvas = tk.Tk()
canvas.title("Disfunktional Radio")
canvas.geometry("500x400")
canvas.config(bg="white")

rootpath = "C:\\Users\Jimmy\Music\Downloads"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file="prev.png")
next_img = tk.PhotoImage(file="next.png")
play_img = tk.PhotoImage(file="play.png")
pause_img = tk.PhotoImage(file="pause.png")
stop_img = tk.PhotoImage(file="stop.png")

def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear("active")

def next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, "end")
    listBox.activate(next_song)
    listBox.select_set(next_song)

def prev():
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listBox.get(prev_song)
    label.config(text=prev_song_name)

    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()

    listBox.select_clear(0, "end")
    listBox.activate(prev_song)
    listBox.select_set(prev_song)

def pause():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"


listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=("poppins", 10))
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text="", bg="white", fg="black", font=("poppins", 10))
label.pack(pady=5)

top = tk.Frame(canvas, bg="white")
top.pack(padx=15, pady=15, anchor="center")

prevButton = tk.Button(canvas, text="Prev", image=prev_img, bg="white", borderwidth=0, command=prev)
prevButton.pack(pady=15, in_=top, side="left")

stopButton = tk.Button(canvas, text="Stop", image=stop_img, bg="white", borderwidth=0, command=stop)
stopButton.pack(pady=15, in_=top, side="left")

playButton = tk.Button(canvas, text="Play", image=play_img, bg="white", borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side="left")

pauseButton = tk.Button(canvas, text="Pause", image=pause_img, bg="white", borderwidth=0, command=pause)
pauseButton.pack(pady=15, in_=top, side="left")

nextButton = tk.Button(canvas, text="Next", image=next_img, bg="white", borderwidth=0, command=next)
nextButton.pack(pady=15, in_=top, side="left")

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert("end", filename)

canvas.mainloop()