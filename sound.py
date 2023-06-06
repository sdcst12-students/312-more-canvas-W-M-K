import tkinter as tk
import playsound

w = tk.Tk()
b =tk.Button(w,text='play sound')
b.pack()


def play(e):
    playsound.playsound("sound.mp3",block=False)
b.bind("<Button>",play)
w.mainloop()