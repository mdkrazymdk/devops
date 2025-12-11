from tkinter import *

class Score:
    def __init__(self, canvas):
        self.canvas = canvas
        self.score = 0  # Спіймані
        self.lost = 0   # Пропущені
        self.text = None
        self.show_text()

    def show_text(self):
        # Якщо тексту ще немає, створюємо його
        if self.text is None:
            self.text = self.canvas.create_text(350, 20, text=f"Спіймав: 0 Пропустив: 0", font=('Helvetica', 16), fill='black')
        else:
            # Якщо є, оновлюємо
            self.canvas.itemconfig(self.text, text=f"Спіймав: {self.score} Пропустив: {self.lost}")

    def catched_egg(self):
        self.score += 1
        self.show_text()

    def lost_egg(self):
        self.lost += 1
        self.show_text()
