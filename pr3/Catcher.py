from tkinter import *


class Catcher:
    def __init__(self, canvas, color, score):
        self.canvas = canvas
        self.score = score
 
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)

        self.canvas.move(self.id, 200, 350)

        self.x = 0
        self.canvas_width = self.canvas.winfo_width()


        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -3  

    def turn_right(self, evt):
        self.x = 3  

    def draw(self):
       
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

      
        if pos[0] <= 0:
            self.x = 0
       
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def catch(self, eggs):
        
        catcher_pos = self.canvas.coords(self.id)

       
        for egg in eggs:
            egg_pos = self.canvas.coords(egg.id)
            
            if catcher_pos[0] < egg_pos[2] and egg_pos[0] < catcher_pos[2] and catcher_pos[1] < egg_pos[3] and egg_pos[
                1] < catcher_pos[3]:
                eggs.remove(egg)  
                self.canvas.delete(egg.id)  
                self.score.catched_egg()  
