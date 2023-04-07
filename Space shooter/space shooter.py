from tkinter import *
import time
import tkinter.messagebox
import winsound
import random


window = Tk()
window.title('space shooter')


img1 = PhotoImage(file = 'images/ship.png')
img2 = PhotoImage(file = 'images/missle_purple.png')
img3 = PhotoImage(file = 'images/missle_red.png')

points = 0

def play_shoot():
    winsound.PlaySound('C:/Users/ajone/Desktop/PYTHONCLASS/beginner-python-games/sounds/shoot', 1)
    
def play_boom():
    winsound.PlaySound('C:/Users/ajone/Desktop/PYTHONCLASS/beginner-python-games/sounds/explosion', 1)
    
def play_launch():
    winsound.PlaySound('C:/Users/ajone/Desktop/PYTHONCLASS/beginner-python-games/sounds/launch', 1)
    
def new_game():
    active = True 
    global points
    points = 0 
    play_launch()
    canvas = Canvas(window, width = 800, height = 650)
    canvas.pack()
    ship = canvas.create_image(360, 550, anchor=NW, image=img1)
    missile1 = canvas.create_image(200, 100, anchor=NW, image = img2)
    missile2 = canvas.create_image(500, 100, anchor = NW, image = img3)
    score = Label(window, text = 'Score = 0')
    score.config(font = ('Courier', 24))
    


window.mainloop()











