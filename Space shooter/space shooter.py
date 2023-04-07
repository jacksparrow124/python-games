from tkinter import *
import time
import tkinter.messagebox
import winsound
import random


window = Tk()
window.title('space shooter')
local_path="c:/Users/ajone/Desktop/python/beginner-python-games/Space shooter/"



img1 = PhotoImage(file = local_path+'images/ship.png')
img2 = PhotoImage(file = local_path+'images/missle_purple.png')
img3 = PhotoImage(file = local_path+'images/missle_red.png')

points = 0





def play_shoot():
    winsound.PlaySound(local_path+'sounds/shoot.wav', 1)

def play_boom():
    winsound.PlaySound(local_path+'sounds/explosion.wav', 1)

def play_launch():
    winsound.PlaySound(local_path+'sounds/launch.wav', 1)


  






def new_game():
    active = True 
    global points
    global canvas
    global ship
    points = 0 
    play_launch()
    canvas = Canvas(window, width = 800, height = 650)
    canvas.pack()
    ship = canvas.create_image(360, 550, anchor=NW, image=img1)
    missile1 = canvas.create_image(200, 100, anchor=NW, image = img2)
    missile2 = canvas.create_image(500, 100, anchor = NW, image = img3)
    score = Label(window, text = 'Score = 0')
    score.config(font = ('Courier', 24))
    score.pack()
    
    def move_left(evt):
        pos = canvas.coords(ship)
        if pos[0] > 0:
            canvas.move(ship, -15, 0)

    def move_right(evt):
        pos = canvas.coords(ship)
        if pos[0] < 730:
            canvas.move(ship, 15, 0)
   
shots = []
    def shoot(evt):
        pos = Canvas.coords(ship)
        shot = Canvas.create_rectangle(pos[0]+35, 530, pos[0]+40, 540, fill='green')
        shots.append(shot)
        play_shoot()






    def move_shots():
        for shot in shots:
            canvas.move(shot, 0, -5)
        pos = canvas.coords(shot)
        if pos[1] <= 0:
            canvas.delete(shot)
            shots.remove(shot)

    def move_missiles():
        canvas.move(missile1, 0, 2)
        pos = canvas.coords(missile1)
        ship_pos = canvas.coords(ship)
        if pos[1]+257 >= 650:
            print ('game over')
        elif pos[1]+257 >= 550 and pos[0]+67 >= ship_pos[0] and pos[0] <= ship_pos[0]+67:
            print ('game over')
         canvas.move(missile2, 0, 2)
        pos = canvas.coords(missile2)
        ship_pos = canvas.coords(ship)
        if pos[1]+257 >= 650:
            print ('game over')
        elif pos[1]+257 >= 550 and pos[0]+67 >= ship_pos[0] and pos[0] <= ship_pos[0]+67:
            print ('game over')

    def reset_missile():
        


        canvas.bind_all('<KeyPress-Right>', move_right)
        canvas.bind_all('<KeyPress-Left>', move_left)
        canvas.bind_all('KeyPress-Up', shoot)

    
    while active:
        move_shots()
        window.update()
        time.sleep(.015)



new_game()











