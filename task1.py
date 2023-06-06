import tkinter as tk
import csv
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#00EEEE")
c.pack()


f = open('map1.txt')
data = f.read()
print(data)
for i in data:
    print(i)
    

exit()
rec = c.create_rectangle(20,20,40,40,fill="#006400")
def keyPress(event):
    key = event.keysym
    x1, y1, x2, y2 = c.coords(rec)
    distance = 10  

    if key == "Left":
        if x1 - distance >= 0:
            c.move(rec, -distance, 0)
    elif key == "Right":
        if x2 + distance <= c.winfo_width():
            c.move(rec, distance, 0)
    elif key == "Up":
        if y1 - distance >= 0:
            c.move(rec, 0, -distance)
    elif key == "Down":
        if y2 + distance <= c.winfo_height():
            c.move(rec, 0, distance)
    

w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)


w.mainloop()