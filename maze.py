from tkinter import Tk,Canvas
import tkinter.messagebox

window = Tk()
window.title("the amazing maze")
canvas = Canvas(window, width = 600, height = 600)
canvas.pack()



def you_won():
    PlayAgain =  tkinter.messagebox.askyesno('YOU WON!!! Do you want to play again?')
    if PlayAgain:
        new_game()
    else:
        window.destroy()
        raise SystemExit 
        
        
def new_game():
    canvas.coords(player, 37, 5, 52, 20)
    
walls = []

def draw_row(row, squares):
    squares = list(squares)
    column = 0
    for square in squares:
        if square == '1':
            wall = canvas.create_rectangle(column * 30, row * 30, column * 30 + 30, row * 30 + 30, fill = 'blue')
            walls.append(wall)
        column += 1
draw_row(0, '10111111111111111111')
draw_row(1, '10000100001001001001')
draw_row(2, '11010111011011010101')
draw_row(3, '10010101010010010111')
draw_row(4, '11010101011110110101')
draw_row(5, '10000101110000000001')
draw_row(6, '10110101010010111101')
draw_row(7, '10100001000110101001')
draw_row(8, '10111100010010101011')
draw_row(9, '11101001011010101011')
draw_row(10, '10001111001010100001')
draw_row(11, '11101000001000111111')
draw_row(12, '10000011111010000001')
draw_row(13, '11110000010010101101')
draw_row(14, '10011111010010101001')
draw_row(15, '10111011111011111001')
draw_row(16, '10100000010010001101')
draw_row(17, '10111011011110100001')
draw_row(18, '10000010000000110101')
draw_row(19, '10111111111111111111')

player = canvas.create_oval(37, 5, 52, 20, fill ='red')


def touching_walls(pos):
    if pos[1] <= 0:
        return True 
    for wall in walls:
        wall_pos = canvas.coords(wall)
        if pos[2] >= wall_pos[0] and pos[0] <= wall_pos[2]:
            if pos[3] >= wall_pos[1] and pos[1] <= wall_pos[3]:
                return True 
    return False 


def move_left(evt):
    pos = canvas.coords(player) 
    pos[0] -= 5
    if touching_walls(pos) == False:
        canvas.move(player, -5, 0)

def move_right(evt):
    pos = canvas.coords(player)
    pos[2] += 5
    if touching_walls(pos) == False:
        canvas.move(player, 5, 0)

def move_up(evt):
    pos = canvas.coords(player)
    pos[1] -= 5
    if touching_walls(pos) == False:
        canvas.move(player, 0, -5)

def move_down(evt):
    pos = canvas.coords(player)
    pos[3] += 5
    if touching_walls(pos) == False:
        canvas.move(player, 0, 5)
    if pos[3] > 615:
        you_won() 


canvas.bind_all('<KeyPress-Left>', move_left)
canvas.bind_all('<KeyPress-Right>', move_right)
canvas.bind_all('<KeyPress-Up>', move_up)
canvas.bind_all('<KeyPress-Down>', move_down)



window.mainloop()
    






















