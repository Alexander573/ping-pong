from tkinter import*
from time import sleep
import random




class Score:
    def __init__(self,canvas,color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(300,10,text = f'Текущий счёт: {self.score}',font = ('Courier',15),fill = color)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id,text = f'Текущий счёт: {self.score}')



class Ball:
    def __init__(self,canvas,color,paddle,score):
        self.paddle = paddle
        self.canvas = canvas
        self.score = score
        self.hit_bottom = False
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        start = [-2,-1,1,2]
        self.x = random.choice(start)
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()





    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)

        if pos[0]<=0:
            self.x = 2
        if pos[2]>=self.canvas_width:
            self.x = -2

        if self.hit_paddle(pos):
            self.y = -2

        if pos[1]<=0:
            self.y=2
        if pos[3]>= self.canvas_height:
            self.hit_bottom = True


    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()
                return True
            return False

class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill = color)
        self.canvas.move(self.id,250,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Right>',self.trunc_right)
        self.canvas.bind_all('<KeyPress-Left>', self.trunc_left)


    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas_width:
            self.x=0

    def trunc_right(self,event):
        self.x = 2

    def trunc_left(self,event):
        self.x = -2



root = Tk()
root.title('прыг-скок')
root.resizable(0,0)
root.wm_attributes('-topmost',1)



canvas = Canvas(root,width=500,height=400,bd=0,highlightthickness=0)



canvas.pack()
root.update()


score = Score(canvas,'green')
paddle = Paddle(canvas,'purple')
ball = Ball(canvas,'red',paddle,score)


while True:
    if  ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        root.update_idletasks()
        root.update()
        sleep(0.01)
    else:
        final = canvas.create_text(250,200,text= f'Вы проиграли.ваш счёт: {score.score}')
        root.update()
        sleep(3)
        break
