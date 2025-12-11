from tkinter import *

class Score:
    def __init__(self, canvas):
        self.canvas = canvas
        self.score = 0  
        self.lost = 0   
        self.text = None
        self.show_text()

    def show_text(self):
        
        if self.text is None:
            self.text = self.canvas.create_text(350, 20, text=f"Спіймав: 0 Пропустив: 0", font=('Helvetica', 16), fill='black')
        else:
       
            self.canvas.itemconfig(self.text, text=f"Спіймав: {self.score} Пропустив: {self.lost}")

    def catched_egg(self):
        self.score += 1
        self.show_text()

    def lost_egg(self):
        self.lost += 1
        self.show_text()
