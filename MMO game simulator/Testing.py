import tkinter as tk

#Create Window
window = tk.Tk()
window.title("MMO Game Simulator")
window.geometry ("1408x768")
window.configure(bg="black")
window.resizable(False, False)

fightscreenimg = tk.PhotoImage(file="bossfightbg.png")
fightscreenimg_lab = tk.Label(window, image=fightscreenimg)
fightscreenimg_lab.place(x=0, y=0, relwidth=1, relheight=1) # relwidth/height=1 stretches it 100%
        #without this it wouldnt load for some reason - directly saving the whole bg 
fightscreenimg_lab.image = fightscreenimg 



window.mainloop()

"""

canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

img = tk.PhotoImage(file="sprite.png")

canvas.create_image(250, 250, image=img)

canvas.img = img  # KEEP REFERENCE

"""